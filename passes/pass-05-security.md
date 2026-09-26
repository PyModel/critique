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
* privilege escalation; least privilege; capability scoping
* server-side validation; mass assignment; unsafe deserialization
* injection: SQL, command, template, prompt (where model input mixes with untrusted text)
* path traversal; arbitrary file access; unsafe uploads; SSRF
* CSRF; XSS; insecure redirects
* secrets management; credential lifetime and rotation; token leakage
* replay attacks; webhook signature verification
* rate limiting and its bypasses; brute force; enumeration
* resource-exhaustion and denial-of-service surfaces
* information leakage through errors, logs, or timing
* debug endpoints; dependency trust; supply-chain assumptions

Attack any mechanism enforced only by UI visibility, client logic, hidden IDs, undocumented convention, or obscurity.

Security belongs in the boundary design, not in middleware bolted on afterward — prefer fixes that move enforcement to the owning boundary.
