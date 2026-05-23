import pandas as pd
import joblib

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from sklearn.model_selection import train_test_split

# -----------------------------------
# LOAD CLEANED DATA
# -----------------------------------

df = pd.read_csv(
    "data/processed/cleaned_air_quality.csv"
)

# -----------------------------------
# FEATURES & TARGET
# -----------------------------------

X = df[[
    "CO AQI Value",
    "Ozone AQI Value",
    "NO2 AQI Value",
    "PM2.5 AQI Value"
]]

y = df["AQI Value"]

# -----------------------------------
# TRAIN TEST SPLIT
# -----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------------
# LOAD MODEL
# -----------------------------------

model = joblib.load(
    "models/aqi_model.pkl"
)

# -----------------------------------
# PREDICTIONS
# -----------------------------------

predictions = model.predict(X_test)

# -----------------------------------
# EVALUATION
# -----------------------------------

mae = mean_absolute_error(
    y_test,
    predictions
)

rmse = mean_squared_error(
    y_test,
    predictions
) ** 0.5

r2 = r2_score(
    y_test,
    predictions
)

print("\nMODEL EVALUATION RESULTS\n")

print("MAE:", mae)

print("RMSE:", rmse)

print("R2 SCORE:", r2)