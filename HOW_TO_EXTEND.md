# How to Extend This Skill

The skill has one extension seam: **a pass is a file**. The kernel (`SKILL.md`) never needs editing to add review coverage.

## Anatomy of a pass

Every file in `passes/` follows this contract:

```markdown
---
id: pass-NN-compliance
name: Compliance
triggers:
  - regulated data (PII, payments, health) is mentioned or implied
  - audit, retention, or residency requirements appear in the submission
depends_on: [pass-06-data-model]
---

## Pass NN — Compliance

Attack list (specific, evidence-checkable items — not vibes).

Closing question the pass must answer.
```

(`NN` is the next free number — check `passes/` for the current highest. Never reuse a live id.)

Field semantics:

- **`id`** — unique, stable, kebab-case, prefixed `pass-NN-`.
- **`triggers`** — conditions under which the pass is applicable. The kernel's rule: *a pass is applicable iff its triggers match the submission.* Write them as checkable phrases about the artifact, not about mood. Use `always` for passes that run on every review (currently: assumptions, correctness, failure semantics, testing, simplicity).
- **`depends_on`** — pass ids that should run first, so the pass can build on their findings.

## Registration: drop the file, add one line

1. Create `passes/pass-NN-name.md` with the frontmatter above.
2. Add it to any `packs/*.md` run order where it belongs (or create a new pack — see below).

That is the entire registration. The kernel's Routing Table and Lifecycle pick it up; no other file changes. If the pass introduces a genuinely new output concern, add it to the Full-tier output structure in the kernel — otherwise render findings through the standard Finding Format and it needs nothing.

## Hooks

Two named points in the lifecycle accept extension behavior:

- **`on_scope`** — a pack's Notes section may add conditional passes ("joins when the flow writes data").
- **`on_gate`** — a pass may declare extra Bulletproof Gate evidence requirements; state them in a `## Gate additions` section of the pass file.

## Creating a domain pack

A pack is a run-ordered list of pass files plus Notes. Copy `packs/api.md` as a template. Keep packs composable: a pack references passes, never other packs.

## Rules every extension must obey

1. No invented defects: a checklist item that matches nothing in the artifact is skipped silently (kernel Hard Rule 1 — global, applies to your pass too).
2. If your pass finds a defect another pass will also find, say which pass reports it; never double-report.
3. Fixes your pass produces follow the kernel's Fix Validation Protocol unchanged — do not add your own validation rules.

## Worked example

Adding accessibility coverage:

1. `passes/pass-NN-accessibility.md` — triggers: "a user-facing interface is under review"; depends_on: `pass-10-ux`.
2. Add to `packs/ux.md` run order after Pass 10.
3. Done — the next UX review attacks contrast ratios, focus order, screen-reader semantics, and touch targets without any kernel edit.

To verify registration: run a critique on a UI submission and confirm the Executive Assessment's coverage disclosure lists the new pass.

For real worked examples, read `passes/pass-19-idempotency-integrity.md` with `packs/code.md` (v0.5.0) and `passes/pass-21-codebase-survey.md` with `packs/codebase.md` (v0.6.0) — both added through exactly this seam.
