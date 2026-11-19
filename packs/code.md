# Pack: code

Use for a source file, module, or snippet.

Membership only. A listed pass runs iff its triggers match; order is fixed by the kernel (phase, then number).

## Passes

01 assumptions · 02 correctness · 03 failure-semantics · 04 concurrency · 05 security · 06 data-model · 07 api-contract · 08 scalability · 09 performance · 10 ux · 11 operations · 12 observability · 13 testing · 14 maintainability · 15 dependency-risk · 16 simplicity · 17 code-architecture · 18 thread-safety · 19 idempotency-integrity · 20 execution-order · 22 state-invariants · 23 resource-bounds · 24 agent-systems · 25 tech-debt

## Notes

- Findings and enhancement backlog first. Replacement Implementation is an appendix only when requested.
- A file reviewed alone is still part of a system: follow its entry points and callers far enough to settle every absence claim (kernel Hard Rule 1).
