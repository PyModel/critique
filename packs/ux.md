# Pack: ux

UI, UX, and user-facing product flow reviews.

## Passes (in run order)

1. `passes/pass-01-assumptions.md`
2. `passes/pass-02-correctness.md`
3. `passes/pass-03-failure-semantics.md`
4. `passes/pass-10-ux.md`
5. `passes/pass-09-performance.md`
6. `passes/pass-13-testing.md`
7. `passes/pass-16-simplicity.md`

Add when the flow writes data or calls a backend:

- `passes/pass-05-security.md`
- `passes/pass-06-data-model.md`
- `passes/pass-07-api-contract.md`
- `passes/pass-04-concurrency.md`

## Notes

- The core UX question drives this pack: what does the user believe happened, and how does that differ from system state?
- Destructive or irreversible actions always pull in Security and Failure Semantics regardless of pack size.
