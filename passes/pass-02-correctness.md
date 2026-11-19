---
id: pass-02-correctness
name: Correctness
triggers:
  - always
phase: attack
---

## Pass 2 — Correctness

Attack:

* invalid or contradictory states; missing invariants
* lost, duplicate, or partial updates; ambiguous commits
* stale, inconsistent, non-repeatable, or phantom reads; write skew
* incorrect transaction boundaries; TOCTOU
* ordering and uniqueness assumptions; eventual-consistency assumptions
* empty, null, malformed, minimum, and maximum inputs; off-by-one
* integer overflow, float precision, truncation
* money and quantity arithmetic: rounding, currency minor units, unit mismatches
* encoding and Unicode edge cases
* timezones, clock skew, leap time
* native/FFI or binary boundaries: trace who owns memory, bounds and integer width conversions, alignment, partial initialization, cleanup and platform/ABI differences. Use documented contracts, safe boundary-value tests or existing sanitizer diagnostics; do not create corruption inputs
* schema or serialization mismatches between producer and consumer
* pagination correctness; deletion semantics; mutable historical records

Trace the actual consequence of each — never list the possibility alone.

Ask:

> Can the system represent a state that should be impossible?

If yes, show the path that reaches it.

Dedupe: a concurrency defect is reported once — business scenario in Pass 4 (designs) or mechanism in Pass 18 (code) when those passes run; here otherwise.
