---
id: pass-04-concurrency
name: Concurrency
triggers:
  - multiple writers, workers, tabs, jobs, queues, webhooks, or duplicated requests appear in the submission or are implied by its scale claims
depends_on: [pass-02-correctness]
---

## Pass 4 — Concurrency

Look for:

* check-then-write
* double submission
* duplicate workers
* simultaneous updates
* stale optimistic state
* non-atomic counters
* inventory oversell
* double payments
* duplicate emails
* duplicated jobs
* conflicting state transitions
* multiple browser tabs
* webhook/request races

Require explicit answers for:

* locking
* uniqueness
* compare-and-swap
* transaction isolation
* idempotency keys
* conflict resolution

where relevant.

Note: report a concurrency defect once — either here or in Pass 2, never in both.
