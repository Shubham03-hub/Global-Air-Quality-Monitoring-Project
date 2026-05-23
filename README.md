# Global Air Quality Monitoring Project

A complete end-to-end Data Science and Machine Learning project focused on analyzing, visualizing, and predicting global air quality using AQI (Air Quality Index) data.

---

# Project Overview

This project demonstrates the full data science workflow, including:

* Data Collection and Cleaning
* Exploratory Data Analysis (EDA)
* AQI Prediction using Machine Learning
* Data Visualization and Insights
* Interactive Dashboard Development with Streamlit

The project helps identify pollution patterns, understand environmental trends, and build predictive models for air quality analysis.

---

# Project Structure

```bash
global-air-quality-project/
│
├── data/
│   ├── raw/
│   │   └── air_quality.csv
│   │
│   └── processed/
│       └── cleaned_air_quality.csv
│
├── models/
│   └── aqi_model.pkl
│
├── screenshots/
│   ├── dataset_preview.png
│   ├── aqi_distribution.png
│   └── PM2.5_vs_AQI.png
│
├── src/
│   ├── data_loading.py
│   ├── preprocessing.py
│   ├── eda.py
│   ├── modeling.py
│   └── evaluation.py
│
├── dashboards/
│   └── app.py
│
├── requirements.txt
└── README.md
```

---

#  Dataset Information

The dataset includes air quality measurements from multiple countries and cities worldwide.

### Key Features

* AQI Value
* PM2.5 AQI Value
* NO2 AQI Value
* Ozone AQI Value
* CO AQI Value
* Country
* City

The dataset is used for pollution analysis, visualization, and AQI prediction modeling.

---

# 🛠 Technologies Used

This project was built using the following technologies and libraries:

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* Scikit-learn
* Streamlit
* Joblib

---

#  Installation Guide

## Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

## Navigate to the Project Folder

```bash
cd global-air-quality-project
```

## Install Required Libraries

```bash
python -m pip install -r requirements.txt
```

---

# Running the Project

## Step 1: Load the Dataset

```bash
python src/data_loading.py
```

## Step 2: Preprocess the Data

```bash
python src/preprocessing.py
```

## Step 3: Perform Exploratory Data Analysis (EDA)

```bash
python src/eda.py
```

## Step 4: Train the Machine Learning Model

```bash
python src/modeling.py
```

## Step 5: Evaluate Model Performance

```bash
python src/evaluation.py
```

## Step 6: Launch the Streamlit Dashboard

```bash
python -m streamlit run dashboards/app.py
```

---

# Model Performance

The machine learning model achieved excellent predictive performance:

| Metric   | Score |
| -------- | ----- |
| MAE      | 0.228 |
| RMSE     | 2.652 |
| R² Score | 0.997 |

---

# Project Screenshots

## Dataset Preview

![Dataset Preview](screenshots/dataset_preview.png)

---

## AQI Distribution Analysis

![AQI Distribution](screenshots/aqi_distribution.png)

---

## 🌫 PM2.5 vs AQI Relationship

![PM2.5 vs AQI](screenshots/PM2.5_vs_AQI.png)

---

# Key Features

* AQI Prediction using Machine Learning
* Air Pollution Analysis
* Interactive Data Visualization
* Streamlit Dashboard
* Automated Data Processing Pipeline
* Model Evaluation and Insights

---

# Future Enhancements

Possible future improvements for the project include:

* Real-Time AQI Monitoring using APIs
* Time Series Forecasting
* Geospatial Pollution Mapping
* Deep Learning-Based Prediction Models
* Cloud Deployment and CI/CD Integration

---

# Author

**Shubham Panchal**
Data Science | Data Analytics | Machine Learning
Focused on building practical, real-world, end-to-end data science projects.

🔗 LinkedIn:
[https://linkedin.com/in/shubham-panchal-a100282a8](https://linkedin.com/in/shubham-panchal-a100282a8)
