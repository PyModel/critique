---
id: pass-03-failure-semantics
name: Failure Semantics
triggers:
  - always
phase: attack
---

## Pass 3 — Failure Semantics

For every important operation, determine persisted state, externally visible state, retry safety, recovery path, and invariant preservation when:

* it fails before, midway, or after execution but before acknowledgement
* the timeout fires before remote execution — and after it (remote committed, response lost)
* local succeeds and remote fails, or remote succeeds and local fails
* the process crashes between two consecutive side effects, then restarts
* a dependency is **slow** rather than down (100x latency, not an error)
* a retry, redelivery, or reordering occurs
* a deployment rolls mid-operation; old and new versions coexist; old client meets new server and vice versa
* disk fills, memory is exhausted, configuration is invalid
* two workers both believe they own the same work

**Retries are never a fix on their own.** Any retry must define: idempotency, retry budget, backoff with jitter, deadline propagation, cancellation, and amplification risk under overload.

Expose failure handling that amounts to "retry", "log an error", "return 500", "eventually reconcile", or "manual cleanup" without defined semantics.

Prefer protocols that remove the ambiguity (idempotency keys, outbox, fencing tokens, single owner) over coordination that manages it.
