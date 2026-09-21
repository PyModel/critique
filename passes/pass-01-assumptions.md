---
id: pass-01-assumptions
name: Assumption Extraction
triggers:
  - always
depends_on: []
---

## Pass 1 — Assumption Extraction

Identify assumptions the design depends upon.

Examples:

* requests arrive once
* messages remain ordered
* clocks are accurate
* IDs are unique
* external APIs are available
* clients obey the protocol
* database writes succeed atomically across boundaries
* retries are harmless
* events are processed once
* cache entries remain coherent
* users finish workflows
* operators configure deployment correctly
* workers do not run twice
* payload schemas remain compatible
* traffic grows gradually
* all records fit in memory
* users cannot manipulate client-controlled values

For each important assumption:

**Assumption → Failure condition → Consequence → Required protection**
