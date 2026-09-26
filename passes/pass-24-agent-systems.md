---
id: pass-24-agent-systems
name: Agent & LLM Systems
triggers:
  - the artifact calls language models, runs agents or tool loops, builds prompts, retrieves context, or treats model output as input to other systems
phase: attack
---

## Pass 24 — Agent & LLM Systems

Model output is untrusted, nondeterministic input. Design as if it lies sometimes.

**Trust and authority**

* prompt injection through retrieved documents, tool results, user content, or web pages
* tool permissions broader than the task needs; no human confirmation on irreversible actions
* model output flowing into shell, SQL, file paths, URLs, or other models without validation
* instructions used as access control ("the agent is told not to…")
* secrets or private data placed in prompts, logs, or traces

**Correctness under nondeterminism**

* output parsed without a schema, or schema violations not handled
* single-sample decisions where the cost of a wrong answer warrants verification
* agent loops with no termination bound, step budget, or progress check
* state kept only in the conversation instead of a durable store
* retries of tool calls with side effects and no idempotency

**Cost and waste**

* redundant model or tool calls; missing caching of stable prefixes or results
* context stuffed beyond what the task uses; unbounded conversation growth
* a large model doing work a deterministic function or small model could do
* no per-request token or spend ceiling

**Evaluation and operations**

* no eval set with pass/fail criteria; changes to prompts or models shipped unmeasured
* model/version pinning; behavior drift on provider upgrades
* fallback behavior when the provider is slow, rate-limited, or down
* traces sufficient to reconstruct why the agent took an action

Dedupe: generic injection and authz belong to Pass 5; generic token/spend bounds to Pass 23. This pass owns model-specific mechanisms.
