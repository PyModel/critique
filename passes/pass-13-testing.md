---
id: pass-13-testing
name: Testing
triggers:
  - always
phase: attack
---

## Pass 13 — Testing

Tests passing proves only what they assert. Ask what they fail to test.

Attack existing suites for:

* tests coupled to implementation, or that only exercise mocks
* assertions that cannot fail; happy-path-only coverage
* shared state between tests; sleeps and timing luck where a fake clock, seeded randomness, or a barrier belongs
* tests asserting the historical bug shape, or rewritten to match a refactor instead of intended behavior
* disabled or skipped tests — each goes to the Workaround Ledger
* no test ever crossing a real boundary (database, queue, network)
* benchmarks on unrepresentative workloads

For each critical finding, state the test that proves the fix — choosing from:

* **Unit** — pure domain invariants
* **Property-based / fuzz** — invariants over generated or hostile input
* **Integration** — real database, queue, cache, filesystem, external boundary
* **Contract / compatibility** — API schemas across versions
* **Concurrency** — deterministic interleavings of conflicting operations
* **Failure injection** — timeouts, crashes mid-operation, duplicate delivery, slow dependencies
* **Migration / rollback** — forward, compatibility window, rollback
* **Security** — authorization boundaries, abuse cases
* **Load / stress / soak** — critical path under representative and overload workload
* **Mutation testing** — where suite strength itself is in doubt

Every discovered bug gets a regression test reproducing its actual mechanism, shown failing on the unfixed code first; a test that passes on both sides proves nothing.

(This pass defines **what to prove**. Remediation plans **when**; the Production Gate checks **whether it was proven**. Do not restate the list in all three.)
