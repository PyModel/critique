#!/usr/bin/env python3
"""Wiring check for the critique skill. Exits non-zero on any violation.

Invariants (each failure message names the one it breaks):
  passes  - frontmatter present; id == filename stem; name present; phase valid;
            triggers list present; heading '## Pass N — ...'; unique numbers
  packs   - every entry 'NN slug' names an existing pass and slug == filename slug;
            every `always` pass is in every pack; every pass is in >= 1 specialized pack;
            full lists every pass
  routing - every pack has a Routing Table row and every row has a pack
  kernel  - description double-quoted and <= 1024 chars; name lowercase-hyphenated;
            metadata.version == first CHANGELOG heading
  docs    - no stale terms; every 'Pass N' / 'Passes N, M–K' and 'Hard Rule N' reference resolves
  evals   - every case in evals/cases.csv has exactly one rubric section and a fixture directory
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PHASES = {"frame", "attack", "synthesize"}
STALE = ["depends_on", "on_gate", "on_scope", "VALIDATION_UNAVAILABLE", "UNVERIFIED RISK",
         "Bulletproof", "Fake Design", "Final Challenge", "Fake-Safety"]
NUM_LIST = r"\s*\(?\s*(\d{1,2}(?:(?:,\s*|\s+and\s+|\s*[–-]\s*|/)\d{1,2})*)"
PASS_REF = re.compile(r"(?i)\bpass(?:es)?" + NUM_LIST)
RULE_REF = re.compile(r"(?i)\bhard rules?" + NUM_LIST)
NUM_OR_RANGE = re.compile(r"(\d{1,2})(?:\s*[–-]\s*(\d{1,2}))?")


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return m.group(1) if m else None


def referenced(pattern, text):
    for group in pattern.findall(text):
        for a, b in NUM_OR_RANGE.findall(group):
            yield from range(int(a), int(b or a) + 1)


def main():
    errors = []
    err = errors.append

    passes, slugs, always = {}, {}, set()
    for f in sorted((ROOT / "passes").glob("pass-*.md")):
        text = f.read_text()
        fm = frontmatter(text)
        if fm is None:
            err(f"{f.name}: no frontmatter")
            continue
        num, slug = f.name[5:7], f.stem[8:]
        pid = re.search(r"^id: (\S+)$", fm, re.M)
        phase = re.search(r"^phase: (\S+)$", fm, re.M)
        triggers = re.search(r"^triggers:\n((?:  - .+\n?)+)", fm, re.M)
        if not pid or pid.group(1) != f.stem:
            err(f"{f.name}: id must equal filename stem")
        if not re.search(r"^name: \S", fm, re.M):
            err(f"{f.name}: name missing")
        if not phase or phase.group(1) not in PHASES:
            err(f"{f.name}: phase must be one of {sorted(PHASES)}")
        if not triggers:
            err(f"{f.name}: triggers list missing")
        elif re.search(r"^  - always$", triggers.group(1), re.M):
            always.add(num)
        if not re.search(rf"^## Pass {int(num)} — ", text, re.M):
            err(f"{f.name}: heading must be '## Pass {int(num)} — ...'")
        if num in passes:
            err(f"{f.name}: duplicate pass number {num}")
        passes[num], slugs[num] = f, slug

    skill = (ROOT / "SKILL.md").read_text()
    fm = frontmatter(skill) or ""
    desc = re.search(r'^description: "(.*)"$', fm, re.M)
    if not desc:
        err("SKILL.md: description missing or not double-quoted")
    elif len(desc.group(1)) > 1024:
        err(f"SKILL.md: description {len(desc.group(1))} chars > 1024")
    if not re.search(r"^name: [a-z0-9]+(-[a-z0-9]+)*$", fm, re.M):
        err("SKILL.md: name must be lowercase-hyphenated")
    version = re.search(r'^  version: "(\d+\.\d+\.\d+)"$', fm, re.M)
    changelog = re.search(r"^## (\d+\.\d+\.\d+)$", (ROOT / "CHANGELOG.md").read_text(), re.M)
    if not version:
        err("SKILL.md: metadata.version missing or not quoted semver")
    elif not changelog or changelog.group(1) != version.group(1):
        err(f"SKILL.md version {version.group(1)} != CHANGELOG head {changelog and changelog.group(1)}")

    routed = set(re.findall(r"`packs/([a-z-]+)\.md`", skill))
    packs = {p.stem: p for p in (ROOT / "packs").glob("*.md")}
    for name in routed - packs.keys():
        err(f"SKILL.md routes to missing pack {name}")
    for name in packs.keys() - routed:
        err(f"packs/{name}.md is not in the Routing Table")

    covered = set()
    for name, p in sorted(packs.items()):
        m = re.search(r"^## Passes\n\n(.+)$", p.read_text(), re.M)
        if not m:
            err(f"packs/{name}.md: '## Passes' line missing")
            continue
        members = set()
        for entry in m.group(1).split("·"):
            parts = entry.split()
            n = parts[0] if parts else ""
            if not re.fullmatch(r"\d{2}", n) or n not in passes:
                err(f"packs/{name}.md: entry '{entry.strip()}' names no existing pass")
                continue
            members.add(n)
            if name != "full" and parts[1:] != [slugs[n]]:
                err(f"packs/{name}.md: entry '{entry.strip()}' must read '{n} {slugs[n]}'")
        for n in always - members:
            err(f"packs/{name}.md: always-trigger pass {n} missing")
        if name == "full":
            if members != set(passes):
                err(f"packs/full.md must list every pass; missing {sorted(set(passes) - members)}")
        else:
            covered |= members
    for n in sorted(set(passes) - covered):
        err(f"pass {n} belongs to no specialized pack (only full)")

    hard_rules = skill.split("\n# Hard Rules\n", 1)[-1].split("\n# ", 1)[0]
    rule_count = len(re.findall(r"^\d+\. \*\*", hard_rules, re.M))

    docs = [ROOT / "SKILL.md", ROOT / "HOW_TO_EXTEND.md", *(ROOT / "passes").glob("*.md"), *packs.values()]
    for d in docs:
        text = d.read_text()
        for term in STALE:
            if term in text:
                err(f"{d.relative_to(ROOT)}: stale term '{term}'")
        for n in sorted(set(referenced(PASS_REF, text)) - {int(k) for k in passes}):
            err(f"{d.relative_to(ROOT)}: references missing Pass {n}")
        for n in sorted(n for n in set(referenced(RULE_REF, text)) if not 1 <= n <= rule_count):
            err(f"{d.relative_to(ROOT)}: references missing Hard Rule {n}")

    evals = ROOT / "evals"
    case_file, rubric_file = evals / "cases.csv", evals / "behavior-rubric.md"
    for f in (case_file, rubric_file):
        if not f.is_file():
            err(f"{f.relative_to(ROOT)}: missing")
    cases = re.findall(r"^([a-z]+-\d+),", case_file.read_text(), re.M) if case_file.is_file() else []
    rubric = re.findall(r"^## ([a-z]+-\d+)$", rubric_file.read_text(), re.M) if rubric_file.is_file() else []
    if sorted(cases) != sorted(rubric) or len(set(cases)) != len(cases):
        err(f"evals: cases.csv ids {sorted(cases)} != rubric sections {sorted(rubric)}")
    for case in cases:
        if not (evals / "fixtures" / case).is_dir():
            err(f"evals/fixtures/{case}: fixture directory missing")

    for e in errors:
        print(f"FAIL {e}")
    print(f"{len(passes)} passes, {len(packs)} packs, {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
