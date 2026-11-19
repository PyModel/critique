# Pack: codebase

Whole repository or module tree: audit and level up correctness, performance, and maintainability.

Membership only. A listed pass runs iff its triggers match; order is fixed by the kernel (phase, then number).

## Passes

01 assumptions · 21 codebase-survey · 02 correctness · 03 failure-semantics · 04 concurrency · 05 security · 06 data-model · 07 api-contract · 08 scalability · 09 performance · 10 ux · 11 operations · 12 observability · 13 testing · 14 maintainability · 15 dependency-risk · 16 simplicity · 17 code-architecture · 18 thread-safety · 19 idempotency-integrity · 20 execution-order · 22 state-invariants · 23 resource-bounds · 24 agent-systems · 25 tech-debt

## Notes

- Pass 21 owns stratification: Tier A at full rigor, Tier B pattern-sampled, Tier C structural. Explicit deep/all/exhaustive requests use its inventory mode; the reconciled manifest goes in Coverage.
- Never propose a big-bang rewrite. Sequence by dependency and risk; one coherent end state per remediation step.
- Measure before optimizing: every performance claim names its metric.
- A small repo may use Triage only under the kernel's tier rules; an explicit deep review is not a quick look.
