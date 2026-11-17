---
id: pass-04-concurrency
name: Concurrency (scenarios)
triggers:
  - multiple writers, workers, tabs, jobs, queues, consumers, webhooks, or duplicated requests appear in the submission or are implied by its scale claims
phase: attack
---

## Pass 4 — Concurrency (business scenarios)

Look for:

* check-then-write; double submission; duplicate consumers or workers
* simultaneous updates; stale optimistic state; non-atomic counters
* inventory oversell; double payments; duplicate emails or jobs
* conflicting state transitions; multiple browser tabs
* webhook/request races; cancellation and shutdown races; stale writers after failover
* a process-local lock or in-memory dedupe guarding state other processes or replicas also write; a lease whose stale holder can still write because the resource checks no fencing token

For every shared mutable resource ask:

* Who owns it, and who may modify it?
* What synchronizes access?
* Can single ownership replace synchronization?
* Can immutable data replace shared mutation?
* Can moving the transaction boundary delete the race entirely?

Require explicit answers — locking, uniqueness constraints, compare-and-swap, isolation level, idempotency keys, fencing, conflict resolution — where relevant.

Dedupe: this pass owns the scenario; Pass 18 owns the code mechanism. Report each defect once.
