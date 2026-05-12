# Challenge 7 — AI-Assisted Forecasting Methodology
## Linking the Agent Approach to the Forecasting Challenge

This document applies the Challenge 7 agent patterns to the specific problem of **developing forecasting methodology**. The goal is to demonstrate how AI can take on the analytical design work — proposing, justifying, and validating a forecasting approach — while the analyst retains decision authority.

---

## The Problem: Asking AI to Develop Forecasting Methodology

When a WMC team faces a new forecasting task, a significant portion of analyst time is spent on:
1. Selecting candidate methods
2. Justifying the selection for the given data regime
3. Designing the validation framework
4. Writing up the methodology

All four of these steps can be substantially assisted by AI, using the Assumptions Challenger and Methods Reviewer patterns from `03_agent_patterns_and_prompt_recipes.md`.

---

## Step 1: AI Proposes Candidate Forecasting Methodologies

**Recommended tool:** Claude or ChatGPT  
**Pattern:** Adapted Methods Reviewer + Assumptions Challenger

### Prompt Recipe — Forecasting Method Selector

```
You are an expert forecasting methodologist advising a government analytical team.

I will describe the forecasting problem. Your job is to:
1. Identify the data regime (see criteria below).
2. Propose a shortlist of 3–5 candidate forecasting methods appropriate to that regime.
3. For each method, explain: what it is, why it suits this regime, its main limitations, and what data it requires.
4. Recommend one method as your primary choice and justify the choice.
5. Flag any gaps in the information I have provided that would change your recommendation.

Data regime criteria to assess:
- History length: how many data points are available?
- Seasonality: is there a regular seasonal pattern?
- Trend: is there a clear upward or downward trend?
- Exogenous drivers: are there external variables that predict the series?
- Structural breaks: have there been step-changes or policy interventions?
- Forecast horizon: how far ahead is the forecast needed?
- Uncertainty requirements: is a point forecast or a prediction interval needed?

---
FORECASTING PROBLEM:

Series being forecast: [INSERT — e.g., "monthly A&E attendances by health board"]
Available history: [INSERT — e.g., "72 months of data, Jan 2019 – Dec 2024"]
Seasonality observed: [YES / NO / UNSURE — describe if yes]
Trend observed: [YES / NO / UNSURE — describe if yes]
Known exogenous drivers: [LIST OR "none identified"]
Known structural breaks: [LIST OR "none identified — but note COVID impact 2020–21"]
Forecast horizon: [INSERT — e.g., "24 months ahead, monthly granularity"]
Uncertainty requirements: [e.g., "80% and 95% prediction intervals required"]
Primary use of forecast: [e.g., "capacity planning, published quarterly"]
---

Produce your method shortlist, recommendation, and gap flags now.
```

---

## Step 2: AI Justifies Method Selection by Data Regime

The prompt above generates a reasoned recommendation. The table below maps data regimes to the methods AI is most likely to recommend, giving analysts a quick cross-check:

| Data Regime | Likely Recommended Methods |
|---|---|
| Short history (< 24 obs), no seasonality | Exponential smoothing (SES, Holt), ARIMA |
| Short history, strong seasonality | Holt-Winters, STL decomposition |
| Long history, stable trend and seasonality | SARIMA, Prophet, ETS |
| Long history, known exogenous drivers | ARIMAX, regression with ARIMA errors, ML (XGBoost) |
| Structural breaks present | Piecewise models, intervention analysis, Prophet with changepoints |
| High uncertainty / ensemble required | Model averaging, bootstrap ensembles, quantile regression |
| Very long history, complex patterns | LSTM / temporal fusion transformer (only with sufficient data) |
| Hierarchical series (e.g., by health board) | Hierarchical forecasting (bottom-up, top-down, MinT) |

---

## Step 3: AI Generates a Validation Framework

**Recommended tool:** Copilot (for code-based validation) or Claude (for specification)

### Prompt Recipe — Forecasting Validation Designer

```
You are an expert forecasting validation specialist.

I have chosen [METHOD NAME] to forecast [SERIES NAME]. I need you to design a validation framework that will tell me whether this method is performing acceptably before I publish the forecast.

Design the validation framework to include:

1. BACKTESTING DESIGN
   - Specify the rolling-origin (time-series cross-validation) setup: origin start, step size, minimum training window, and number of test windows.
   - Specify the forecast horizons to evaluate (e.g., h=1, 3, 6, 12).

2. ERROR METRICS
   - Specify which metrics to compute and why: choose from MAE, RMSE, MAPE, sMAPE, MASE, Winkler score (for intervals).
   - Specify the primary metric for model selection.
   - Define the pass/fail threshold for each metric.

3. BIAS CHECKS
   - Specify how to detect systematic over- or under-forecasting.
   - Propose a statistical test for forecast bias.

4. STABILITY CHECKS
   - Specify how to test whether forecast accuracy is stable over time (not degrading).
   - Propose a chart or test for this.

5. BENCHMARK COMPARISON
   - Specify a naive benchmark (e.g., seasonal naive) to compare against.
   - The chosen method must beat the benchmark on the primary metric.

---
INPUTS:

Method chosen: [INSERT]
Series: [INSERT]
Forecast horizon: [INSERT]
Historical data available: [INSERT]
Seasonality: [YES / NO]
Prediction intervals required: [YES / NO]
---

Produce the validation framework specification now, including Python or R code for each component where helpful.
```

---

## Step 4: AI Produces a Forecasting Decision Memo

Once validation is complete, AI drafts the decision memo — applying the Report Writer pattern.

### Prompt Recipe — Forecasting Decision Memo

```
You are an expert analyst writing a forecasting methodology decision memo for internal sign-off.

Using the inputs below, draft a concise decision memo that documents:
1. The forecasting problem and business context.
2. The candidate methods considered and why each was or was not selected.
3. The chosen method with full justification.
4. The validation results (include the numbers I provide).
5. Trade-offs accepted and risks that remain.
6. Monitoring triggers: at what point would we revisit the method choice?

Rules:
- Be direct and specific. Do not hedge without reason.
- Document rejected alternatives briefly but clearly.
- The memo must be self-contained — a reader unfamiliar with the project must understand the decision.
- Maximum 2 pages.

---
INPUTS:

Forecasting problem: [INSERT]
Candidate methods considered: [LIST]
Chosen method: [INSERT]
Justification: [INSERT]
Validation results: [INSERT — e.g., MAPE = 4.2%, beats seasonal naive MAPE of 7.1%, no significant bias detected]
Key trade-offs: [INSERT]
Risk register items: [INSERT]
Monitoring triggers: [INSERT OR ask AI to propose them]
---

Draft the decision memo now.
```

---

## Integration with the Challenge 7 Agent Library

The forecasting patterns above slot directly into the broader agent library:

| Challenge 7 Pattern | Forecasting Application |
|---|---|
| Report Writer | Forecasting decision memo; methodology chapter |
| QA Check Designer | Validation framework; data input checks |
| Methods Reviewer | Peer review of chosen method before sign-off |
| Assumptions Challenger | Surface assumptions in method choice and data |

---

## Human Sign-Off Requirements for Forecasting

Forecasting outputs carry additional risk because they inform resource allocation and published statistics. The following human-in-the-loop gates apply beyond the standard ones in `03_agent_patterns_and_prompt_recipes.md`:

| Gate | Trigger | Action |
|---|---|---|
| **Method approval** | AI recommends a method | Senior analyst reviews and formally accepts or overrides |
| **Validation sign-off** | Validation results meet thresholds | Lead analyst confirms and records in model register |
| **Structural break review** | Forecast deviates significantly from outturn | Human investigates before next publication |
| **External publication** | Forecast published in official statistics | Full sign-off including statistical adviser clearance |

---

> **Next step:** see `05_pilot_plan.md` to run these patterns on a real case.
