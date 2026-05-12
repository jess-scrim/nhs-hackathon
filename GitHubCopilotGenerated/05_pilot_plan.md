# Challenge 7 — Pilot Execution Plan
## Running AI Agent Patterns on Real Cases

This document defines a structured pilot to test the Challenge 7 agent patterns against real WMC analyst work. The pilot produces evidence on quality, time saving, and trust — and generates the final reusable playbook for network adoption.

---

## Pilot Objectives

1. Validate that the prompt recipes produce useful, accurate outputs on real data.
2. Quantify the time saving compared to manual analyst effort.
3. Identify rework rate and quality gaps that require pattern refinement.
4. Produce trust and safety findings to inform governance decisions.
5. Publish a final reusable playbook for WMC network adoption.

---

## Pilot Scope: Three Priority Tasks

The pilot focuses on the three highest-value, most immediately ready tasks from the delegation catalogue:

| Priority | Task | Pattern used | Tool |
|---|---|---|---|
| 1 | **Report drafting** — executive summary from model outputs | Report Writer | Claude |
| 2 | **QA check generation** — data pipeline test suite | QA Check Designer | Copilot / Claude |
| 3 | **Forecasting method recommendation** — method selection memo | Forecasting Method Selector + Decision Memo | Claude |

---

## Pilot Design: Human vs AI Side-by-Side

Each task will be run as a **controlled comparison**:

```
Step 1 — Human baseline
  An analyst completes the task using their normal process.
  Time is recorded. Output is saved as the "human baseline".

Step 2 — AI-assisted run
  The same analyst (or a second analyst) runs the AI prompt recipe on the same inputs.
  Time is recorded. The AI output is saved without editing.

Step 3 — AI output reviewed and refined
  The analyst reviews the AI output, makes corrections, and produces a "human-reviewed AI output".
  Rework time is recorded.

Step 4 — Blind quality assessment
  A third analyst (blind to which is which) rates both the human baseline and the human-reviewed AI output
  on the acceptance checks defined in each pattern.

Step 5 — Results recorded
  Metrics are recorded in the pilot log (see below).
```

---

## Pilot Metrics

| Metric | Definition | How measured |
|---|---|---|
| **Time to first draft** | Minutes from task start to complete draft | Analyst self-report (stopwatch) |
| **Rework time** | Minutes spent correcting AI output | Analyst self-report |
| **Total AI-assisted time** | Rework time + prompt time (not including setup) | Analyst self-report |
| **Time saving** | Human baseline time minus total AI-assisted time | Calculated |
| **Quality score** | Blind reviewer rating on acceptance check criteria (0–10) | Blind reviewer rating |
| **Accuracy errors** | Count of factual errors in AI output before correction | Reviewer count |
| **Hallucination incidents** | AI-generated content not supported by inputs | Reviewer count |
| **Escalation events** | Times an escalation rule was triggered | Analyst log |

---

## Pilot Log Template

For each pilot task, complete this record:

```
PILOT TASK LOG

Task:                     [e.g., Report drafting — executive summary]
Pattern used:             [e.g., Report Writer]
Tool used:                [e.g., Claude]
Date:                     [DATE]
Analyst:                  [INITIALS ONLY]
Blind reviewer:           [INITIALS ONLY]

TIME RECORDING
  Human baseline time:    [MINUTES]
  AI prompt run time:     [MINUTES]
  AI rework time:         [MINUTES]
  Total AI-assisted time: [MINUTES]
  Time saving:            [MINUTES / %]

QUALITY ASSESSMENT (blind reviewer)
  Human baseline score:   [0–10]
  AI-assisted score:      [0–10]

ACCURACY FINDINGS
  Factual errors in AI output (before correction): [COUNT]
  Hallucination incidents: [COUNT]
  Description of errors:  [FREE TEXT]

ESCALATION EVENTS
  Triggered:              [YES / NO]
  Description:            [FREE TEXT]

OVERALL ASSESSMENT
  AI output usable as first draft:   [YES / NO / WITH MAJOR EDITS]
  Would use this pattern again:      [YES / NO / MAYBE]
  Recommended pattern change:        [FREE TEXT OR "none"]
```

---

## Pilot Timeline

| Week | Activity |
|---|---|
| Week 1 | Set up: brief pilot analysts, confirm real case inputs, finalise prompt recipes |
| Week 2 | Run Task 1 pilot (report drafting) — human baseline and AI-assisted runs |
| Week 3 | Run Task 2 pilot (QA check generation) — human baseline and AI-assisted runs |
| Week 4 | Run Task 3 pilot (forecasting method recommendation) — human baseline and AI-assisted runs |
| Week 5 | Blind quality assessments; compile pilot log results |
| Week 6 | Analysis of results; pattern refinement; draft playbook |
| Week 7 | Playbook review and sign-off |
| Week 8 | Publish playbook to WMC network; present findings at network meeting |

---

## Definition of Success

The pilot is considered successful if the following thresholds are met across all three tasks:

| Threshold | Target |
|---|---|
| Average time saving | ≥ 30% reduction in time to acceptable first draft |
| Quality score | AI-assisted output ≥ 7/10 (before rework) or ≥ 9/10 (after rework) |
| Hallucination rate | ≤ 1 uncorrected hallucination per task after rework |
| Analyst confidence | ≥ 80% of pilot analysts say they would use the pattern on a real task |

---

## Final Playbook Structure

The output of the pilot is a **WMC AI Agent Playbook** with this structure:

```
WMC AI Agent Playbook
│
├── Introduction and how to use this playbook
├── Governance principles (human-in-the-loop gates, publication rules)
├── Tool guidance (which tool for which task, procurement notes)
│
├── Pattern Library
│   ├── Pattern 1 — Report Writer          [prompt + worked example]
│   ├── Pattern 2 — QA Check Designer      [prompt + worked example]
│   ├── Pattern 3 — Methods Reviewer       [prompt + worked example]
│   ├── Pattern 4 — Assumptions Challenger [prompt + worked example]
│   └── Pattern 5 — Forecasting Methodology [prompt + worked example]
│
├── Pilot Results Summary
│   ├── Time saving evidence
│   ├── Quality evidence
│   └── Trust and safety findings
│
└── How to contribute new patterns to the library
```

Each pattern entry includes a **worked example** — a real (anonymised) input and the AI output produced during the pilot, annotated with what was good, what needed correction, and what the escalation trigger was.

---

## Network Adoption

Once the playbook is published, WMC teams adopt patterns by:

1. **Cloning this repository** and using patterns as-is or adapting for local context.
2. **Submitting new patterns** via pull request — using the pattern template in `03_agent_patterns_and_prompt_recipes.md`.
3. **Reporting quality issues** via GitHub Issues — linking to the specific pattern and describing the failure.
4. **Reviewing patterns annually** — each pattern is reviewed against updated AI capabilities and any new governance requirements.

---

> This completes the Challenge 7 deliverable set. See `README.md` for a full index of all documents.
