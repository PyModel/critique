---
id: pass-08-scalability
name: Scalability
triggers:
  - growth, traffic, user counts, or large data volumes are claimed or implied
depends_on: [pass-06-data-model]
---

## Pass 8 — Scalability

Do not merely ask whether something is `O(n)`.

Determine what grows with:

* users
* tenants
* requests
* connections
* records
* events
* workers
* uploaded files
* context size
* history
* cache cardinality

Look for:

* unbounded scans
* offset pagination
* N+1 queries
* fan-out amplification
* global locks
* huge transactions
* synchronous external calls
* memory proportional to total state
* unlimited queues
* hotspot keys
* high-cardinality metrics
* uncontrolled retry storms

Distinguish:

**Current bottleneck** from **future scalability risk**.

Do not invent scale requirements.
