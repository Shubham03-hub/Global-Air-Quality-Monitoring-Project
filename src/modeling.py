import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

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
# CREATE MODEL
# -----------------------------------

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# -----------------------------------
# TRAIN MODEL
# -----------------------------------

model.fit(X_train, y_train)

# -----------------------------------
# SAVE MODEL
# -----------------------------------

joblib.dump(
    model,
    "models/aqi_model.pkl"
)

print("\nMODEL TRAINED SUCCESSFULLY")