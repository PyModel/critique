---
id: pass-15-dependency-risk
name: Dependency Risk
triggers:
  - external libraries, services, APIs, models, or third-party platforms are used or proposed
phase: attack
---

## Pass 15 — Dependency Risk

Treat every dependency as permanent operational cost until shown otherwise.

Examine:

* why it exists; what functionality is actually used
* maintenance status; ecosystem health; security history; transitive dependencies
* API stability; upgrade path; version pinning; supply-chain verification
* pinned and lock-filed with integrity verification; a dependency nobody on the team owns is an incident waiting for an owner
* outage and slowness behavior; rate limits; pricing sensitivity
* binary size; startup cost; runtime overhead
* licensing; platform support; data portability; lock-in and replacement difficulty

Do not add a dependency for what a few safe lines can do. Do not reimplement mature, security-sensitive infrastructure (crypto, auth protocols, parsers of hostile formats).

Do not classify a dependency as bad merely because it is external. Measure the coupling.
