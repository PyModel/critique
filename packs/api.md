# Pack: api

API, contract, protocol, SDK, and integration reviews.

Membership only. A listed pass runs iff its triggers match; order is fixed by the kernel (phase, then number).

## Passes

01 assumptions · 02 correctness · 03 failure-semantics · 04 concurrency · 05 security · 06 data-model · 07 api-contract · 08 scalability · 09 performance · 10 ux · 11 operations · 13 testing · 14 maintainability · 15 dependency-risk · 16 simplicity · 22 state-invariants · 23 resource-bounds · 25 tech-debt

## Notes

- Pass 7 is the spine; judge contract problems after Pass 6 has exposed schema problems (phase order guarantees this).
- Version skew is the dominant hazard: every change is checked old-client/new-server and new-client/old-server.
