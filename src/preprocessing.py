import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

# -----------------------------------
# LOAD DATASET
# -----------------------------------

df = pd.read_csv("data/raw/air_quality.csv")

# -----------------------------------
# BASIC INFO
# -----------------------------------

print("\nDATASET INFO:\n")
print(df.info())

print("\nMISSING VALUES:\n")
print(df.isnull().sum())

# -----------------------------------
# REMOVE DUPLICATES
# -----------------------------------

df = df.drop_duplicates()

# -----------------------------------
# HANDLE MISSING VALUES
# -----------------------------------

df["Country"] = df["Country"].fillna("Unknown")

df["City"] = df["City"].fillna("Unknown")

# -----------------------------------
# FEATURE ENGINEERING
# -----------------------------------

df["Pollution_Level"] = df["AQI Value"].apply(
    lambda x: "High" if x > 150 else "Low"
)

# -----------------------------------
# LABEL ENCODING
# -----------------------------------

encoder = LabelEncoder()

df["Country"] = encoder.fit_transform(df["Country"])

df["City"] = encoder.fit_transform(df["City"])

df["AQI Category"] = encoder.fit_transform(
    df["AQI Category"]
)

# -----------------------------------
# FEATURE SCALING
# -----------------------------------

scaler = StandardScaler()

numerical_columns = [
    "CO AQI Value",
    "Ozone AQI Value",
    "NO2 AQI Value",
    "PM2.5 AQI Value"
]

df[numerical_columns] = scaler.fit_transform(
    df[numerical_columns]
)

# -----------------------------------
# SAVE CLEANED DATA
# -----------------------------------

df.to_csv(
    "data/processed/cleaned_air_quality.csv",
    index=False
)

print("\nPREPROCESSING COMPLETED SUCCESSFULLY")