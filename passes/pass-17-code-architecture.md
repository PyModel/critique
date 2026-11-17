---
id: pass-17-code-architecture
name: Code Architecture & Change Coupling
triggers:
  - the submission is source code
phase: attack
---

## Pass 17 — Code Architecture & Change Coupling

Attack the code's structure with one question: **should these pieces change together?** Code gets the answer wrong in three ways.

**Hidden links** — must change together, and nothing shows it

* copy-pasted rules or values that must evolve together; parallel definitions of one concept (types, constants, validation thresholds)
* business rules duplicated between validation and persistence paths
* a module reading a global, file, or environment variable another module sets
* one feature split across folders by layer, so a single conceptual change touches many files (shotgun surgery)
* a call order or convention callers must simply know
* Boundary: only duplication that encodes the **same rule** is a link. Similar-looking code with different evolution is not — forcing it shared creates a coupling bug.

**Needless links** — tied together, change for different reasons

* functions mixing IO, business logic, and presentation; classes with several reasons to change; god objects
* callers depending on internals; modules reaching across layers (handler importing DB driver, domain importing transport types)
* stable code importing something more volatile than itself; business logic constructing its own concrete dependencies instead of receiving them
* a general function carrying a parameter only one caller understands
* shallow modules whose interface changes whenever their internals do; fat interfaces whose consumers implement half the methods as no-ops
* subtype or interface implementations violating caller expectations

**Surplus** — no reason of its own to change

* pass-through wrappers; abstraction layers with one implementation and one caller (kernel Hard Rule 3 applies verbatim)
* parameters, configuration, extension points, and branches with no caller, or for what never varies
* dead code, commented-out code, "future-proofing"

Ask:

> Which files would I have to touch to change X?

If the answer is a scatter, the boundaries are wrong. The target: a typical change lands in one place, and nothing imports anything more volatile than itself.

Dedupe: design-level abstraction tax belongs to Pass 16; this pass reports code-level instances with line evidence.
