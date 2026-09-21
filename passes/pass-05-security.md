---
id: pass-05-security
name: Security
triggers:
  - any user-facing, network-facing, or privilege boundary exists in the submission
depends_on: [pass-01-assumptions]
---

## Pass 5 — Security

Assume:

> The client is hostile.

Inspect:

* authentication
* authorization
* tenant isolation
* IDOR
* privilege escalation
* server-side validation
* secrets
* token lifecycle
* replay attacks
* CSRF
* SSRF
* XSS
* SQL injection
* command injection
* path traversal
* insecure redirects
* webhook verification
* rate limiting
* brute-force resistance
* enumeration
* mass assignment
* unsafe uploads
* sensitive logs
* debug endpoints
* dependency trust
* supply-chain assumptions

Attack any security mechanism enforced only by:

* UI visibility
* client logic
* hidden IDs
* undocumented convention
* obscurity
