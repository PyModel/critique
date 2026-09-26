#!/usr/bin/env python3
"""Wiring check for the critique skill: passes, packs, routing, frontmatter, stale terms.

Run from anywhere: python3 scripts/check.py. Exits non-zero on any violation.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PHASES = {"frame", "attack", "synthesize"}
STALE = ["depends_on", "on_gate", "on_scope", "VALIDATION_UNAVAILABLE", "UNVERIFIED RISK",
         "Bulletproof", "Fake Design", "Final Challenge", "Fake-Safety"]


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return m.group(1) if m else None


def main():
    errors = []
    err = errors.append

    passes = {}
    for f in sorted((ROOT / "passes").glob("pass-*.md")):
        fm = frontmatter(f.read_text())
        if fm is None:
            err(f"{f.name}: no frontmatter")
            continue
        num = f.name[5:7]
        pid = re.search(r"^id: (\S+)$", fm, re.M)
        phase = re.search(r"^phase: (\S+)$", fm, re.M)
        if not pid or pid.group(1) != f.stem:
            err(f"{f.name}: id must equal filename stem")
        if not phase or phase.group(1) not in PHASES:
            err(f"{f.name}: phase must be one of {sorted(PHASES)}")
        if not re.search(r"^triggers:\n  - ", fm, re.M):
            err(f"{f.name}: triggers list missing")
        if not re.search(rf"^## Pass {int(num)} — ", f.read_text(), re.M):
            err(f"{f.name}: heading must be '## Pass {int(num)} — ...'")
        if num in passes:
            err(f"{f.name}: duplicate pass number {num}")
        passes[num] = f

    skill = (ROOT / "SKILL.md").read_text()
    fm = frontmatter(skill) or ""
    desc = re.search(r'^description: "(.*)"$', fm, re.M)
    if not desc:
        err("SKILL.md: description missing or not double-quoted")
    elif len(desc.group(1)) > 1024:
        err(f"SKILL.md: description {len(desc.group(1))} chars > 1024")
    if not re.search(r"^name: [a-z0-9]+(-[a-z0-9]+)*$", fm, re.M):
        err("SKILL.md: name must be lowercase-hyphenated")

    routed = set(re.findall(r"`packs/([a-z-]+)\.md`", skill))
    packs = {p.stem: p for p in (ROOT / "packs").glob("*.md")}
    for name in routed - packs.keys():
        err(f"SKILL.md routes to missing pack {name}")
    for name in packs.keys() - routed:
        err(f"packs/{name}.md is not in the Routing Table")

    for name, p in packs.items():
        m = re.search(r"^## Passes\n\n(.+)$", p.read_text(), re.M)
        if not m:
            err(f"packs/{name}.md: '## Passes' line missing")
            continue
        members = re.findall(r"\b(\d{2})\b", m.group(1))
        for n in members:
            if n not in passes:
                err(f"packs/{name}.md: pass {n} does not exist")
        if name == "full" and set(members) != set(passes):
            err(f"packs/full.md must list every pass; missing {sorted(set(passes) - set(members))}")

    docs = [ROOT / "SKILL.md", ROOT / "HOW_TO_EXTEND.md", *(ROOT / "passes").glob("*.md"), *packs.values()]
    for d in docs:
        text = d.read_text()
        for term in STALE:
            if term in text:
                err(f"{d.relative_to(ROOT)}: stale term '{term}'")
        for ref in re.findall(r"\bPass(?:es)? (\d{1,2})\b", text):
            if f"{int(ref):02d}" not in passes:
                err(f"{d.relative_to(ROOT)}: references missing Pass {ref}")

    for e in errors:
        print(f"FAIL {e}")
    print(f"{len(passes)} passes, {len(packs)} packs, {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
