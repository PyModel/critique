---
id: pass-14-maintainability
name: Maintainability & Developer Experience
triggers:
  - a codebase, long-lived system, or contributor-facing surface is under review
phase: attack
---

## Pass 14 — Maintainability & Developer Experience

Identify:

* hidden coupling; unclear ownership; excessively broad modules; god objects
* duplicated business rules; misleading names; sprawling conditionals
* runtime behavior controlled by distant or hidden configuration
* abstractions requiring tribal knowledge; unsafe or unclear extension points
* APIs easy to misuse; poor error messages; difficult debugging
* difficult setup; fragile local environments; slow test loops
* duplicated commands; excessive boilerplate; complex contribution workflows

Ask of every boundary: **should these pieces change together?** A design gets the answer wrong in three ways (Pass 17 owns the code-level instances):

* **hidden links** — pieces that must change together while nothing shows it
* **needless links** — pieces tied together that change for different reasons
* **surplus** — pieces with no reason of their own to change

Ask:

> Can an engineer modify this safely six months later without asking the original author?

Good architecture reduces the context an engineer needs to change it safely. Measure that: how many files, concepts, and conventions must one know to make the most common change? The target is one place. Where change history exists it is evidence: files that change together but live apart are a hidden link, and the most-churned files are where structure costs most.
