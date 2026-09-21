---
id: pass-12-observability
name: Observability
triggers:
  - production operation is claimed, or logging/metrics/alerting are mentioned
depends_on: [pass-11-operations]
---

## Pass 12 — Observability

Ask whether an operator can determine:

1. something is broken,
2. which component is responsible,
3. which users are affected,
4. why it happened,
5. whether the fix worked.

Inspect:

* structured logs
* request IDs
* trace IDs
* tenant identifiers
* latency histograms
* queue depth
* retries
* error classification
* domain metrics
* saturation metrics
* audit trails

Flag logging that produces lots of text but little diagnostic value.
