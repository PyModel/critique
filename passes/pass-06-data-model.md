---
id: pass-06-data-model
name: Data Model & Persistence
triggers:
  - persistence, schema, database, files, or cache is mentioned or implied
phase: attack
---

## Pass 6 — Data Model & Persistence

Review persistence independently of application logic.

**Schema**

* missing constraints, foreign keys, uniqueness; nullable states that should be impossible
* duplicate sources of truth; derived state persisted without a consistency rule
* overloaded columns; JSON used to avoid modeling; timestamps standing in for state machines
* incorrect ownership; dangerous cascades; soft-delete contamination; missing auditability

**Access**

* transaction boundaries and isolation level vs the anomalies the logic can tolerate
* optimistic vs pessimistic concurrency; idempotency keys stored with a uniqueness constraint
* indexes vs actual query shapes; query plans; N+1; unbounded result sets; pagination semantics
* hot partitions; read/write amplification

**Lifecycle**

* migrations: expand/contract, backward and forward compatibility, rollback, irreversible steps
* retention, archival, unbounded tables
* backups, restore, corruption recovery — tested or assumed?

Ask:

> Which invariants exist only in application code?

Those are prime failure candidates — the database should guarantee them.
