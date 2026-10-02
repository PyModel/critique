# Pack: agent

LLM, agent, tool-using, retrieval, and prompt-driven systems.

Membership only. A listed pass runs iff its triggers match; order is fixed by the kernel (phase, then number).

## Passes

01 assumptions · 02 correctness · 03 failure-semantics · 04 concurrency · 05 security · 06 data-model · 07 api-contract · 09 performance · 10 ux · 11 operations · 12 observability · 13 testing · 14 maintainability · 15 dependency-risk · 16 simplicity · 22 state-invariants · 23 resource-bounds · 24 agent-systems · 25 tech-debt

## Notes

- Pass 24 is the spine. Tool schemas are API contracts (Pass 7); tool side effects need Pass 3 idempotency analysis.
- Performance here includes model and token cost: count calls per task and name the ones that can be deleted.
- Agent submitted as source code → also route to `code`.
