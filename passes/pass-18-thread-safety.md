---
id: pass-18-thread-safety
name: Concurrency & Thread Safety (code)
triggers:
  - the code shares state across threads, tasks, goroutines, or requests; uses locks, atomics, channels, or async/await; or spawns background work
depends_on: [pass-02-correctness]
---

## Pass 18 — Concurrency & Thread Safety (code level)

Attack mechanism-level concurrency defects.

**Shared mutable state**

* fields or collections written by concurrent paths without synchronization
* check-then-act sequences on shared state (TOCTOU)
* lazy initialization without a safe publication mechanism
* visibility and reordering assumptions the language's memory model does not guarantee

**Locking**

* lock ordering that can deadlock (two locks acquired in opposite order on different paths)
* locks held across I/O, network calls, or awaited operations
* coarse global locks serializing independent operations
* missing release of locks/sessions/connections on error paths

**Async task lifecycle**

* fire-and-forget: unawaited futures/promises, detached goroutines, un-Joined threads
* missing cancellation propagation; background work that outlives its scope
* errors swallowed in background paths (no await, no error channel, no deferred recover)
* unbounded task spawning vs bounded pools/queues; missing backpressure

**Non-blocking, resource-safe execution**

* blocking calls on non-blocking threads (event loop, scheduler thread, renderer)
* busy-wait loops instead of condition variables/channels/await
* per-language leaks: goroutine leaks, pending asyncio tasks, undisposed resources

Map every mechanism to the submission language's idioms — do not demand patterns the language forbids, and do not excuse defects the language's own model makes impossible to commit safely.

Dedupe: business-scenario duplicates (double submit, oversell, duplicate emails) belong to Pass 4; this pass owns the mechanism that permits them.
