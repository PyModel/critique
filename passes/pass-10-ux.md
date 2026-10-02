---
id: pass-10-ux
name: UX
triggers:
  - a user-facing interface, workflow, or interaction surface exists in the submission
phase: attack
---

## Pass 10 — UX

Review the system from the user's perspective. For every user action trace: what the user sees → what the system actually did → what happens if it fails midway, is repeated, or is abandoned → how the user recovers.

Attack:

* states: loading, empty, error, retry, partial success, permission denied, offline, stale — each designed, or each a finding
* double submission; back button, refresh, or second tab mid-flow; optimistic UI that disagrees with server truth
* irreversible actions: weak confirmation, destructive defaults, no undo or grace period
* hidden state and ambiguous labels — the user cannot predict what an action will do
* excessive steps, modal chains, duplicate controls, cognitive load
* inaccessible interactions: keyboard, screen reader, contrast, focus order, motion
* slow perceived response with no progress; data loss on navigation; small-viewport breakage

Ask:

> What does the user believe happened?

Then compare that belief to actual system state. That gap is a UX bug.

Dedupe: server-side enforcement of what the UI prevents belongs to Pass 5; the failure semantics behind a retry control to Pass 3.
