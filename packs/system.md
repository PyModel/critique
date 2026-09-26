# Pack: system

Backend, service, infrastructure, and distributed-system reviews.

Membership only. A listed pass runs iff its triggers match; order is fixed by the kernel (phase, then number).

## Passes

01 assumptions · 02 correctness · 03 failure-semantics · 04 concurrency · 05 security · 06 data-model · 07 api-contract · 08 scalability · 09 performance · 10 ux · 11 operations · 12 observability · 13 testing · 14 maintainability · 15 dependency-risk · 16 simplicity · 22 state-invariants · 23 resource-bounds · 24 agent-systems · 25 tech-debt

## Notes

- Highest yield: 03, 04, 06, 22, 23. Never drop them under budget pressure.
- 11 and 12 are mandatory when stage is pre-production or in-production.
- Distributed boundaries: attack every network hop with Pass 3's timeout-before/after and slow-dependency cases before accepting it.
