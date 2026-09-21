---
id: pass-07-api-contract
name: API / Contract
triggers:
  - an API, endpoint, interface, SDK, or client-server boundary exists in the submission
depends_on: [pass-06-data-model]
---

## Pass 7 — API / Contract

Inspect:

* versioning
* compatibility
* error models
* idempotency
* pagination
* filtering
* sorting
* validation
* enum evolution
* partial updates
* null semantics
* field ownership
* retries
* timeout semantics
* long-running operations
* authorization boundaries

Flag:

* undocumented behavior
* magic defaults
* overloaded endpoints
* inconsistent errors
* transport leaking internal models
* breaking enum assumptions
* server behavior inferred only from frontend code
