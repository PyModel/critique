# Pack: code

Exhaustive production-grade review and refactoring of source code, in the submission's language.

## Passes (in run order)

1. `passes/pass-01-assumptions.md`
2. `passes/pass-02-correctness.md`
3. `passes/pass-03-failure-semantics.md`
4. `passes/pass-14-maintainability.md`
5. `passes/pass-17-code-architecture.md`
6. `passes/pass-20-execution-order.md`
7. `passes/pass-19-idempotency-integrity.md`
8. `passes/pass-18-thread-safety.md` (when triggers match)
9. `passes/pass-09-performance.md` (always for code)
10. `passes/pass-13-testing.md`
11. `passes/pass-16-simplicity.md` (last)

Add when applicable:

- `passes/pass-04-concurrency.md` — business flows where duplicate scenarios matter (webhook handlers, payments, cart mutations)
- `passes/pass-05-security.md` — auth, API surface, or untrusted input handling
- `passes/pass-06-data-model.md` — persistence code
- `passes/pass-08-scalability.md` — explicit scale claims

## Notes

- Output uses the kernel's **Code tier**: Critical Audit → Refactored Implementation → Key Trade-offs.
- The refactored code is a fix: every added or changed library/API call goes through the Fix Validation Protocol.
- Write the refactor in the submission's language and idioms; flag every deliberate behavior change inline.
- Performance findings must state time/space complexity deltas.
- Pass 17 and Pass 4/18 must not double-report the same concurrency defect — 18 owns the mechanism, 4 owns the scenario.
