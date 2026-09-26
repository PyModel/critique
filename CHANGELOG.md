# Changelog

All notable changes to the `critique` skill. Format: semver; breaking changes bump the minor until 1.0.

## 0.7.0

Generalized, hardened, and rebuilt on zero-tech-debt principles. Breaking: pass frontmatter, pack format, evidence labels, and output sections changed.

### Added

- **Zero-tech-debt core** — the current implementation is evidence, not authority; reviews design toward the end state, not its history. New **Shape Change** output (Deleted / Unified / Renamed / Left alone / Deferred / Net concepts) and Self-Gate check that concepts net down.
- **Workaround Ledger** — exhaustive workaround hunt (markers plus structural shapes: catch-and-continue, sleep/poll, reconciliation jobs, one-caller branches, manual runbook steps); every entry gets a root-cause replacement.
- **Enhancements** section — every material improvement found, ranked by impact / engineering cost, nothing dropped for length.
- **Replacement Implementation** on by default for code: runnable root-cause code for every P0–P2 finding and ledger entry, fixed at the shared point all callers route through; continues across responses instead of truncating.
- Passes: 22 State Model & Invariants, 23 Resource Bounds & Backpressure, 24 Agent & LLM Systems, 25 Tech Debt & Historical Leakage.
- Packs: `agent`, `full` (replaces the pack-less "all passes" route).
- **Degradation** table — defined fallback for missing inputs, context overflow, missing lookup tools, failed lookups, no execution, underdetermined fixes. The review never stalls.
- Reviewer Disciplines (was Senior Engineering Mindset): reframe + end state, root-cause grouping, delete-before-add; each checked by the Self-Gate.
- Priority order for breaking ties between fixes (correctness → simplicity → invariants → … → cost).
- CONTAINMENT and MIGRATION STEP labels: permitted interim states, each paired with a permanent fix and removal criterion (fixes the old rule forbidding containment of an in-production P0).
- `scripts/check.py` — wiring check (ids, phases, pack membership, routing, description cap, stale terms, dangling Pass references).
- Passes 01–07, 09, 11–16 enriched: first-principles reframe, timeout-before/after and slow-dependency failure cases, retry budgets, optimization ladder and benchmark discipline, property/fuzz/mutation testing, DX, dependency licensing and supply chain.

### Changed

- **One ordering authority:** `depends_on` removed; order is `phase` (frame → attack → synthesize) then pass number. The old pack orders contradicted `depends_on` (codebase pack ran 17 before 14 and 16 before 15/13).
- **One selection rule:** a pass runs iff it is in a selected pack and its triggers match. Packs are membership lists; "add when applicable" lists removed.
- Evidence labels: VERIFIED / INFERRED / ASSUMED / HYPOTHETICAL. Fix label: UNVALIDATED. Coverage label: NOT COVERED. Removes the UNVERIFIED collision between evidence and fix validation.
- Fix Validation is tool-agnostic (docs lookup → web search → page fetch, native tools allowed); budget is 3 attempts per claim total, one per source. Fixes the old retry-per-source vs ceiling contradiction and the dual UNVERIFIED / VALIDATION_UNAVAILABLE labels.
- One output spine across Triage / Full / Code; Coverage section in every tier (absorbs the codebase Coverage Ledger and SCOPE_EXCEEDED). Remediation ranked by impact / cost with explicit prerequisite marks. Finding Format gains **Fix cost**.
- Input Contract: missing stage/constraints/focus never blocks; inferred and labeled ASSUMED.
- Bulletproof Gate → Production Gate (adds Concurrency and Resources). Fake-Safety → False-Assurance Detector (adds async, tests-pass, microservices, prompt-as-access-control).
- Description rewritten (793 chars).
- Severity stays P0–P3 plus non-severity Opportunities (in Enhancements); the pasted BLOCKER…OPPORTUNITY scale was not adopted to avoid a second severity vocabulary.

### Removed

- `on_scope` / `on_gate` hooks (never wired into the kernel).
- Final Challenge (folded into the Self-Gate adversarial second pass).
- Hard Rule 3's inline attack list (Pass 16 owns it).

### Migration from 0.6.0

Custom passes: replace `depends_on:` with `phase:` and add the pass number to the relevant packs and `packs/full.md`. Custom packs: convert the run-order list to one `## Passes` line of `NN name` entries and add a Routing Table row. Run `python3 scripts/check.py`.

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

Description cap validated 2026-09-26 against agentskills.io/specification: max 1024 characters.
