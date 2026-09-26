---
id: pass-01-assumptions
name: Assumption Extraction & Reframe
triggers:
  - always
phase: frame
---

## Pass 1 — Assumption Extraction & Reframe

**Reframe.** Before extracting assumptions, reconstruct the problem:

* What problem actually needs solving? Is the artifact solving that one?
* Which guarantees are required, which optional? Which failures are acceptable, which catastrophic?
* What is the source of truth for each important piece of state, and who owns each transition?
* Which operations must be atomic; which may be eventually consistent?
* What workload shape, latency, and throughput actually matter?
* What is the smallest architecture meeting those requirements — and what would you build if none of this existed yet?

State the intended end state in 1–3 sentences. Every later finding is judged against it.

**Extract assumptions** the design depends on but does not encode. Common ones:

* requests arrive once; messages stay ordered; workers never run twice
* clocks agree; IDs are unique; payload schemas stay compatible
* external APIs are available — and fast when available
* clients obey the protocol and cannot manipulate client-controlled values
* writes across boundaries succeed atomically; retries are harmless
* caches stay coherent; all records fit in memory; traffic grows gradually
* operators configure deployment correctly; versions never coexist
* users finish workflows; model/agent outputs follow instructions

For each important assumption:

**Assumption → Failure condition → Consequence → Required protection (preferably by construction: constraint, type, state machine, ownership)**
