"""Offline regressions for wiring, release decisions, and the benign optimization oracle."""
import copy
import io
import itertools
import json
import re
import runpy
import shutil
import sqlite3
import tempfile
import unittest
from contextlib import closing, redirect_stdout
from pathlib import Path
from unittest.mock import patch

import check

ROOT = check.ROOT
grading = runpy.run_path(str(ROOT / 'evals/score.py'))
score = grading['score']


class WiringTests(unittest.TestCase):
    def test_empty_pass_fails_even_with_valid_registration(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in ('SKILL.md', 'HOW_TO_EXTEND.md', 'CHANGELOG.md'):
                shutil.copy(ROOT / name, root / name)
            for name in ('passes', 'packs', 'evals'):
                shutil.copytree(ROOT / name, root / name)
            target = root / 'passes/pass-05-security.md'
            target.write_text(target.read_text().split('Assume:', 1)[0])
            with patch.object(check, 'ROOT', root), redirect_stdout(io.StringIO()) as log:
                self.assertEqual(check.main(), 1)
            self.assertIn('pass-05-security.md: pass body is empty', log.getvalue())

    def test_standalone_hazard_routes(self):
        for name, required in [('agent', {'08', '24'}), ('ux', {'08', '15'})]:
            line = (ROOT / f'packs/{name}.md').read_text().split('## Passes\n\n')[1].splitlines()[0]
            self.assertLessEqual(required, set(re.findall(r'\b\d{2}\b', line)))


class ScoreTests(unittest.TestCase):
    def setUp(self):
        self.criteria = {'example': {'critical': ['risk'], 'other': ['coverage'], 'optimization': ['batch'], 'forbidden': ['false-alarm']}}
        revisions = {'plain': 'none', 'previous': 'a' * 40, 'candidate': 'b' * 64}
        self.rows = [dict(arm=a, case='example', trial=t, model='fixture-model', tools='static', revision=revisions[a],
                          review=f'{a}-{t}.md', marks={k: [v, 'fixture evidence'] for k, v in
                          [('risk', True), ('coverage', True), ('batch', a == 'candidate'), ('false-alarm', False)]}, unsupported_high=[])
                     for t in (1, 2) for a in ('plain', 'previous', 'candidate')]

    def test_raw_evidence_must_exist_under_results_root(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            grades = root / 'grades.json'
            (root / 'review.md').write_text('two words')
            for ref in ['review.md', '../other.md', '/tmp/other.md', 'missing.md']:
                grades.write_text(json.dumps([{'review': ref}]))
                if ref == 'review.md':
                    self.assertEqual(grading['read_trials'](grades)[0]['words'], 2)
                else:
                    with self.assertRaises(ValueError):
                        grading['read_trials'](grades)
            grades.write_text(json.dumps([{'review': 'review.md'}, {'review': './review.md'}]))
            with self.assertRaisesRegex(ValueError, 'reused review artifact'):
                grading['read_trials'](grades)
            (root / 'alias.md').hardlink_to(root / 'review.md')
            grades.write_text(json.dumps([{'review': 'review.md'}, {'review': 'alias.md'}]))
            with self.assertRaisesRegex(ValueError, 'reused review artifact'):
                grading['read_trials'](grades)

    def test_grade_sheet_cannot_be_its_own_review(self):
        with tempfile.TemporaryDirectory() as directory:
            grades = Path(directory) / 'grades.json'
            grades.write_text(json.dumps([{'review': grades.name}]))
            with self.assertRaises(ValueError):
                grading['read_trials'](grades)

    def test_conflicting_duplicate_marks_are_invalid(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'review.md').write_text('review')
            grades = root / 'grades.json'
            grades.write_text('[{"review":"review.md","marks":{"risk":[false,"absent"],"risk":[true,"seen"]}}]')
            with self.assertRaisesRegex(ValueError, 'duplicate.*risk'):
                grading['read_trials'](grades)

    def test_per_trial_uplift(self):
        lines, blockers = score(self.criteria, self.rows)
        self.assertFalse(blockers)
        self.assertIn("candidate vs plain trial 2: added [('example', 'batch')]; missed []", lines)

    def test_release_blockers(self):
        for field, value in [('risk', False), ('batch', False), ('false-alarm', True), ('unsupported_high', ['unproven P0'])]:
            with self.subTest(field=field):
                rows = copy.deepcopy(self.rows)
                if field == 'unsupported_high':
                    rows[-1][field] = value
                else:
                    rows[-1]['marks'][field][0] = value
                self.assertTrue(score(self.criteria, rows)[1])

    def test_missing_duplicate_or_incomparable_rows_do_not_pass(self):
        for rows in ([], self.rows[:3], self.rows[1:], self.rows + [self.rows[0]],
                     [dict(self.rows[0], tools='different')] + self.rows[1:],
                     [dict(self.rows[0], marks={})] + self.rows[1:]):
            with self.subTest(rows=len(rows)), self.assertRaises(ValueError):
                score(self.criteria, rows)

    def test_each_arm_identifies_what_ran(self):
        for arm, revision in [('plain', 'b' * 64), ('previous', 'none'), ('candidate', 'none'),
                              ('previous', 'main'), ('candidate', 'a' * 40)]:
            rows = [dict(row, revision=revision) if row['arm'] == arm else row for row in self.rows]
            with self.subTest(arm=arm), self.assertRaises(ValueError):
                score(self.criteria, rows)
        self.rows[0]['status'] = 'blocked'
        with self.assertRaises(ValueError):
            score(self.criteria, self.rows)

    def test_unrepresentable_metric_is_incomplete(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            row = dict(self.rows[0], case='crit-01', tokens=10**400)
            criteria = json.loads((ROOT / 'evals/criteria.json').read_text())
            row['marks'] = {item: [False, 'absent'] for group in criteria['crit-01'].values() for item in group}
            (root / row['review']).write_text('review')
            grades = root / 'grades.json'
            grades.write_text(json.dumps([row]))
            with patch('sys.stderr', new_callable=io.StringIO):
                self.assertEqual(grading['main']([str(grades)]), 2)

    def test_optimization_requires_equivalent_output(self):
        criteria = json.loads((ROOT / 'evals/criteria.json').read_text())
        for case, missed in [('crit-06', 'distinct-editable-rows'), ('crit-06', 'ordering-and-misses'),
                             ('crit-09', 'output-equivalence'), ('crit-09', 'zero-calls-for-empty')]:
            with self.subTest(case=case, missed=missed):
                groups = criteria[case]
                rows = []
                for row in self.rows:
                    marks = {item: [kind != 'forbidden', 'fixture evidence'] for kind, ids in groups.items() for item in ids}
                    if row['arm'] == 'candidate':
                        marks[missed][0] = False
                    rows.append(dict(row, case=case, marks=marks))
                lines, blockers = score({case: groups}, rows)
                self.assertTrue(any(missed in blocker for blocker in blockers))
                self.assertTrue(any(line.startswith('candidate trial 1:') and 'optimization 0/1' in line for line in lines))


class InvariantTests(unittest.TestCase):
    def test_preference_set_is_naturally_idempotent_in_fixture(self):
        disable = runpy.run_path(str(ROOT / 'evals/fixtures/crit-07/service.py'))['disable_reminders']
        with closing(sqlite3.connect(':memory:')) as db:
            db.execute('CREATE TABLE preferences (enabled INTEGER)')
            db.execute('INSERT INTO preferences VALUES (1)')
            for expected_changes in (1, 0):
                before = db.total_changes
                disable(db)
                self.assertEqual(db.total_changes - before, expected_changes)
                self.assertEqual(db.execute('SELECT enabled FROM preferences').fetchall(), [(0,)])


class OptimizationTests(unittest.TestCase):
    def test_grouped_results_and_alias_negative_control(self):
        source = runpy.run_path(str(ROOT / 'evals/fixtures/crit-06/report_groups.py'))['report_groups']
        for req in itertools.product(('a', 'b', 'missing'), repeat=3):
            for rows in ([], [('a', 'last'), ('a', 'first'), ('a', 'first'), ('b', 'other')]):
                buckets = {g: [] for g in req}
                for k, v in rows:
                    if k in buckets:
                        buckets[k].append(v)
                reference = source(req, rows)
                candidate = [buckets[g].copy() for g in req]
                self.assertEqual(reference, candidate)
                self.assertEqual(len({id(r) for r in candidate}), len(req))
                if len(set(req)) != len(req):
                    unsafe = [buckets[g] for g in req]
                    self.assertLess(len({id(r) for r in unsafe}), len(req))

    def test_bulk_read_oracle(self):
        render = runpy.run_path(str(ROOT / 'evals/fixtures/crit-09/render.py'))['render']
        for n in [0, 1, 100, 101, 501]:
            ids = [i % 240 for i in range(n)]
            data = {i: [str(i), 'second'] for i in ids if i % 3}
            class Snapshot:
                def __init__(self):
                    self.reads = 0

                def items(self, key):
                    self.reads += 1
                    return data.get(key, []).copy()

                def items_many(self, keys):
                    self.reads += 1
                    if not 1 <= len(keys) <= 100:
                        raise AssertionError('invalid batch size')
                    return [(k, v) for k in keys for v in data.get(k, [])]

            with self.subTest(n=n):
                db = Snapshot()
                expected = render(db, ids)
                self.assertEqual(db.reads, n)
                db = Snapshot()
                keys = list(dict.fromkeys(ids))
                grouped = {k: [] for k in keys}
                for start in range(0, len(keys), 100):
                    for k, v in db.items_many(keys[start:start+100]):
                        grouped[k].append(v)
                actual = [grouped[k].copy() for k in ids]
                self.assertEqual(db.reads, (len(keys) + 99) // 100)
                self.assertEqual(expected, actual)
                self.assertEqual(len({id(r) for r in actual}), n)


if __name__ == '__main__':
    unittest.main()
