---
id: pass-08-scalability
name: Scalability
triggers:
  - growth, traffic, user counts, or large data volumes are claimed or implied
phase: attack
---

## Pass 8 — Scalability

Do not merely ask whether something is `O(n)`.

Determine what grows with: users · tenants · requests · connections · records · events · workers · uploaded files · context size · history · cache cardinality.

Look for: unbounded scans · offset pagination · N+1 queries · fan-out amplification · global locks · huge transactions · synchronous external calls · memory proportional to total state · unlimited queues · hotspot keys · high-cardinality metrics · uncontrolled retry storms.

Every finding names the growth axis, the resource that saturates first, and the multiple of current load at which it does — or the measurement that would establish it. "This won't scale" without those three is not a finding.

Check workload arithmetic before recommending scale-out: inflow versus unique completions per window, retries and duplicate work, batch re-selection, the stopping condition and oldest-item age. State when a bound assumes a single batch. A fast worker cannot drain more items than it selects.

Distinguish **current bottleneck** from **future scalability risk**. Do not invent scale requirements.

Dedupe: bounds and overload behavior belong to Pass 23; hot-path cost to Pass 9.
