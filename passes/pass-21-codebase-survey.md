---
id: pass-21-codebase-survey
name: Codebase Survey & Stratification
triggers:
  - the artifact is an entire codebase, repository, or module tree rather than a single design or file
phase: frame
---

## Pass 21 — Codebase Survey & Stratification

Reviewing a codebase is not reviewing a large file. Survey first, stratify, then attack.

**Survey — before any finding**

* entry points: HTTP handlers, queue consumers, CLIs, cron jobs, exports — where untrusted input enters
* data flow: where state lives (database, cache, files, memory) and where it mutates
* dependency graph: internal module boundaries and external dependencies (Pass 15 deep-dives the externals)
* hot paths: highest-QPS, latency-critical, and throughput-critical routes
* cross-cutting conventions: error handling, logging, config, retries — and where the convention silently breaks
* change history, where available: churn (which files change most) and co-change (which change together) — evidence for Tier A and for hidden links (Pass 14)

A codebase too large to hold in view is surveyed from its skeleton first — signatures and imports without bodies — so the whole shape is seen before depth is allocated.

**Stratify — review depth is allocated by risk, not uniformly**

* **Tier A (full rigor):** hot paths, money/auth/mutation paths, anything with a P0-capable failure — run the code passes (9, 17–20, 22, 23) file by file
* **Tier B (risk-sampled):** the rest — pattern-level review (error-handling style, N+1 call sites, blocking I/O, unbounded queries), spot-check the outliers
* **Tier C (structural):** module boundaries, dependency direction, dead code mass — Passes 14 and 16 at architecture level

**Coverage ledger — mandatory.** Default risk review may sample B and examine C structurally; label both. In inventory mode, enumerate in-scope source, configs, build/release definitions, migrations, jobs, tests and public entry points before choosing depth. Include ignored/generated/vendor code only when relevant to the shipped behavior; record exclusions. Map critical actors, state owners, sinks and irreversible effects across file boundaries. Risk order still decides where to start, not what counts as done.

Use `path or flow | risk | traced / sampled / not examined / out of scope | evidence or reason | next action`. “Traced” means the relevant path and guard were followed to their effect, not merely that a file was opened. For large trees use nonoverlapping groups with counts and separately name high-risk exceptions. Reconcile counts to the inventory; for incomplete enumeration say which root remains unenumerated. Any in-scope sampled/unexamined item means **partial coverage**, with a resumable next item. Even complete scope coverage is not proof of zero defects.

**Codebase-specific attack surface**

* death by a thousand cuts: the same small inefficiency at every call site (per-request allocation, redundant serialization, missing batching) — report the class once with its aggregate cost, not 200 instances
* convention drift: the codebase's own error/retry/config pattern violated in exactly the dangerous places
* configuration traps: flags and env vars that change failure semantics
* repository rot: dead modules, duplicated utilities, parallel implementations of the same concept (Pass 25 owns the deletion verdicts)

Dedupe: single-file defects found in Tier A report through the code passes; this pass owns the survey, the stratification, and the aggregate findings.
