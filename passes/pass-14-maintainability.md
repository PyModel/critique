---
id: pass-14-maintainability
name: Maintainability
triggers:
  - a codebase or long-lived system is under review
depends_on: [pass-02-correctness]
---

## Pass 14 — Maintainability

Identify:

* hidden coupling
* duplicated business rules
* misleading names
* excessively broad modules
* god objects
* sprawling conditional logic
* unsafe extension points
* unclear ownership
* runtime behavior controlled by distant configuration
* abstractions requiring tribal knowledge

Ask:

> Can an engineer modify this safely six months later without asking the original author?
