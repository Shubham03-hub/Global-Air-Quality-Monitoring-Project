import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/air_quality.csv")

# Display first rows
print("\nFIRST 5 ROWS:\n")
print(df.head())

# Display dataset information
print("\nDATASET INFO:\n")
print(df.info())

# Display column names
print("\nCOLUMN NAMES:\n")
print(df.columns)