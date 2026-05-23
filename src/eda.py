import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv(
    "data/processed/cleaned_air_quality.csv"
)

# Statistical summary
print(df.describe())

# Correlation matrix
corr = df.corr(numeric_only=True)

plt.figure(figsize=(12, 8))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Matrix")

plt.show()

# AQI distribution
plt.figure(figsize=(10, 5))

sns.histplot(
    df["AQI Value"],
    bins=30
)

plt.title("AQI Distribution")

plt.show()