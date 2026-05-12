# Challenge 7 — AI Tool Comparison Scorecard
## Matching Tools to Analyst Tasks

This scorecard rates **GitHub Copilot**, **Claude**, **ChatGPT**, and **Gemini** against the criteria most relevant to WMC analyst workflows. Ratings use a 1–5 scale (5 = excellent). A **Best Fit** and **Backup Fit** tool is assigned to each task category.

---

## Evaluation Criteria

| Criterion | What it measures |
|---|---|
| **Reasoning depth** | Ability to follow multi-step analytical logic and handle nuance |
| **Coding support** | Quality of code generation, refactoring, and test writing |
| **Long-context handling** | Ability to work with lengthy documents, large schemas, or full codebases |
| **Document writing quality** | Fluency, structure, and accuracy of generated prose |
| **Workflow integration** | How readily the tool plugs into existing analyst toolchains |
| **Governance / security** | Data residency options, audit logging, enterprise controls |
| **Cost** | Per-token or subscription cost relative to value delivered |

---

## Tool Ratings

### GitHub Copilot

| Criterion | Rating | Notes |
|---|---|---|
| Reasoning depth | 3 | Strong within code context; weaker for open-ended analysis |
| Coding support | 5 | Best-in-class for in-repo code, tests, and CI tasks |
| Long-context handling | 4 | Workspace-aware; can scan full repo with agent mode |
| Document writing quality | 3 | Adequate for code comments and short docs; not long-form prose |
| Workflow integration | 5 | Native in VS Code, GitHub Actions, and PR workflows |
| Governance / security | 5 | Enterprise SKU; org-level policy controls; no training on private code |
| Cost | 4 | Per-seat pricing; good ROI for developer-heavy teams |

**Best suited for:** QA/test design, code documentation, data pipeline validation, reproducibility checks.

---

### Claude (Anthropic)

| Criterion | Rating | Notes |
|---|---|---|
| Reasoning depth | 5 | Excellent structured reasoning; handles complex, multi-step tasks |
| Coding support | 4 | Good code generation; not IDE-native |
| Long-context handling | 5 | 200k token context window; ideal for full reports or large schemas |
| Document writing quality | 5 | Best-in-class for long-form, structured prose |
| Workflow integration | 3 | API available; requires custom integration effort |
| Governance / security | 4 | Enterprise tier; strong privacy policies; EU data residency in progress |
| Cost | 3 | Higher per-token cost at long context; usage requires discipline |

**Best suited for:** Report writing, technical documentation, methodology reviews, assumption logging, stakeholder Q&A prep.

---

### ChatGPT (OpenAI GPT-4o / o1)

| Criterion | Rating | Notes |
|---|---|---|
| Reasoning depth | 5 | o1/o3 models excel at chain-of-thought; GPT-4o is versatile |
| Coding support | 4 | Strong code interpreter and generation; Python-centric |
| Long-context handling | 4 | 128k context; good but shorter than Claude |
| Document writing quality | 4 | High quality; slightly less structured than Claude |
| Workflow integration | 4 | Plugins, Custom GPTs, and API; flexible tooling |
| Governance / security | 3 | Enterprise tier available; US-hosted by default |
| Cost | 3 | Competitive; cost spikes with o1 reasoning tokens |

**Best suited for:** Exploratory analysis narratives, scenario generation, slide drafting, literature reviews, workflow prototyping.

---

### Gemini (Google DeepMind)

| Criterion | Rating | Notes |
|---|---|---|
| Reasoning depth | 4 | Strong reasoning; improving rapidly |
| Coding support | 4 | Good; strong with Python and Google ecosystem tooling |
| Long-context handling | 5 | 1M token context; unmatched for ingesting full datasets or documents |
| Document writing quality | 4 | Good quality; strong with structured formats |
| Workflow integration | 5 | Native in Google Workspace, BigQuery, Colab, Looker |
| Governance / security | 4 | Google Cloud enterprise controls; Workspace data governance |
| Cost | 4 | Competitive; generous free tier; Workspace integration adds value |

**Best suited for:** Data exploration at scale, multimodal analysis (charts/tables), Google-stack integrations, long-document synthesis.

---

## Task-to-Tool Assignment Matrix

| Task Category | Best Fit | Backup Fit |
|---|---|---|
| Technical documentation | Claude | Copilot |
| Executive report writing | Claude | ChatGPT |
| Scenario commentary | ChatGPT | Claude |
| Slide deck drafting | ChatGPT | Gemini |
| Stakeholder Q&A prep | Claude | ChatGPT |
| QA / test check design | Copilot | ChatGPT |
| Data validation rules | Copilot | Claude |
| Unit test scaffolding | Copilot | ChatGPT |
| Data dictionary population | Gemini | Claude |
| Exploratory analysis narratives | ChatGPT | Gemini |
| Forecasting methodology | Claude | ChatGPT |
| Assumption logging | Claude | ChatGPT |
| Scenario generation | ChatGPT | Claude |
| Literature review | Claude | ChatGPT |
| Reproducibility checks | Copilot | Claude |
| Risk and limitation registers | Claude | ChatGPT |

---

## Key Takeaways

1. **No single tool wins everything.** The right choice depends on task type, context length, and toolchain.
2. **Copilot dominates engineering tasks.** Use it for anything touching code, tests, or CI.
3. **Claude dominates writing tasks.** Use it for long-form, structured analysis and documentation.
4. **ChatGPT is the most versatile.** Ideal as a general fallback and for ideation workflows.
5. **Gemini shines at scale and in Google-stack environments.** Leverage its 1M token window for large ingestion tasks.

> **Next step:** see `03_agent_patterns_and_prompt_recipes.md` to operationalise these assignments.
