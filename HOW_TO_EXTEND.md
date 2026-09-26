# How to Extend This Skill

Two extension seams: **a pass is a file**, and **a pack is a file plus one Routing Table row**. `scripts/check.py` verifies the wiring; run it after every change.

## Anatomy of a pass

```markdown
---
id: pass-NN-compliance
name: Compliance
triggers:
  - regulated data (PII, payments, health) is mentioned or implied
  - audit, retention, or residency requirements appear in the submission
phase: attack
---

## Pass NN — Compliance

Attack list: specific, evidence-checkable items, not vibes.

Closing question the pass must answer.

Dedupe: which neighbouring pass owns overlapping defects.
```

`NN` is the next free number — check `passes/` for the highest. Never reuse or renumber a live id.

Field semantics:

- **`id`** — equals the filename without `.md`.
- **`triggers`** — checkable conditions about the artifact. The kernel rule: *a pass runs iff it is a member of a selected pack and its triggers match.* `always` runs on every review.
- **`phase`** — `frame` (reconstruct the problem before attacking: 01, 21), `attack` (default), or `synthesize` (judges the others' output: 16). Execution order is phase, then number. There is no per-pass ordering beyond that — if a pass truly needs another's output, it belongs in a later phase.

## Registering a pass

1. Create `passes/pass-NN-name.md`.
2. Add `NN name` to every pack it belongs to, including `packs/full.md`.
3. Run `python3 scripts/check.py`.

No kernel edit. If the pass introduces a new output concern, add a row to the Output table in `SKILL.md`; otherwise its findings use the standard Finding Format.

## Creating a pack

1. Copy `packs/api.md`; list member passes by `NN name`.
2. Add one row to the Routing Table in `SKILL.md`.
3. Run `python3 scripts/check.py`.

Packs reference passes, never other packs.

## Rules every extension obeys

1. No invented defects — an item that matches nothing in the artifact is skipped silently (Hard Rule 1).
2. One owner per defect — state in a Dedupe line which pass reports overlaps.
3. Fixes follow the kernel's Fix Validation unchanged; passes never define their own validation or evidence labels.

## Worked example

`passes/pass-24-agent-systems.md` + `packs/agent.md` (v0.7.0) were added through exactly these seams: one pass file, one pack file, one Routing Table row.

Verify registration: run a critique on a matching artifact and confirm Coverage lists the new pass as run.
