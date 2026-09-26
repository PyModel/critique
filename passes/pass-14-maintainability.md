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

Ask:

> Can an engineer modify this safely six months later without asking the original author?

Good architecture reduces the context an engineer needs to change it safely. Measure that: how many files, concepts, and conventions must one know to make the most common change?
