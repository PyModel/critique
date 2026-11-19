---
id: pass-09-performance
name: Performance
triggers:
  - latency, throughput, hot path, cost, or responsiveness requirements exist or are implied
  - the submission is source code
phase: attack
---

## Pass 9 — Performance

Performance is a measurable property. Inspect the actual critical path and search first for work that can be **eliminated**, not accelerated.

Optimization order — do not skip ahead:

1. eliminate work → 2. reduce work → 3. batch → 4. move off the critical path → 5. better algorithm → 6. better data structure → 7. locality → 8. parallelize where it pays → 9. low-level tuning

Identify:

* redundant computation, queries, network hops, API calls, model or tool calls
* repeated parsing, validation, serialization, or authentication work
* unnecessary copies, intermediate representations, JSON round trips
* avoidable allocations; blocking I/O; lock contention; excess process or network boundaries
* over-fetching; large payloads or bundles; excessive hydration; cold starts
* missing batching, streaming, caching — and incorrect caching
* logging on hot paths; synchronous work that should not block the request

For source code, additionally:

* accidental O(n²) and nested scans of the same collection
* allocations and string concatenation in loops; large structures copied per iteration
* N+1 patterns; filters with no usable index; columns fetched and never read

**Evidence discipline.** Locate the limiting resource in a representative baseline (profile, query plan, or deterministic work count). Compare doing nothing with the smallest candidate using paired runs, same inputs/environment, enough repetitions to show variance. Check warm/cold, skew, concurrency or tail latency only where they change the decision. Report the relevant time, peak memory, calls or cost, the denominator and the break-even point. Count output materialization and index/build overhead. A work-count reduction is not a wall-time speedup. Without measurements, state the experiment and decision threshold; do not invent seconds, speedup ratios or an SLO.

Before recommending a faster path, check result equivalence: ordering, duplicates, missing values, ownership/aliasing, tenant visibility, durability and failure behavior as applicable. Include a counterexample that would reject a faster but incorrect candidate.

For source code, every performance fix states its complexity delta, time and space (e.g. `O(n²) → O(n log n)`).

Dedupe: growth ceilings belong to Pass 8; bounds and backpressure to Pass 23.
