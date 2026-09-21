---
id: pass-09-performance
name: Performance
triggers:
  - latency, throughput, hot path, or responsiveness requirements exist or are implied
depends_on: [pass-08-scalability]
---

## Pass 9 — Performance

Inspect the actual critical path.

Identify:

* unnecessary serialization
* redundant network hops
* excessive parsing
* duplicate queries
* repeated authentication work
* avoidable allocations
* excessive hydration
* large bundles
* blocking I/O
* cold-start penalties
* cache-unfriendly access
* over-fetching
* under-indexing

Demand measurement before speculative optimization.

Specify the metric needed when evidence is missing.
