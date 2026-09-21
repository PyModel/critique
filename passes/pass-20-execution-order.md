---
id: pass-20-execution-order
name: Execution Order & Error Handling
triggers:
  - the submission is source code
depends_on: [pass-02-correctness]
---

## Pass 20 — Execution Order & Error Handling

Attack the structure of operations.

**Lifecycle order** — code should read top-to-bottom following natural execution:

1. validate inputs (fail-fast, before any side effect)
2. retrieve state
3. core business logic (pure where possible)
4. mutations and side effects — last, after all failure modes have been excluded
5. return / serialize

Attack:

* side effects that fire before validation completes
* business logic interleaved with IO
* mutations embedded in the middle of validation chains
* functions mixing multiple levels of abstraction

**Fail-fast error handling**

* swallowed errors: empty catch blocks, discarded results, unchecked error returns
* catch-all handlers converting programmer errors into silent fallbacks
* errors stripped of context (no wrapping, no operation name, no identifiers)
* cleanup not guaranteed on error paths (resources leak on early return)
* edge cases at boundaries: empty, single, max, unicode, null/nil/undefined, timezone, overflow

Prefer guard clauses and early exits over nested conditional pyramids.

Dedupe: whether error *types* are modeled correctly is Pass 3 territory; this pass owns code structure — where validation sits, in what order effects run, and whether failures surface or sink.
