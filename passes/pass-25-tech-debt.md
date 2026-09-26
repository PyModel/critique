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

For each candidate state: why it exists, who still depends on it, and whether removing it changes user-visible behavior.

**Verdicts** feed the Workaround Ledger and the Shape Change section:

* **Delete** — no remaining caller or value.
* **Unify** — N paths or rules → 1 authoritative owner.
* **Rename** — to current domain language; every caller updated in the same step.
* **Left alone** — still earns its place; say why, so the next review does not re-flag it.
* **Deferred** — real debt needing separate work; state what it blocks.

Rules:

* `git blame` is not architectural authority. "It has always been this way" is inertia, not a constraint.
* Removal of code must not silently remove its telemetry, alerts, or tests of intended behavior.
* Deletion and replacement are separate remediation steps.
* Do not apply structural cleanup to a hotfix or security backport; there, a minimal targeted change wins and the debt goes to Deferred.
