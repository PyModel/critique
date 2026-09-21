---
id: pass-09-performance
name: Performance
triggers:
  - latency, throughput, hot path, or responsiveness requirements exist or are implied
  - the submission is source code
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

For source code, additionally:

* algorithmic complexity in hot paths: nested iteration over the same collection, accidental O(n²)
* allocations inside loops; string concatenation in loops; large structures copied per iteration
* N+1 query patterns; queries whose filters have no usable index
* redundant I/O: repeated round trips, missing batching, fetching columns that are never read
* serialization/deserialization on hot paths where cheaper transfer exists

Demand measurement before speculative optimization.

Specify the metric needed when evidence is missing.

For source code, every performance finding states the complexity change its fix delivers — time and space (e.g., `O(n²) → O(n log n)`, `O(n) → O(1)` extra space).
