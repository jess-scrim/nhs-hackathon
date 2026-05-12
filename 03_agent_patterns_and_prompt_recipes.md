# Challenge 7 — Agent Patterns and Prompt Recipes
## Reusable Templates for the Wales Modelling Collaborative

This document provides **agent pattern templates** and **ready-to-use prompt recipes** that any WMC analyst can pick up and adapt. Each pattern follows a standard structure to make the AI's role, inputs, and quality bar explicit.

---

## Agent Pattern Template

Every reusable agent pattern in this library follows this structure:

```
PATTERN NAME:     A short, memorable name
OBJECTIVE:        What this agent pattern achieves in one sentence
RECOMMENDED TOOL: Which AI tool to use (and why)
INPUTS:           What the analyst must supply before running
CONSTRAINTS:      What the agent must NOT do (scope limits, no-hallucination rules)
ACCEPTANCE CHECKS:How the analyst verifies the output is good enough
OUTPUT FORMAT:    The expected structure of the deliverable
ESCALATION RULES: When to stop the AI and bring in human judgement
```

---

## Pattern 1 — Report Writer

```
PATTERN NAME:     Report Writer
OBJECTIVE:        Draft a full technical or executive report from structured inputs
RECOMMENDED TOOL: Claude (long-form prose quality); ChatGPT as backup
INPUTS:
  - Model name and version
  - Purpose of the analysis (one paragraph)
  - Key outputs and findings (bullet list or table)
  - Known limitations (bullet list)
  - Audience type (technical / executive / ministerial)
  - House style guide (if available, paste key rules)
CONSTRAINTS:
  - Do not invent numbers, findings, or sources not in the inputs
  - Do not draw policy conclusions unless explicitly instructed
  - Flag any gap where more information is needed rather than filling it speculatively
ACCEPTANCE CHECKS:
  - All figures in the report match the inputs provided
  - Limitations section is present and not watered down
  - Executive summary can stand alone without the body
OUTPUT FORMAT:
  Markdown or Word-compatible structure:
  1. Executive Summary (max 1 page)
  2. Background and Purpose
  3. Methodology Summary
  4. Key Findings
  5. Limitations and Caveats
  6. Recommendations (if in scope)
  7. Appendix (technical detail)
ESCALATION RULES:
  - Escalate to human author if policy interpretation is required
  - Escalate if any finding contradicts previous published outputs
```

### Prompt Recipe — Report Writer

```
You are an expert analyst report writer working for a Welsh Government modelling team.

I will give you structured inputs. Your job is to draft a [TECHNICAL / EXECUTIVE] report using those inputs.

Rules:
- Do not invent any numbers, names, or findings not present in the inputs.
- If a section cannot be completed because information is missing, write [INFORMATION NEEDED: describe what is missing] rather than guessing.
- Write in plain English suitable for [AUDIENCE TYPE].
- Keep the executive summary to no more than one A4 page.
- Flag any assumption you make explicitly.

---
INPUTS:

Model name and version: [INSERT]
Purpose of analysis: [INSERT]
Key findings: [INSERT AS BULLET LIST]
Limitations: [INSERT AS BULLET LIST]
Audience: [technical / executive / ministerial]
---

Draft the report now, following this structure:
1. Executive Summary
2. Background and Purpose
3. Methodology Summary
4. Key Findings
5. Limitations and Caveats
6. Recommendations (only if in scope — if not, omit)
7. Appendix
```

---

## Pattern 2 — QA Check Designer

```
PATTERN NAME:     QA Check Designer
OBJECTIVE:        Generate a comprehensive suite of data and model QA checks
RECOMMENDED TOOL: GitHub Copilot (code-native checks); Claude for prose specification
INPUTS:
  - Data schema (field names, types, expected ranges)
  - Model type (e.g., regression, time series, microsimulation)
  - Known business rules (e.g., totals must sum to X, no negatives in column Y)
  - Previous known data quality issues (if any)
CONSTRAINTS:
  - Checks must be executable (produce pass/fail output)
  - Do not omit null/missing value checks
  - Checks must be version-controlled and repeatable
ACCEPTANCE CHECKS:
  - Every field in the schema has at least one check
  - At least one cross-field or aggregate check is included
  - Checks can run without manual intervention
OUTPUT FORMAT:
  - A numbered list of checks with: check ID, description, logic/query, expected result, severity (Error / Warning / Info)
  - Optional: Python / SQL implementation of each check
ESCALATION RULES:
  - Escalate if a check requires domain knowledge about what a "valid" value is
  - Escalate if a check cannot be automated (requires visual or contextual judgement)
```

### Prompt Recipe — QA Check Designer

```
You are a senior data quality engineer. I need you to design a QA check suite for a data pipeline.

I will provide the schema and business rules. Your job is to produce a complete, executable set of checks.

Rules:
- Every field must have at least one check (null check, range check, or format check).
- Include at least one cross-field consistency check and one aggregate/totals check.
- For each check, specify: Check ID, Description, Logic (plain English or SQL/Python), Expected Result, Severity (Error / Warning / Info).
- If you need a business rule I haven't provided, flag it as [RULE NEEDED: describe gap].

---
INPUTS:

Schema:
[PASTE SCHEMA — field name, data type, expected range/values]

Business rules:
[LIST KNOWN RULES]

Known past data issues:
[LIST OR "none known"]
---

Produce the QA check suite now.
```

---

## Pattern 3 — Methods Reviewer

```
PATTERN NAME:     Methods Reviewer
OBJECTIVE:        Critically review a methodology note for completeness, rigour, and consistency
RECOMMENDED TOOL: Claude (structured reasoning and long-context)
INPUTS:
  - Methodology document (paste or attach)
  - Review criteria (e.g., ONS quality framework, HMT Green Book, WG internal standard)
  - Known concerns to investigate (optional)
CONSTRAINTS:
  - Do not rewrite the document — produce a structured review only
  - Flag omissions and weaknesses; do not soften findings to be polite
  - Rate each dimension and explain the rating
ACCEPTANCE CHECKS:
  - Every major methodology section is covered in the review
  - Ratings are justified with specific evidence from the document
  - A prioritised list of required improvements is produced
OUTPUT FORMAT:
  - Dimension-by-dimension scorecard (completeness, reproducibility, validation, transparency, limitations)
  - Top 3 must-fix issues (blocking sign-off)
  - Top 5 should-fix issues (recommended improvements)
  - Overall assessment (Approved / Approved with conditions / Not approved)
ESCALATION RULES:
  - Escalate to human reviewer if overall assessment is "Not approved"
  - Escalate if document contains statistical claims that require specialist verification
```

### Prompt Recipe — Methods Reviewer

```
You are an expert peer reviewer for a government analytical team. Review the methodology document I provide against the criteria below.

Rules:
- Be direct and critical. Do not soften findings.
- Rate each dimension: Satisfactory / Partially satisfactory / Unsatisfactory.
- For each rating, quote the specific passage that supports your assessment.
- Produce a prioritised list of issues: must-fix (blocks sign-off) and should-fix (recommended).
- Give an overall assessment: Approved / Approved with conditions / Not approved.

Review criteria: [INSERT FRAMEWORK — e.g., ONS Quality Framework / HMT Green Book / internal standard]

---
DOCUMENT TO REVIEW:

[PASTE METHODOLOGY DOCUMENT]
---

Produce your structured review now.
```

---

## Pattern 4 — Assumptions Challenger

```
PATTERN NAME:     Assumptions Challenger
OBJECTIVE:        Surface, stress-test, and log the assumptions underpinning a model or analysis
RECOMMENDED TOOL: Claude or ChatGPT (structured reasoning)
INPUTS:
  - Model description (purpose, outputs, audience)
  - Current assumption list (if one exists)
  - Relevant policy context or data sources
CONSTRAINTS:
  - Challenge assumptions constructively — propose alternatives, not just criticisms
  - Do not change the model design; identify risks only
  - Record every assumption even if it seems obvious
ACCEPTANCE CHECKS:
  - Every assumption is rated by impact (High / Medium / Low) and certainty (High / Medium / Low)
  - At least one alternative scenario is proposed for each High-impact assumption
  - Output is structured for inclusion in a model documentation register
OUTPUT FORMAT:
  - Assumption register table: ID, Assumption, Justification, Impact, Certainty, Alternative, Owner
  - Narrative section: top 3 assumptions warranting sensitivity analysis
ESCALATION RULES:
  - Escalate if an assumption is contested by published evidence the AI cites
  - Escalate if a High-impact / Low-certainty assumption has no mitigation
```

### Prompt Recipe — Assumptions Challenger

```
You are an expert model auditor. I need you to surface and challenge the assumptions in the analysis I describe.

Rules:
- List every assumption, including ones so common they are rarely stated.
- Rate each by: Impact on outputs (High / Medium / Low) and Certainty of the assumption (High / Medium / Low).
- For every High-impact assumption, propose at least one plausible alternative.
- Identify the top 3 assumptions that most warrant a sensitivity test.
- Format the output as an assumption register table, then a narrative section.

---
INPUTS:

Model description: [INSERT]
Existing assumption list: [INSERT OR "none"]
Policy context: [INSERT]
---

Produce the assumption register and narrative now.
```

---

## Human-in-the-Loop Gates

All patterns above are designed to produce **draft outputs for human review**, not final outputs. The following gates must be maintained regardless of output quality:

| Gate | Trigger | Human action required |
|---|---|---|
| **Factual sign-off** | Any output containing numbers or conclusions | Analyst verifies against source data |
| **Policy interpretation** | Any output touching policy recommendations | Senior analyst or policy lead reviews |
| **Publication gate** | Any output intended for external release | Full QA and clearance process applies |
| **Escalation trigger** | AI flags a gap or expresses uncertainty | Human investigates before proceeding |
| **Version control** | Any AI-generated output saved as a deliverable | Committed to repo with AI-generated label |

---

> **Next step:** see `04_forecasting_methodology.md` to apply these patterns to the forecasting challenge.
