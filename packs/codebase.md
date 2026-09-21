# Pack: codebase

Whole-codebase audits: ruthless senior review of a repository or module tree to raise performance, correctness, and maintainability.

## Passes (in run order)

1. `passes/pass-01-assumptions.md`
2. `passes/pass-21-codebase-survey.md` — survey + stratification governs everything below
3. `passes/pass-02-correctness.md`, `passes/pass-03-failure-semantics.md` — Tier A paths
4. `passes/pass-17-code-architecture.md`, `passes/pass-20-execution-order.md`, `passes/pass-19-idempotency-integrity.md`, `passes/pass-18-thread-safety.md` — Tier A files
5. `passes/pass-09-performance.md` — hot paths, always
6. `passes/pass-14-maintainability.md`, `passes/pass-16-simplicity.md` — Tier C structure
7. `passes/pass-15-dependency-risk.md` — external dependencies
8. `passes/pass-13-testing.md` — tests required by the findings

Add when applicable:

- `passes/pass-05-security.md` — any trust boundary exists
- `passes/pass-06-data-model.md` — persistence code
- `passes/pass-08-scalability.md` — explicit scale claims
- `passes/pass-11-operations.md`, `passes/pass-12-observability.md` — in-production codebases

## Notes

- Output: Full-tier structure **plus the Coverage Ledger** from Pass 21 (what ran at which tier, what was not reviewed).
- Improvement mandate: end with the top leverage moves ranked by impact / engineering cost — failure classes eliminated, complexity deleted, measurable performance gains.
- Never propose a whole-codebase big-bang refactor. Sequence changes by dependency and risk (kernel Hard Rule 5 scope honesty).
- Measure before optimizing: every performance claim names its metric (Pass 9 rule); a codebase review without numbers is a vibe.
- A small repo (fits in a few screens of file list) may use Triage + Coverage Ledger instead of Full.
