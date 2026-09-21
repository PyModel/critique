---
id: pass-11-operations
name: Operational Reality
triggers:
  - deployment, production operation, or environment configuration is mentioned or implied
depends_on: [pass-03-failure-semantics]
---

## Pass 11 — Operational Reality

Attack designs that assume deployment is perfect.

Inspect:

* configuration
* startup
* shutdown
* health checks
* migrations
* rollback
* backups
* restores
* secret rotation
* deployment ordering
* worker draining
* stuck jobs
* poison messages
* queue growth
* storage exhaustion
* certificate expiration
* clock skew
* dependency degradation

Require recovery procedures for critical state.
