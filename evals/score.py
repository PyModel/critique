#!/usr/bin/env python3
"""Score independent human grades, not report keywords. Offline; never runs targets."""
import json
import math
import re
import statistics
import sys
from pathlib import Path

ARMS = ('plain', 'previous', 'candidate')


def unique_keys(pairs):
    values = {}
    for key, value in pairs:
        if key in values:
            raise ValueError(f'duplicate JSON key: {key}')
        values[key] = value
    return values


def read_trials(path):
    rows = json.loads(path.read_text(), object_pairs_hook=unique_keys)
    if not isinstance(rows, list):
        raise ValueError('grades must be a JSON array')
    root = path.resolve().parent
    sheet = path.stat()
    artifacts = {(sheet.st_dev, sheet.st_ino)}
    for row in rows:
        ref = Path(row['review'])
        review = (root / ref).resolve()
        if ref.is_absolute() or root not in review.parents or not review.is_file():
            raise ValueError('review reference must identify a local file inside the results directory')
        stat = review.stat()
        identity = (stat.st_dev, stat.st_ino)
        if identity in artifacts:
            raise ValueError(f'reused review artifact: {ref}')
        artifacts.add(identity)
        words = len(review.read_text().split())
        if not words:
            raise ValueError(f'empty review: {ref}')
        row['words'] = words
    return rows


def score(criteria, rows):
    if not isinstance(rows, list) or not rows:
        raise ValueError('no graded trials')
    matrix, revisions, setups = {}, {}, set()
    for row in rows:
        case, arm, trial = row['case'], row['arm'], row['trial']
        if case not in criteria or arm not in ARMS or type(trial) is not int or trial < 1:
            raise ValueError('unknown case, arm or trial')
        key = (case, arm, trial)
        if row.get('status', 'completed') != 'completed':
            raise ValueError(f'{key}: trial did not complete')
        if key in matrix:
            raise ValueError(f'duplicate trial: {key}')
        for field in ('model', 'tools', 'revision', 'review'):
            if not isinstance(row[field], str) or not row[field].strip():
                raise ValueError(f'{key}: missing {field}')
        setups.add((row['model'], row['tools']))
        revision = row['revision']
        if arm == 'plain':
            if revision != 'none':
                raise ValueError(f'{key}: plain arm requires revision "none"')
        elif not re.fullmatch(r'(?:[0-9a-f]{40}|[0-9a-f]{64})', revision):
            raise ValueError(f'{key}: identify the skill with a full commit or content hash')
        if revisions.setdefault(arm, revision) != revision:
            raise ValueError(f'{arm}: mixed revisions')
        groups = criteria[case]
        expected = set().union(*groups.values())
        marks = row['marks']
        if not isinstance(marks, dict) or set(marks) != expected:
            raise ValueError(f'{key}: grade every criterion exactly once')
        for item, mark in marks.items():
            if (not isinstance(mark, list) or len(mark) != 2 or type(mark[0]) is not bool
                    or not isinstance(mark[1], str) or not mark[1].strip()):
                raise ValueError(f'{key} {item}: need [observed boolean, deciding evidence]')
        high = row['unsupported_high']
        if not isinstance(high, list) or any(not isinstance(h, str) or not h.strip() for h in high):
            raise ValueError(f'{key}: unsupported_high must list the unsubstantiated P0/P1 claims')
        for metric in ('words', 'tokens', 'elapsed_s', 'cost_usd'):
            value = row.get(metric)
            if value is not None and (type(value) not in (int, float) or not math.isfinite(value) or value < 0):
                raise ValueError(f'{key}: invalid {metric}')
        matrix[key] = row
    if len(setups) != 1:
        raise ValueError('model and tool/permission profile must match across arms')
    trials = {t for _, _, t in matrix}
    required = {(c, a, t) for c in criteria for a in ARMS for t in trials}
    if len(trials) < 2 or required != matrix.keys():
        raise ValueError('incomplete release matrix: repeat each case on all three arms at least twice')
    if revisions['previous'] == revisions['candidate']:
        raise ValueError('previous and candidate must identify different skill snapshots')
    results, blockers = [], []
    for trial in sorted(trials):
        found = {}
        for arm in ARMS:
            detected, total, optimizations, possible, alarms = set(), 0, 0, 0, 0
            for case, groups in criteria.items():
                row = matrix[case, arm, trial]
                seen = {item for item, mark in row['marks'].items() if mark[0]}
                wanted = set(groups['critical'] + groups['other'] + groups['optimization'])
                detected.update((case, item) for item in wanted & seen)
                total += len(wanted)
                forbidden = seen.intersection(groups['forbidden'])
                if groups['optimization']:
                    possible += 1
                    if set(groups['optimization']) <= seen and not forbidden:
                        optimizations += 1
                alarms += len(forbidden)
                if arm == 'candidate':
                    required_hits = set(groups['critical'] + groups['optimization'])
                    failures = sorted((required_hits - seen) | forbidden) + row['unsupported_high']
                    blockers.extend(f'{case} trial {trial}: {f}' for f in failures)
            found[arm] = detected
            high = sum(len(matrix[c, arm, trial]['unsupported_high']) for c in criteria)
            metrics = []
            for metric in ('words', 'tokens', 'elapsed_s', 'cost_usd'):
                values = [matrix[c, arm, trial].get(metric) for c in criteria]
                if all(v is not None for v in values):
                    metrics.append(f'{metric} median {statistics.median(values):g}')
            results.append(f'{arm} trial {trial}: expected {len(detected)}/{total}; optimization {optimizations}/{possible}; forbidden {alarms}; unsupported P0/P1 {high}; ' + ', '.join(metrics))
        for base in ARMS[:2]:
            added = sorted(found['candidate'] - found[base])
            lost = sorted(found[base] - found['candidate'])
            results.append(f'candidate vs {base} trial {trial}: added {added}; missed {lost}')
    return results, blockers


def main(argv):
    if len(argv) != 1:
        print('Usage: python3 evals/score.py GRADES.json', file=sys.stderr)
        return 2
    try:
        criteria = json.loads(Path(__file__).with_name('criteria.json').read_text(), object_pairs_hook=unique_keys)
        rows = read_trials(Path(argv[0]))
        results, blockers = score(criteria, rows)
    except (OSError, ValueError, TypeError, KeyError, AttributeError, OverflowError) as exc:
        print(f'INCOMPLETE: {exc}', file=sys.stderr)
        return 2
    print('\n'.join(results + ['BLOCK: ' + b for b in blockers]))
    return int(bool(blockers))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
