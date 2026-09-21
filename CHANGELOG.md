# Changelog

All notable changes to the `critique` skill. Format: semver; breaking changes bump the minor until 1.0.

## 0.4.0

Restructured from a single monolithic prompt into kernel + passes + packs.

### Added

- Input Contract (artifact, stage, constraints, scope) with `NO_ARTIFACT` / `SCOPE_EXCEEDED` degradation labels.
- Definition of Done, promoted to the kernel top; the review's termination condition.
- Review Lifecycle with an explicit Routing Table and per-pass trigger contracts (`passes/*.md` frontmatter).
- Domain packs: `packs/system.md`, `packs/api.md`, `packs/ux.md`.
- Failure semantics in the Fix Validation Protocol: bounded attempts (1 retry per source, max 3 per unique tool+library+version), fallback down routing order, cross-finding dedupe, attempt-counts instead of wall-clock backoff, never-block rule.
- `VALIDATION_UNAVAILABLE` label for exhausted validation.
- Self-Gate run before every review output.
- Depth tiers (Triage / Full) and output compression rules.
- Severity calibration anchor (P1 vs P3 example).
- Global anti-fabrication rule (was previously scoped to edge cases only).
- `HOW_TO_EXTEND.md` and this changelog.

### Changed

- Frontmatter description rewritten trigger-only (was 1,033 chars mixing triggers with hard rules; hard rules already live in the body).
- Testing requirements split by role: Pass 13 defines what to prove, Remediation plans when, the Gate checks whether — no shared wording to drift.
- Correctness/Concurrency overlap resolved: a concurrency defect is reported once, in the pass that explains it best.

### Migration from 0.3.0

Behavior-preserving: all 16 passes' attack lists moved verbatim into `passes/`. A full-skill invocation runs the same coverage as v0.3.0, plus explicit scope/tier disclosure.

## 0.3.0

Baseline as audited (single-file skill, 16 inline passes).

**UNVERIFIED — validate before implementation:** the Agent Skills frontmatter description length cap (believed 1,024 chars) against the current agentskills.io spec; the v0.4.0 description targets ≤1,000 chars with margin regardless.
