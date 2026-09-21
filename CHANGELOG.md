# Changelog

All notable changes to the `critique` skill. Format: semver; breaking changes bump the minor until 1.0.

## 0.6.0

Whole-codebase mode, senior-mindset enforcement, and leverage-ranked output.

### Added

- `packs/codebase.md` — whole-codebase audit pack: survey, risk-stratified depth, coverage ledger, leverage-ranked improvements.
- `passes/pass-21-codebase-survey.md` — survey (entry points, data flow, hot paths, conventions), Tier A/B/C stratification, coverage ledger, codebase-specific attack surface (death-by-a-thousand-cuts, convention drift, config traps, repository rot).
- **Senior Engineering Mindset** (kernel) — seven enforced disciplines: mechanism before verdict, quantify or name the measurement, every fix states its cost, no cargo-cult, own the outcome, leverage over volume, reframe before reviewing.
- Routing Table row and Input Contract entry for codebase artifacts.
- Purpose now mandates leverage ranking: every review ends with the highest-leverage improvements ordered by impact / engineering cost.
- Self-Gate check 5: failure mechanism, fix cost, and leverage ranking verified before output.

### Changed

- Description advertises codebase audits and level-up triggers (816 → ~940 chars, trigger-only).
- `HOW_TO_EXTEND.md` examples use `pass-NN` placeholders — ends the recurring example-id collision class (examples collided with real passes 17 and 21 in consecutive releases).

## 0.5.0

Added a code review-and-refactor mode, registered through the v0.4.0 extension seam.

### Added

- `packs/code.md` — pack for exhaustive production-grade review and refactoring of source code.
- `passes/pass-17-code-architecture.md` — SOLID, separation of concerns, DRY-vs-YAGNI boundary at code level.
- `passes/pass-18-thread-safety.md` — mechanism-level concurrency: shared mutable state, lock ordering/deadlock, async task lifecycle, non-blocking resource-safe execution.
- `passes/pass-19-idempotency-integrity.md` — retry safety, transactional integrity, deterministic execution, state-machine integrity for mutations.
- `passes/pass-20-execution-order.md` — lifecycle ordering (validate → retrieve → logic → mutate → return) and fail-fast error handling.
- **Code tier** output in the kernel: Critical Audit → Refactored Implementation → Key Trade-offs, with behavior-preservation flags, language-idiom rule, complexity-delta requirement for performance findings, and validation of every added/changed library call.
- Routing Table row and depth-tier entry for code submissions; boundary kept sharp — routine diffs/PRs still belong to `code-review`.

### Changed

- `passes/pass-09-performance.md` — added code-level items (loop allocations, N+1, redundant I/O, algorithmic complexity) and a source-code trigger; performance findings on code must state time/space complexity deltas.
- Frontmatter description rewritten to advertise the code mode (743 → ~930 chars, still trigger-focused).
- `HOW_TO_EXTEND.md` example ids bumped pass-17 → pass-21 to free the 17–20 range occupied by real passes.

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
