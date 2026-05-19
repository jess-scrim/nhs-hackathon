import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load and sort chronologically (critical for time series — prevents future leakage)
df = pd.read_csv("training_dataset.csv")
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["value"] = pd.to_numeric(df["value"], errors="coerce")
df = df.dropna(subset=["date", "value"]).sort_values("date").reset_index(drop=True)

# Date-part features
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month

# Lag features per group (description + geography + sex + age) — strongest predictors for time series
group_cols = ["description", "geography", "sex", "age"]
df = df.sort_values(group_cols + ["date"]).reset_index(drop=True)
for lag in [1, 2, 3, 6, 12]:
    df[f"lag_{lag}"] = df.groupby(group_cols)["value"].shift(lag)

# Rolling mean features (3-month and 6-month)
df["rolling_3"] = df.groupby(group_cols)["value"].transform(lambda s: s.shift(1).rolling(3).mean())
df["rolling_6"] = df.groupby(group_cols)["value"].transform(lambda s: s.shift(1).rolling(6).mean())

# Drop rows where any lag/rolling feature is missing (early rows in each group)
df = df.dropna().reset_index(drop=True)

# One-hot encode discrete features
categorical_features = ["description", "geography", "sex", "age", "source_file"]
numeric_features = ["year", "month", "lag_1", "lag_2", "lag_3", "lag_6", "lag_12", "rolling_3", "rolling_6"]

X_cat = pd.get_dummies(df[categorical_features].astype(str), dummy_na=False)
X = pd.concat([df[numeric_features].reset_index(drop=True), X_cat.reset_index(drop=True)], axis=1)
y = df["value"]

# Chronological 80/20 split — no shuffling, preserves time order
split_idx = int(len(df) * 0.8)
X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]

# Model
model = RandomForestRegressor(n_estimators=300, max_features="sqrt", random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# Evaluate — rich metrics for report generation
preds = model.predict(X_test)
mae = mean_absolute_error(y_test, preds)
rmse = np.sqrt(mean_squared_error(y_test, preds))
mape = np.mean(np.abs((y_test.values - preds) / y_test.values)) * 100
r2 = r2_score(y_test, preds)

print(f"MAE:   {mae:.2f}")
print(f"RMSE:  {rmse:.2f}")
print(f"MAPE:  {mape:.2f}%")
print(f"R²:    {r2:.4f}")

# Feature importances (useful context for the report prompt)
importances = pd.Series(model.feature_importances_, index=X.columns)
print("\nTop 10 feature importances:")
print(importances.nlargest(10).to_string())
