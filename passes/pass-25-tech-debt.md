---
id: pass-25-tech-debt
name: Tech Debt & Historical Leakage
triggers:
  - the artifact is an existing implementation, a change to one, or a plan that migrates, extends, or preserves one
phase: attack
---

## Pass 25 — Tech Debt & Historical Leakage

The current implementation is evidence, not authority. Judge every part against the end state from Pass 1, not against the history that produced it.

**Audit** — each hit is a candidate, not an automatic delete:

* marker comments: `TODO: remove after <past date>`, `DEPRECATED`, `temporary`, `hack`, `XXX`
* versioned identifiers: `_v2`, `_new`, `_old`, `Legacy*` — a finished migration (delete old), a failed one (delete new), or in flight (confirm the owner)
* feature flags that became permanent architecture: never flipped, one-line else, no removal plan
* dual-mode forks: `if legacy`, `if clientVersion < N` — the old path is rarely tested
* compatibility shims, route aliases, pass-through wrappers, adapters that only rename
* duplicate config keys (`retry_count` / `max_retries`) and duplicate state across layers
* the same decision rule (permission, validation, retry, derivation, routing) implemented in more than one place
* names that leak retired infrastructure or no longer match behavior (`MongoOrderStore` on Postgres; `processOrder` that handles refunds)
* tests that assert a historical bug; configuration that has become the code

For each candidate state: why it exists, who still depends on it, and whether removing it changes user-visible behavior.

**Preconditions** — a Delete, Unify, or Rename verdict becomes a Remediation step only with:

* a test pinning the behavior worth keeping — written first where missing, asserting intended behavior, not the historical bug shape
* every caller of the changed surface enumerated: code, tests, config, docs, CI, downstream consumers
* a rollback path
* no migration in flight on the same surface
* the telemetry, alerts, dashboards, and runbooks that name what is removed, updated in the same step

**Verdicts** feed the Workaround Ledger and the Shape Change section:

* **Delete** — no remaining caller or value.
* **Unify** — N paths or rules → 1 authoritative owner.
* **Rename** — to current domain language; every caller updated in the same step.
* **Left alone** — still earns its place; say why, so the next review does not re-flag it.
* **Deferred** — real debt needing separate work; state what it blocks.

Rules:

* `git blame` is not architectural authority. "It has always been this way" is inertia, not a constraint.
* Deletion and replacement are separate remediation steps.
* A constrained change (kernel Purpose) gets no structural cleanup: every verdict here goes to Deferred with its trigger.
