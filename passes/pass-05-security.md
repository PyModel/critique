---
id: pass-05-security
name: Security
triggers:
  - any user-facing, network-facing, privilege, tenant, or untrusted-input boundary exists in the submission
phase: attack
---

## Pass 5 — Security

Assume:

> The client is hostile, and so is every input that crosses a boundary.

Inspect:

* authentication; authorization; resource ownership; tenant isolation; IDOR
* authorization per object on every read and write path, not per endpoint; establish the tenant boundary on every access via a verified query predicate, row policy, isolated store or equivalent; check the effective runtime identity and bypass paths before declaring a missing control
* the same check on cache hits, retries, replays, fallbacks, background jobs, admin and recovery paths; tenant and scope derived from verified context, never from request fields
* an entry point missing the authentication, authorization, validation, or limits its sibling entry points enforce
* privilege escalation; least privilege; capability scoping
* server-side validation; mass assignment; unsafe deserialization
* injection: SQL, command, template, prompt (where model input mixes with untrusted text)
* path traversal; arbitrary file access; unsafe uploads; SSRF
* CSRF; XSS; insecure redirects
* secrets management; credential lifetime and rotation; token leakage
* cryptographic misuse: homegrown primitives, weak randomness for tokens, non-constant-time comparison, secrets in error messages
* replay attacks; webhook signature verification
* rate limiting and its bypasses; brute force; enumeration
* resource-exhaustion and denial-of-service surfaces
* information leakage through errors, logs, or timing
* debug endpoints; dependency trust; supply-chain assumptions

Attack any mechanism enforced only by UI visibility, client logic, hidden IDs, undocumented convention, or obscurity.

A defensive finding names the actor, controlled input, intended control and reachable effect, grounded in code/config evidence. A category alone is not a finding. Verify by tracing enforcement or benign tests of the intended policy; do not construct exploits or test a live target. For queued work involving revocable rights, verify the required authority when the effect occurs, not just when enqueued.

Security belongs in the boundary design, not in middleware bolted on afterward — prefer fixes that move enforcement to the owning boundary.
