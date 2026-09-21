---
id: pass-10-ux
name: UX
triggers:
  - a user-facing interface, workflow, or interaction surface exists in the submission
depends_on: [pass-03-failure-semantics]
---

## Pass 10 — UX

Review the system from the user's perspective.

Attack:

* unclear hierarchy
* excessive steps
* modal chains
* hidden state
* ambiguous labels
* poor empty states
* missing progress
* irreversible actions
* weak confirmation
* bad mobile behavior
* duplicate controls
* inaccessible interactions
* poor keyboard behavior
* slow perceived response
* destructive defaults
* excessive cognitive load

Ask:

> What does the user believe happened?

Then compare that belief to actual system state.

That gap is a UX bug.
