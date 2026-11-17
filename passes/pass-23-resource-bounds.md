---
id: pass-23-resource-bounds
name: Resource Bounds & Backpressure
triggers:
  - the artifact accepts external load, spawns work, holds connections, buffers data, calls models, or runs long-lived processes
phase: attack
---

## Pass 23 — Resource Bounds & Backpressure

Every resource that can grow must be bounded.

Check: memory · queues · threads, tasks, goroutines · connections, sockets, file descriptors · database pool · caches · logs and temp files · retries · recursion depth · request and response size · batch size · worker count · concurrency limits · context size and model tokens · spend per request.

For each, answer:

* What is the upper bound, and where is it enforced?
* What happens when it is reached — reject, shed, queue, block, crash?
* What backpressure propagates to the producer?
* Who gets rejected first, and do they learn why (status, retry-after)?
* How does the system recover after overload — or does it stay degraded (retry storms, reconnect storms, metastable failure)?

A **policy limit** (abuse, spend, safety, quota) and **overload** (no capacity now) are different outcomes even when both answer 429. A policy limit is enforced atomically across every process that claims to share it and stays closed when its store fails. Overload sheds — stale work first: bound the age of the oldest queued item, not only the depth.

An unbounded resource on a path reachable by untrusted input is a denial-of-service finding (Pass 5 severity applies). An unbounded resource elsewhere is an availability finding.

Dedupe: this pass owns bounds and overload behavior; Pass 8 owns growth ceilings; Pass 18 owns task lifecycle leaks in code.
