# Pack: api

API, contract, and integration design reviews.

## Passes (in run order)

1. `passes/pass-01-assumptions.md`
2. `passes/pass-02-correctness.md`
3. `passes/pass-03-failure-semantics.md`
4. `passes/pass-05-security.md`
5. `passes/pass-06-data-model.md`
6. `passes/pass-07-api-contract.md`
7. `passes/pass-08-scalability.md`
8. `passes/pass-09-performance.md`
9. `passes/pass-11-operations.md`
10. `passes/pass-13-testing.md`
11. `passes/pass-14-maintainability.md`
12. `passes/pass-15-dependency-risk.md`
13. `passes/pass-16-simplicity.md`

## Notes

- Pass 7 (API/Contract) is the spine of this pack; it runs after Data Model so schema problems are known before contract problems are judged.
- Concurrency (`pass-04`) joins when the API accepts writes that can be duplicated (webhooks, retries, double submit).
- UX (`pass-10`) joins when the API's consumer is a user-facing client.
