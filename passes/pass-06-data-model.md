---
id: pass-06-data-model
name: Data Model
triggers:
  - persistence, schema, database, files, or cache is mentioned or implied
depends_on: [pass-02-correctness]
---

## Pass 6 — Data Model

Attack schemas for:

* missing constraints
* nullable states that should be impossible
* incorrect ownership
* duplicate sources of truth
* denormalization without consistency rules
* overloaded columns
* JSON used to avoid modeling
* missing foreign keys
* missing uniqueness constraints
* soft-delete contamination
* unbounded tables
* dangerous cascades
* timestamps standing in for state machines
* missing auditability
* irreversible migrations

Ask:

> Which invariants exist only in application code?

Those are prime failure candidates.
