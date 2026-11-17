---
id: pass-16-simplicity
name: Simplicity & Abstraction Tax
triggers:
  - always
phase: synthesize
---

## Pass 16 — Simplicity & Abstraction Tax

Runs last: the other passes have mapped the real requirements; now judge which complexity survives them. Unnecessary complexity is a defect.

**Abstraction tax** — reject abstractions that:

* have one implementation and no substitution need; rename another abstraction
* forward arguments (service layers, repositories wrapping trivial queries, wrappers around wrappers)
* exist for speculative reuse; generic frameworks or plugin systems for one use case
* hide important behavior, spread one responsibility across layers, or blur ownership
* use an event bus where a direct call suffices; split into services with no independent operational boundary
* make configurable what nobody configures

Accept an abstraction only for real isolation, ownership, substitution, invariants, testability, or protocol boundaries. Ask: *what specific change becomes cheaper because this exists?*

**Requirement check** — every cache, queue, circuit breaker, replica, workflow engine, service split, shard, event log, or plugin system the artifact has or proposes names the requirement that demands it (kernel Hard Rule 6). None → deletion candidate; a plausible future need → Deferred with its trigger.

**Deletion hunt** — ask continuously:

* Can stronger ownership remove this lock? Stronger typing remove this validation?
* Can a database constraint remove this application logic? A transaction remove this reconciliation?
* Can one source of truth remove this synchronization?
* Can synchronous execution remove this queue — or a queue remove fragile synchronous coupling?
* Can one process remove a network boundary? Can precomputation remove repeated runtime work?
* Can deleting a feature remove an entire failure class?

Prefer the simplest architecture that preserves the required properties. Density is not simplicity: a clear 200-line function can beat ten 20-line ones threading state through each other.

Output: design-level instances go to the Abstraction Tax section; the net effect goes to Shape Change.
