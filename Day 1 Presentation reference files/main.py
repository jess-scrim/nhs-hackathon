import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load data
df = pd.read_csv("training_dataset.csv")

# Convert target to numeric (continuous regression target).
y = pd.to_numeric(df["value"], errors="coerce")

# Use discrete predictors and engineer date parts for a stronger baseline model.
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month

feature_cols = ["description", "geography", "sex", "age", "source_file", "year", "month"]
X = pd.get_dummies(df[feature_cols].astype(str), dummy_na=True)

# Keep only rows with a valid target/date.
valid_rows = y.notna() & df["date"].notna()
X = X.loc[valid_rows]
y = y.loc[valid_rows]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)
print("MAE:", mean_absolute_error(y_test, preds))
