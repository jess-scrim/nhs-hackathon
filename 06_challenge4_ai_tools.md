# Challenge 7 × Challenge 4 — AI Tools for Forecasting Work
## Applying Agent Patterns to Challenge 4 Tasks

Challenge 4 asks the team to:
- **(a)** Collate existing forecasting solutions using GitHub
- **(b)** Develop an accessible forecasting tool in Excel
- **(c)** Compare all solutions by performance/accuracy on the same time series

This document shows how Challenge 7's agent patterns can do the heavy lifting for each of those three tasks — and provides the ready-to-use prompt recipes to run them right now.

---

## Task (a) — Collating Existing Forecasting Solutions

**What AI does:** Searches, reads, and summarises GitHub repositories and library documentation, then structures findings into a catalogue the team can use.

**Pattern used:** Literature / Precedent Review (from `01_analyst_tasks.md`)  
**Recommended tool:** ChatGPT (broad web search + structured output) or Gemini (Google Scholar + GitHub indexing)

### Prompt Recipe — Forecasting Solutions Researcher

```
You are an expert data scientist helping a government analytics team catalogue forecasting tools.

Your job is to produce a structured catalogue of forecasting solutions suitable for a small public-sector team working primarily in Python, R, and Excel.

For each solution, provide:
- Name and GitHub URL (if applicable)
- Primary language / platform
- Methods covered (e.g., ARIMA, ETS, Prophet, ML, deep learning)
- Ease of use rating (1=specialist only, 5=accessible to non-coder)
- Best suited for (short series / long series / seasonal / hierarchical / uncertain)
- Key limitations
- Licence

Organise the catalogue into four tiers:
  Tier 1 — Excel / no-code tools
  Tier 2 — Python libraries (statsmodels, Prophet, etc.)
  Tier 3 — R libraries (forecast, fable, etc.)
  Tier 4 — Specialist / ML / deep learning

Cover at least 3 tools per tier. After the catalogue, write a one-paragraph recommendation
for a team that wants to start quickly with minimal setup.

Only include tools you are confident exist and are maintained. If you are uncertain about
a URL or version, flag it as [VERIFY].
```

### How to use the output
1. Run the prompt → review AI catalogue against [VERIFY] flags
2. Check each GitHub URL and star count manually (takes ~15 min)
3. Add any WMC-specific tools the AI missed
4. Commit the reviewed catalogue as `challenge4/01_solutions_catalogue.md`

---

## Task (b) — Developing an Accessible Excel Forecasting Tool

**What AI does:** Designs the workbook structure, writes the Excel formulas, and generates the Python build script that creates the `.xlsx` file.

**Pattern used:** QA Check Designer (structure) + Report Writer (instructions sheet)  
**Recommended tool:** GitHub Copilot (code generation) with Claude for the instructions prose

### Prompt Recipe — Excel Tool Architect (Copilot / ChatGPT)

```
You are an expert Python developer and Excel power user.

Write a Python script using openpyxl that generates a ready-to-use Excel forecasting workbook
for a non-technical government analyst.

The workbook must:
1. Contain sample monthly time series data (60 months, with trend and seasonality).
2. Implement these forecasting methods using Excel formulas only (no VBA, no macros):
   - 3-period moving average
   - 6-period moving average
   - Simple exponential smoothing (manual alpha=0.3 column)
   - Holt-Winters via FORECAST.ETS with seasonality=12
   - Linear trend via FORECAST.LINEAR
3. Show a 12-month forecast beyond the historical data for each method.
4. Include an Accuracy sheet that calculates MAE, RMSE, and MAPE for each method
   using the last 12 months of history as a holdout period.
5. Include a Comparison chart showing all methods vs actuals.
6. Include an Instructions sheet written in plain English for a non-technical user.

Code requirements:
- The script must run with only openpyxl installed (pip install openpyxl).
- Apply readable formatting: header rows in bold, alternating row shading,
  clear section labels, method columns colour-coded.
- Add a comment above each formula block explaining what it calculates.
- The generated file must be named WMC_Forecasting_Tool.xlsx.

Output the complete Python script.
```

### Prompt Recipe — Instructions Sheet Writer (Claude)

```
You are a plain-English technical writer for a government analyst team.

Write the content for an "Instructions" sheet in an Excel forecasting workbook.
The audience is a government analyst who is comfortable with Excel but has no
statistics or programming background.

Cover:
1. What this tool does and when to use it (2–3 sentences)
2. How to replace the sample data with your own data (step-by-step)
3. What each forecasting method does (one plain-English sentence each):
   - 3-period moving average
   - 6-period moving average
   - Simple exponential smoothing (alpha=0.3)
   - Holt-Winters (seasonal exponential smoothing)
   - Linear trend
4. How to read the Accuracy sheet and which method to choose
5. Important limitations and when NOT to use this tool
6. Where to get help

Write in second person ("You can..."). Maximum 600 words. No jargon without explanation.
```

### How to use the outputs
1. Run the Excel Tool Architect prompt → save script as `challenge4/forecasting_tool/build_excel_tool.py`
2. Run the Instructions Sheet Writer prompt → paste result into the script's instructions sheet builder
3. Run `python build_excel_tool.py` → verify the `.xlsx` opens correctly
4. Share the `.xlsx` directly — no Python needed by end users

---

## Task (c) — Comparing All Forecasting Solutions

This is the most analytical task. AI assists at three levels: **writing the comparison code**, **designing the test harness**, and **interpreting and reporting the results**.

### Sub-task c1: AI Writes the Comparison Script

**Recommended tool:** GitHub Copilot (in-editor) or ChatGPT Code Interpreter

#### Prompt Recipe — Comparison Script Generator

```
You are a senior Python data scientist.

Write a Python script that:
1. Loads a monthly time series from a CSV file (columns: date, value).
2. Splits it into training (first 80%) and test (last 20%) sets.
3. Implements and evaluates these forecasting methods on the same split:
   a. Seasonal naive (repeat same month last year)
   b. 3-period moving average
   c. 6-period moving average
   d. Simple exponential smoothing (auto-optimised alpha)
   e. Holt's linear exponential smoothing
   f. Holt-Winters additive (seasonal period=12)
   g. Holt-Winters multiplicative (seasonal period=12)
   h. ARIMA(1,1,1) fixed order
   i. SARIMA(1,1,1)(1,1,1,12) fixed order
4. For each method, compute on the test set:
   - MAE (mean absolute error)
   - RMSE (root mean squared error)
   - MAPE (mean absolute percentage error)
   - sMAPE (symmetric MAPE)
   - MASE (mean absolute scaled error, relative to seasonal naive)
5. Print a ranked comparison table (ranked by MASE ascending).
6. Save the results table to results/accuracy_comparison.csv.
7. Plot all method forecasts vs actuals and save to results/forecast_comparison.png.

Requirements:
- Use pandas, numpy, statsmodels, matplotlib.
- Handle exceptions gracefully (if a method fails, record NaN and continue).
- Add docstrings to all functions.
- The script must run with: python compare_methods.py --data sample_data.csv
```

### Sub-task c2: AI Designs the Test Harness

**Recommended tool:** Claude (structured analytical reasoning)

#### Prompt Recipe — Comparison Test Harness Designer

```
You are an expert forecasting evaluation specialist.

I am running an accuracy comparison of forecasting methods for a government analytics team.
I need you to specify the test harness — the rules for how the comparison will be conducted —
so that the results are fair, reproducible, and meaningful.

Design the test harness covering:

1. DATA REQUIREMENTS
   - Minimum series length for reliable comparison
   - How to handle missing values and outliers before the test
   - Whether to test on one series or multiple series (and why)

2. TRAIN / TEST SPLIT
   - Recommended split ratio and why
   - Whether to use a single split or rolling-origin cross-validation (and why)
   - How to handle seasonality in the split

3. EVALUATION RULES
   - Which accuracy metrics to use as primary, secondary, and diagnostic
   - How to interpret each metric for this context (government planning forecasts)
   - How to handle cases where MAPE is unstable (values near zero)

4. FAIRNESS RULES
   - Parameter optimisation rules (same optimisation allowed for all methods, or fixed params?)
   - How to treat methods that fail to converge
   - How to ensure the comparison is not biased towards a particular method

5. REPORTING STANDARD
   - What to include in the comparison table
   - How to communicate uncertainty in the rankings
   - What conclusion is valid from this comparison and what is not

Produce the test harness as a one-page specification document suitable for inclusion
in a methods note.
```

### Sub-task c3: AI Interprets the Results

Once the comparison script has run and produced results, AI drafts the interpretation. This applies the **Report Writer** pattern directly.

#### Prompt Recipe — Comparison Results Interpreter

```
You are an expert forecasting analyst writing up the results of a method comparison study.

I will provide a results table from an accuracy comparison. Your job is to:
1. Identify the best-performing method(s) overall and explain why.
2. Identify whether any simple benchmark (e.g., seasonal naive) is competitive.
3. Note any methods that performed surprisingly well or poorly.
4. State which method you recommend for this series and context, with justification.
5. State the limitations of this comparison and what it does NOT tell us.

Rules:
- Do not overstate the certainty of rankings from a single test series.
- Flag if results are very close between methods (within measurement noise).
- Write in plain English for a government analyst audience.
- Maximum 400 words.

---
RESULTS TABLE:
[PASTE OUTPUT FROM compare_methods.py HERE]

SERIES DESCRIPTION:
[DESCRIBE THE SERIES — e.g., "Monthly A&E attendances, 72 observations, strong seasonality, upward trend, COVID disruption in months 16–24"]

CONTEXT:
[DESCRIBE THE USE CASE — e.g., "Forecast used for capacity planning, 12-month horizon, published quarterly"]
---

Write the interpretation now.
```

---

## End-to-End Workflow: Challenge 7 Doing Challenge 4

```
┌─────────────────────────────────────────────────────────────────┐
│  CHALLENGE 4 TASK                  CHALLENGE 7 AI TOOL          │
├─────────────────────────────────────────────────────────────────┤
│  (a) Collate solutions             Forecasting Solutions         │
│      → reviewed catalogue         Researcher prompt             │
│                                   [ChatGPT / Gemini]            │
├─────────────────────────────────────────────────────────────────┤
│  (b) Build Excel tool              Excel Tool Architect prompt   │
│      → WMC_Forecasting_Tool.xlsx  [Copilot / ChatGPT]           │
│      → Instructions sheet         Instructions Writer prompt     │
│                                   [Claude]                       │
├─────────────────────────────────────────────────────────────────┤
│  (c) Compare solutions             Comparison Script Generator   │
│      → compare_methods.py         [Copilot]                     │
│      → Test harness spec          Test Harness Designer          │
│                                   [Claude]                       │
│      → Results write-up           Results Interpreter prompt     │
│                                   [Claude / ChatGPT]             │
└─────────────────────────────────────────────────────────────────┘
```

**Human time estimate with AI assistance:**
- Task (a): ~1 hour (30 min AI + 30 min human verification)
- Task (b): ~2 hours (45 min AI + 75 min human review and testing)
- Task (c): ~2 hours (60 min AI + 60 min human validation and write-up)
- **Total: ~5 hours vs ~3–5 days unaided**

---

## Human Sign-Off Gates (Challenge 4 specific)

| Gate | What to check |
|---|---|
| Catalogue verification | All GitHub URLs resolve; star counts and licence correct |
| Excel tool QA | All formulas return sensible numbers on sample data; accuracy metrics verified by hand for 2–3 rows |
| Comparison script QA | Method implementations match statsmodels documentation; no data leakage in train/test split |
| Results interpretation | AI conclusion consistent with the numbers; limitations section not softened |

---

> The prompt recipes above are ready to run. The code deliverables they generate are in `../challenge4/`.
