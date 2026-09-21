---
id: pass-02-correctness
name: Correctness
triggers:
  - always
depends_on: [pass-01-assumptions]
---

## Pass 2 — Correctness

Attack:

* invalid states
* missing invariants
* race conditions
* lost updates
* duplicate processing
* ordering assumptions
* incorrect transaction boundaries
* TOCTOU bugs
* partial writes
* inconsistent reads
* stale state
* retry behavior
* non-idempotent operations
* unsafe state transitions
* integer/float mistakes
* timezone problems
* truncation
* overflow
* pagination correctness
* deletion semantics
* mutable historical records

Ask:

> Can the system represent a state that should be impossible?

If yes, explain how it gets there.

Note: race conditions, lost updates, and duplicate processing identified here are analyzed in depth by Pass 4 (Concurrency). Do not report the same defect twice — report it once, in the pass that explains it best.
