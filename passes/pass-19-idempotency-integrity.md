---
id: pass-19-idempotency-integrity
name: Idempotency & State Integrity
triggers:
  - the code performs writes, mutations, external API calls, or database operations
depends_on: [pass-03-failure-semantics]
---

## Pass 19 — Idempotency & State Integrity

Attack the safety of mutations.

**Retry safety**

* side effects that duplicate on retry (charge, send, create) with no idempotency key, dedupe window, or natural idempotency
* partial mutation then retry: does the second attempt double-apply or corrupt?
* retry loops that treat permanent errors as transient and vice versa

**Transactional integrity**

* compound mutations spanning multiple stores with no transaction, outbox, or compensating action
* decisions computed from reads outside the transaction that guards the write (write skew)
* deterministic execution: clock reads, randomness, or unordered iteration affecting persisted results

**State integrity**

* state machines whose illegal transitions are representable in code
* in-memory state (caches, singletons, process locals) treated as source of truth across requests
* mutation-order dependencies hidden in the call graph

Ask:

> Execute this operation twice, concurrently, in both orders, and once after a crash midway — what state results?

If any answer is a corrupted or duplicated state, the mutation is not safe.

Dedupe: what happens *when* failure occurs belongs to Pass 3; this pass owns whether retries, duplication, and partial failure corrupt state.
