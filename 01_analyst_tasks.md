# Challenge 7 — Analyst Tasks Catalogue
## Tasks We Are Willing to Relinquish to AI

This document catalogues the analyst tasks under consideration for AI delegation within the Wales Modelling Collaborative (WMC). Tasks are grouped by category and rated by **delegation readiness** (High / Medium / Low) based on current tooling maturity and organisational risk appetite.

---

## 1. Documentation

| Task | Description | Delegation Readiness |
|---|---|---|
| Technical documentation drafting | Producing method notes, data dictionaries, and data source logs | High |
| Automated documentation updates | Re-generating docs when model code or assumptions change | High |
| Glossary and metadata management | Keeping definitions, field descriptions, and lineage records current | High |
| Meeting minutes and action logs | Summarising meeting notes into structured action items | Medium |

---

## 2. Report Writing

| Task | Description | Delegation Readiness |
|---|---|---|
| Executive summaries | Translating model outputs into plain-English briefing notes | High |
| Technical reports | Drafting full methodology and results chapters | High |
| Scenario commentary | Writing narrative explanations for each modelled scenario | High |
| Slide deck drafting | Producing first-cut PowerPoint content from a results brief | Medium |
| Stakeholder Q&A prep | Anticipating questions and drafting model responses | Medium |

---

## 3. Quality Assurance and Testing

| Task | Description | Delegation Readiness |
|---|---|---|
| QA check design | Generating test suites and acceptance criteria for data pipelines | High |
| Data validation rule specification | Writing rules for range checks, referential integrity, null handling | High |
| Unit test scaffolding | Creating test stubs and fixtures from function signatures | High |
| Regression test analysis | Comparing outputs across model versions and flagging differences | Medium |
| Peer-review checklists | Generating structured review templates for model sign-off | High |

---

## 4. Data Preparation

| Task | Description | Delegation Readiness |
|---|---|---|
| Data cleaning rule drafting | Specifying imputation, outlier, and transformation logic | Medium |
| Data dictionary population | Auto-generating field descriptions from schema and sample data | High |
| Data lineage mapping | Tracing source-to-output data flows | Medium |
| Exploratory analysis narratives | Describing distributions, trends, and anomalies from EDA outputs | High |

---

## 5. Methodology and Analytical Design

| Task | Description | Delegation Readiness |
|---|---|---|
| Forecasting methodology recommendation | Proposing and justifying candidate methods for a given data regime | Medium |
| Assumption logging | Recording, versioning, and challenging model assumptions | Medium |
| Scenario generation | Proposing plausible scenario sets given a modelling context | Medium |
| Literature / precedent review | Summarising existing approaches for a given analytical problem | High |
| Sensitivity analysis design | Suggesting parameters to test and ranges to sweep | Medium |

---

## 6. Governance and Audit

| Task | Description | Delegation Readiness |
|---|---|---|
| Reproducibility checks | Verifying that model runs can be re-executed from source | Medium |
| Audit trail generation | Producing structured records of model decisions and changes | Medium |
| Risk and limitation registers | Cataloguing known model limitations and risk ratings | High |
| Ethical review prompts | Flagging potential fairness, data-use, or bias concerns | Medium |

---

## Summary

The tasks most immediately ready for AI delegation are those producing structured text from well-defined inputs: documentation, executive summaries, QA check design, data dictionaries, and literature reviews. Tasks involving judgement about model correctness or policy implications remain human-led, with AI in a supporting role.

> **Next step:** see `02_ai_tool_scorecard.md` to match tools to tasks.
