---
id: pass-12-observability
name: Observability
triggers:
  - production operation is claimed, or logging/metrics/tracing/alerting are mentioned
phase: attack
---

## Pass 12 — Observability

Can an operator determine, during failure: what happened, where, why, for whom, how often, how severe, and what changed — and whether the fix worked?

Inspect:

* structured logs with request and correlation IDs; traces across boundaries
* error categories; latency histograms; queue depth; saturation; retry counts
* dependency health; state-transition visibility; audit trails where required
* degradation, fallback, shed, retry-exhaustion, and dead-letter events each countable
* SLOs tied to user-visible behavior

Flag:

* logging that produces volume without diagnostic value; duplicate telemetry
* high-cardinality metric explosions; secrets or PII in logs
* logs used as the only correctness mechanism
* telemetry that a proposed deletion would silently remove
