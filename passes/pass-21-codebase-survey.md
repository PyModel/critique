---
id: pass-21-codebase-survey
name: Codebase Survey & Stratification
triggers:
  - the artifact is an entire codebase, repository, or module tree rather than a single design or file
depends_on: [pass-01-assumptions]
---

## Pass 21 — Codebase Survey & Stratification

Reviewing a codebase is not reviewing a large file. Survey first, stratify, then attack.

**Survey — before any finding**

* entry points: HTTP handlers, queue consumers, CLIs, cron jobs, exports — where untrusted input enters
* data flow: where state lives (database, cache, files, memory) and where it mutates
* dependency graph: internal module boundaries and external dependencies (Pass 15 deep-dives the externals)
* hot paths: highest-QPS, latency-critical, and throughput-critical routes
* cross-cutting conventions: error handling, logging, config, retries — and where the convention silently breaks

**Stratify — review depth is allocated by risk, not uniformly**

* **Tier A (full rigor):** hot paths, money/auth/mutation paths, anything with a P0-capable failure — run the code passes (17, 18, 19, 20, 9) file by file
* **Tier B (risk-sampled):** the rest — pattern-level review (error-handling style, N+1 call sites, blocking I/O, unbounded queries), spot-check the outliers
* **Tier C (structural):** module boundaries, dependency direction, dead code mass — Passes 14 and 16 at architecture level

**Coverage ledger — mandatory in output**

State what was reviewed at which tier and what was not reviewed at all. An unaudited directory listed as such is honest scope; an implied full review that actually sampled is a lie.

**Codebase-specific attack surface**

* death by a thousand cuts: the same small inefficiency at every call site (per-request allocation, redundant serialization, missing batching) — report the class once with its aggregate cost, not 200 instances
* convention drift: the codebase's own error/retry/config pattern violated in exactly the dangerous places
* configuration traps: flags and env vars that change failure semantics
* repository rot: dead modules, duplicated utilities, parallel implementations of the same concept

Dedupe: single-file defects found in Tier A report through the code passes (17–20, 9); this pass owns the survey, the stratification, and the aggregate findings.
