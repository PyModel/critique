---
id: pass-15-dependency-risk
name: Dependency Risk
triggers:
  - external libraries, services, APIs, or third-party platforms are used or proposed
depends_on: [pass-08-scalability]
---

## Pass 15 — Dependency Risk

For external dependencies examine:

* why it exists
* what functionality is actually used
* replacement difficulty
* data portability
* API stability
* outage behavior
* lock-in
* pricing sensitivity
* rate limits
* security implications

Do not classify a dependency as bad merely because it is external.

Measure the coupling.
