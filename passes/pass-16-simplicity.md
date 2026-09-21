---
id: pass-16-simplicity
name: Simplicity
triggers:
  - always
depends_on: []
---

## Pass 16 — Simplicity

Identify complexity that can be deleted.

Look for:

* layers with no meaningful responsibility
* distributed systems solving local problems
* asynchronous flows that can be synchronous
* synchronous flows that should be asynchronous
* configurable behavior nobody needs
* generic abstractions replacing 20 lines of explicit code

Prefer the simplest architecture that preserves the required properties.

Run this pass last among the passes: after the other passes have mapped the design's real requirements, judge which complexity survives.
