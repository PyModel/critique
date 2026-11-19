---
id: pass-11-operations
name: Operational Reality
triggers:
  - deployment, production operation, or environment configuration is mentioned or implied
phase: attack
---

## Pass 11 — Operational Reality

Imagine operating this at 3am. Attack designs that assume deployment is perfect.

Inspect:

* startup, shutdown, restart; worker draining; graceful cancellation
* configuration validated before serving traffic; secret and certificate rotation
* deployment ordering; rolling deploys with mixed versions; rollback safety
* schema migrations interleaved with deploys
* health checks that reflect real readiness
* stuck jobs; poison messages; queue growth; storage exhaustion
* backups, restores, disaster and regional recovery — compare a timed drill against tolerated data loss (RPO) and time to restore service (RTO). Include dependencies, stale writers after failover, and the checks before reads/writes resume; a backup is not a verified recovery
* when pipelines/IaC are in scope, trace reviewed source → built artifact → promotion → running config and rollback. Identify who can change each link and what the release identity can touch. Compare desired and deployed config from supplied evidence; inaccessible runtime state is unknown, not drift proven
* dependency degradation; traffic spikes; CPU, memory, and network saturation
* clock skew

Require recovery procedures for critical state. Recovery that depends on tribal knowledge is a defect.
