---
id: pass-22-state-invariants
name: State Model & Invariants
triggers:
  - the artifact has a workflow, lifecycle, status field, or multi-step business or infrastructure process
  - persistent or shared state is mutated by more than one operation
phase: attack
---

## Pass 22 — State Model & Invariants

Treat every important workflow as a state machine, whether or not the artifact does.

Make explicit:

* valid and invalid states; legal and illegal transitions
* the single owner of each transition; its preconditions, postconditions, atomicity
* retry and recovery semantics of each transition

Attack:

* boolean flags encoding a multi-state workflow (`is_paid && !is_shipped && is_cancelled`)
* contradictory, implicit, or duplicated states; stale derived state
* transitions spread across modules with no single owner
* transitions without transactional protection
* external side effects before durable state — or durable state committed before a required side effect
* retries that can duplicate an irreversible effect

**Invariants.** List the invariants that must always hold (e.g. one authoritative owner per resource; no backward transition unless modeled; a committed operation never leaves half-applied state; no request consumes unbounded resources; version mismatches fail safe). For each, state where it is **encoded** — database constraint, type, constructor, schema, state machine, unique index, atomic operation — or flag it as **convention-only**.

Prefer designs where invalid states cannot be represented over designs that detect them at runtime.

Dedupe: this pass owns the model; Pass 19 owns code-level mutation safety; Pass 6 owns how the database enforces it.
