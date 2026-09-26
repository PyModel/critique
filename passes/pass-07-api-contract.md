---
id: pass-07-api-contract
name: API / Contract
triggers:
  - an API, endpoint, interface, SDK, protocol, tool schema, or client-server boundary exists in the submission
phase: attack
---

## Pass 7 — API / Contract

Inspect:

* explicit semantics; typed inputs and outputs; deterministic behavior
* error taxonomy — can the caller tell retryable from permanent?
* idempotency; retries; timeouts; deadlines; cancellation; long-running operations
* versioning; backward and forward compatibility; enum evolution
* pagination, filtering, sorting; partial updates; null semantics
* validation; field ownership; authentication and authorization boundaries
* observability hooks (request IDs, correlation)

Flag:

* undocumented behavior; magic defaults; overloaded endpoints
* inconsistent errors; transport leaking internal models
* APIs callers can only use correctly by knowing the implementation
* server behavior inferred only from frontend code

Prefer schema-first contracts with generated clients and contract tests when the boundary spans teams or deploy units.
