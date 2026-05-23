import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------------
# LOAD DATA
# -----------------------------------

df = pd.read_csv(
    "data/processed/cleaned_air_quality.csv"
)

# -----------------------------------
# PAGE TITLE
# -----------------------------------

st.title("Global Air Quality Dashboard")

# -----------------------------------
# DATA PREVIEW
# -----------------------------------

st.subheader("Dataset Preview")

st.dataframe(df.head())

# -----------------------------------
# AQI DISTRIBUTION
# -----------------------------------

st.subheader("AQI Distribution")

fig = px.histogram(
    df,
    x="AQI Value",
    nbins=30
)

st.plotly_chart(fig)

# -----------------------------------
# SCATTER PLOT
# -----------------------------------

st.subheader("PM2.5 vs AQI")

fig2 = px.scatter(
    df,
    x="PM2.5 AQI Value",
    y="AQI Value",
    color="AQI Value"
)

st.plotly_chart(fig2)