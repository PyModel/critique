---
id: pass-03-failure-semantics
name: Failure Semantics
triggers:
  - always
depends_on: [pass-02-correctness]
---

## Pass 3 — Failure Semantics

For every important operation determine what happens when failure occurs:

* before execution
* midway through execution
* after execution but before acknowledgement
* during retry
* during rollback
* while a downstream dependency is unavailable
* after process restart

Expose designs whose failure handling amounts to:

* "retry"
* "log an error"
* "return 500"
* "eventually reconcile"
* manual cleanup

without defining semantics.
