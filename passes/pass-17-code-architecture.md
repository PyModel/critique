---
id: pass-17-code-architecture
name: Code Architecture (SOLID / DRY / YAGNI)
triggers:
  - the submission is source code
phase: attack
---

## Pass 17 — Code Architecture (SOLID / DRY / YAGNI)

Attack the code's structure.

**Separation of concerns**

* functions mixing IO, business logic, and presentation
* modules reaching across layers (handler importing DB driver, domain importing transport types)
* business rules duplicated between validation and persistence paths

**SOLID violations**

* SRP: classes/functions with multiple reasons to change; god objects
* OCP: shotgun surgery — one conceptual change requires touching many files
* LSP: subtype or interface implementations violating caller expectations
* ISP: fat interfaces whose consumers implement half the methods as no-ops
* DIP: business logic constructing its own concrete dependencies instead of receiving them

**DRY — eliminate duplicate logic**

* copy-pasted rules that must evolve together
* parallel definitions of the same concept (types, constants, validation thresholds)
* Boundary: extract only duplication that encodes the **same rule**. Similar-looking code with different evolution is not duplication — forcing it shared creates a coupling bug.

**YAGNI — delete speculation**

* parameters, configuration, and branches with no caller
* abstraction layers with one implementation and one caller (kernel Hard Rule 3 applies verbatim)
* dead code, commented-out code, "future-proofing"

Ask:

> Which function would I have to touch to change X?

If the answer is a scatter of files, the module boundaries are wrong.

Dedupe: design-level abstraction tax belongs to Pass 16; this pass reports code-level instances with line evidence.
