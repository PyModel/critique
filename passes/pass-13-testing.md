---
id: pass-13-testing
name: Testing
triggers:
  - always
depends_on: [pass-02-correctness]
---

## Pass 13 — Testing

Reject vague claims such as "add tests."

Specify required categories:

### Unit

Pure domain invariants.

### Integration

Database, queue, cache, filesystem, or external boundary behavior.

### Contract

API compatibility and schemas.

### Concurrency

Simultaneous conflicting operations.

### Failure injection

Timeouts, retries, crashes, duplicate delivery, dependency outages.

### Migration

Forward migration, compatibility window, rollback behavior.

### E2E

Critical user workflows.

### Security

Authorization boundaries and abuse cases.

### Performance

Critical path under representative workload.

For each critical finding, state the test that would prove the fix.

(This pass defines **what to prove**. The Remediation Plan's Tests field plans **when**; the Bulletproof Gate checks **whether it was proven**. Do not restate the same test list in all three.)
