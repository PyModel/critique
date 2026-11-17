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

**Keep the axes apart.** One event can be overloaded, partly committed, and unsafe to retry at once. For each failure a caller must handle, three things stay distinguishable: the result it observes (absence, invalid, denied, conflict, degraded, cancelled, failed), the effect certainty (not started, committed, unknown, partial), and whether this caller may repeat it. Attack:

* several outcomes collapsed into one value — `null`, `false`, an empty list, or a bare 500 standing for "none", "denied", and "failed"
* a default, empty result, or fallback value returned in place of a failure the contract never named
* a timeout or dropped connection treated as "did not happen" — repeated blindly or under a fresh idempotency key instead of resolved by status lookup, same-key replay, or reconciliation
* partial success reported as plain success or plain failure, or stored and later read as complete
* a trusted caller's broken precondition handled like bad input (retried, defaulted) — or hostile input handled like a bug (assertion, crash)
* authorization, tenancy, or a spend or abuse limit that turns permissive when its check or its store fails
* a fallback that drops a constraint the primary path enforces, serves stale data unbounded and unlabeled, or cannot absorb the load redirected to it
* recovery that adds load to the system it recovers — retry storms, cache rebuilds, backlog drains with no bound
* a deadline each layer restarts instead of passing down what remains; cancellation assumed to undo a committed effect

**Retries are never a fix on their own.** Any retry must define: its single owner in the call chain (SDK × wrapper × service × worker multiply), idempotency, retry budget, backoff with jitter, deadline propagation, cancellation, and amplification risk under overload.

Expose failure handling that amounts to "retry", "log an error", "return 500", "eventually reconcile", or "manual cleanup" without defined semantics.

Prefer protocols that remove the ambiguity (idempotency keys, outbox, fencing tokens, single owner) over coordination that manages it.
