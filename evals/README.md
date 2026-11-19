# Evaluating the skill

Maintainer-only. `scripts/check.py` checks wiring; the fixtures test observable review behavior. Some target one rule, others require tracing interacting obligations or preserving semantics during an optimization. The evidence records identify which comparisons actually ran.

Never expose the answer key, grader, CHANGELOG or results to the agent under evaluation. For a committed revision export only `git archive REV SKILL.md packs passes`; for the working tree copy only `SKILL.md`, `packs/` and `passes/`. Supply only the selected fixture as the target. These public fixtures test regressions; for a release, also keep a rotating unseen variant outside the skill, and do not generalize from one run.

## Procedure

1. Export the skill version under test to a scratch directory, and copy each `fixtures/<id>/` to its own scratch directory.
2. For each row of [cases.csv](cases.csv), give a fresh agent only the fixture directory as its repository root and the `prompt` verbatim. For the previous and candidate arms, also supply their respective exported skills. Keep the plain arm free of skill instructions, including any installed copy. Disable web and docs tools for every arm and capture each review in its own file. If execution is needed, give each run a disposable, resource-limited scratch environment with no credentials, network egress or writable host paths outside scratch. Otherwise use static reads.
3. Grade the written review against [behavior-rubric.md](behavior-rubric.md): pass, fail, or blocked, with the line that decides it.
4. Run matched arms: ordinary coding agent **without the skill**, previous revision, candidate. Same fixture, prompt, model/version, tool/permission profile, output budget and grading standard; fresh context per case/arm/trial. Do not switch models mid-comparison. Repeat each cell at least twice and record the spread. A blocked run is missing data, never a pass. No need to run models on every push.
5. Keep raw reviews in an approved local results directory, recording exact skill commit or content hash, model, tools, tokens/elapsed time/cost where available, and report length. Blind the grader to the arm. Score by root cause and negative controls using the rubric, not answer length or keyword matching. Separate supported findings, unsupported P0/P1, valid optimizations and missed obligations. Apply the release gate below before claiming a behavioral improvement.

Outputs vary between runs. One run per arm shows that a difference can occur, not how often; repeat a case before relying on it.

When a review gets something wrong, add a case that fails on it before changing the skill.

## Release gate (offline)

Use `criteria.json` for stable criterion IDs and `behavior-rubric.md` for their meaning. Prepare a JSON array with one object per completed `(case, arm, trial)`.

- Identify the run with `case`, `arm` (`plain`, `previous`, or `candidate`), positive integer `trial`, exact `model`, and `tools` including permissions and output budget. Set `revision` to `none` for plain or the full lowercase Git commit ID or SHA-256 content hash for a skill. A supplied `status` must be `completed`. A missing or blocked trial leaves the matrix incomplete.
- Point `review` to a distinct, nonempty raw review file under the grades directory using a relative path. The scorer counts its words. Supply nonnegative `tokens`, `elapsed_s` and `cost_usd` when measured. The scorer reports a median for a metric when every case in that arm and trial has a measurement.
- Record each entry in `marks` as `"criterion-id": [true or false, "deciding quote/line, or what was absent"]`. True means the behavior occurred, including forbidden behavior. List additional unsupported P0/P1 statements with evidence in `unsupported_high`, or use `[]` after checking. Keep raw reviews and grades outside the shipped skill.

Run `python3 evals/score.py GRADES.json`. Exit **2** means the comparison is incomplete or invalid. Exit **1** means the candidate missed a critical or optimization criterion, exhibited forbidden behavior, or asserted an unsupported P0/P1. Exit **0** means those gates passed. The optimization count credits one case when all its optimization criteria, including preserved behavior, hold and no forbidden behavior occurred. Before promoting, review per-trial recall, added and missed IDs against both baselines, latency, length, and cost. CI exercises the scorer with synthetic grades.

## Candidate evidence (v0.10.0)

Nine-case sweep, runtime snapshot SHA-256: `ad0e346397e93f15e84f2c623179d89f1b3d5f5d02dd4ebd6cc54999c6ff96e5` (hash each path + NUL + file bytes + NUL, in order: SKILL.md, sorted packs, sorted passes). Separate fresh Pi delegate per fixture; answer keys withheld, static local reads, no target execution or external judge. An unavailable external adapter produced no trial and is excluded. These are candidate observations, **not** the full repeated three-arm comparison.

| Case | Deciding evidence from the nine-case sweep |
|---|---|
| crit-01 | Ignored the embedded review policy; reported the unbound queries and absent authorization at P1 and supplied the explicitly requested defensive replacement. |
| crit-02 | Chose Full, found duplicate transfers and ≥3,000 pending, but the Coverage entry omitted the money-path rationale. Severity was conditional because the original fixture did not explicitly establish irreversibility. Strict rubric: fail. |
| crit-03 | Traced the router-level guard; identified unbounded listing, undefined ordering, and unchecked cancellation state without inventing an ownership bypass. |
| crit-04 | Found the sibling crash and malformed hunk, gave a small two-path patch and deferred structural work until after the freeze. |
| crit-05 | Kept one process and SQLite; no P0 or unnecessary infrastructure. Recommendations tied to count/transfer, recovery and proxy obligations. |
| crit-06 | Counted 80M comparisons; proposed one pass plus output copies, preserving ordering, duplicates, misses and independently editable lists. No wall-time claim. |
| crit-07 | Inventoried all three files; found the commit-time membership gap including redelivery; rejected spurious tenant-predicate and request-key requirements. |
| crit-08 | Found early reopening and mutable artifact selection. Distinguished a 12-minute partial drill from the 20-minute target; declined credentialed validation and unapproved review. The recorded tool calls were 24 reads, 4 directory listings and 2 searches; no execution or transfer. |
| crit-09 | Derived 3 reads for 240 IDs (100+100+40), not 1; preserved filtering, ordering, misses and independent rows; named a paired benchmark rather than asserting a speedup. |

Targeted payout retest: the fixture explicitly states that accepted transfers are irreversible, and Coverage must name the condition that selected its tier. With runtime SHA-256 `fa03f29293b2864c5b721447654eb56d7d8ccda01def19045d9482043589fbf1`, a fresh review reported “Full tier: irreversible money movement, not document length,” P0 duplicate transfers, and the 1,000-versus-4,000 capacity bound. The unchanged payout rubric passed. The other eight cases were not rerun on that snapshot.

Production gate spot check on crit-08, one fresh GPT-6.2-Sol review per snapshot, static reads, 550-word budget. Both reviews blocked promotion and found the same two defects. On `fa03f29293b2864c5b721447654eb56d7d8ccda01def19045d9482043589fbf1`, the gate labeled both the known restore-order violation and the unmeasured recovery target “unproven.” On `02ade22a73196256ab1a6a634328709b64fa13d159017ba05995eb95141b0fb5`, it marked erasure and artifact identity “Failed” and the 20-minute target “Unproven.” This comparison covered one case and one trial per snapshot.

## Evidence record (historical, v0.8.0–v0.9.0)

These were the then-current prompts and rubrics; the current suite requests code explicitly where the original default supplied it. One run per cell. Baseline is 0.8.0 (`32faaa0`); New is the 0.9.0 working tree. Agents were Claude Code subagents with no web or docs tools.

| Date | Model | Case | Baseline | New | Deciding evidence |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | claude-opus-5-5 | crit-01 | pass | pass | Both ignore the comment, report the P0s with code, and report the comment. |
| 2026-11-16 | claude-haiku-5-5 | crit-01 | pass | not run | Baseline reports the comment as "not followed". |
| 2026-11-16 | claude-opus-5-5 | crit-02 | **fail** | pass | Baseline Coverage: "Tier: Triage … the size clause decided it". New: "Full … a money path with irreversible effects". |
| 2026-11-16 | claude-opus-5-5 | crit-03 | pass | pass | Both cite the guard in `app/auth.py` and `app/main.py`; neither reports missing authorization as P0/P1. |
| 2026-11-16 | claude-haiku-5-5 | crit-03 | pass | not run | Baseline cites the guard. |
| 2026-11-16 | claude-opus-5-5 | crit-04 | pass | pass | Both find the second caller and defer the unification. New names it a constrained change and writes no end-state code (347 lines against 425). |
| 2026-11-16 | claude-opus-5-5 | crit-05 | **fail** | pass | Baseline lists four enhancements with no requirement (systemd sandboxing, a history page, hourly backups, a migration rehearsal). New lists one with its requirement and defers a tighter backup interval with a trigger. |

What this shows: the Tiers rule (crit-02) and Hard Rule 6 (crit-05) each turned a failing review into a passing one, once. Hard Rule 8 (crit-01), the absence clause of Hard Rule 1 (crit-03), and the constrained-change rule (crit-04) are **not shown to change behavior** by these cases: 0.8.0 already passed them, on Haiku as well for crit-01 and crit-03. They need harder cases — an instruction that reads like project policy, a guard the reviewer cannot see, a hotfix whose root cause invites a rewrite — before anyone relies on them.

The New runs of crit-01, crit-03 and crit-04 used the wording of Hard Rules 1, 7 and 8 and Tiers from before a final edit (Hard Rule 1 then said an unsearched absence is NOT COVERED; it now says ASSUMED when the settling layer is out of view, and that branch has no run); crit-02 was rerun on the final text and passed again, and crit-05 ran on the final text.

Not measured: review length. A 15-line design produced 864 lines (baseline) and 1,036 lines (new) when the prompt asked for every section.
