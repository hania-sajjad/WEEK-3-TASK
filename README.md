# WEEK-3-TASK
Dimensionality Reduction and FastAPI Dashboard

# ⚡ Steel Industry Energy Consumption Prediction using PCA and FastAPI

## Project Overview

This project predicts industrial energy consumption (`Usage_kWh`) using Machine Learning. The dataset was preprocessed, engineered, and reduced using Principal Component Analysis (PCA). A Random Forest Regression model was trained and deployed using FastAPI with an interactive web interface for real-time predictions.

This project was completed as **Week 3 Internship Task** at **ITSimplers Institute**.

---

## Objectives

- Perform dimensionality reduction using PCA.
- Compare model performance before and after PCA.
- Save the trained ML pipeline.
- Deploy the model using FastAPI.
- Build a dashboard for data visualization.
- Predict energy consumption through a web interface.

---

## Project Structure

```
WEEK-3-TASK/
│
├── data/
│   └── steel_energy_engineered.csv
│
├── notebooks/
│   └── week3_pca.ipynb
│
├── static/
│   ├── correlation_heatmap.png
│   ├── energy_by_hour.png
│   └── load_type_distribution.png
│
├── templates/
│   ├── home.html
│   ├── dashboard.html
│   └── predict.html
│
├── model.joblib
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Dataset

**Dataset:** Steel Industry Energy Consumption Dataset

The dataset contains industrial energy usage records along with electrical measurements and operational information.
Basically the Engineered Version of Dataset from Week 2.

### Target Variable

- `Usage_kWh`

### Features

- Lagging Reactive Power
- Leading Reactive Power
- CO₂ Emissions
- Power Factors
- NSM
- Hour
- Month
- Week Status
- Day of Week
- Load Type
- Engineered Features
- One-Hot Encoded Variables

---

## Machine Learning Pipeline

1. Data Loading
2. Train-Test Split
3. Feature Scaling using StandardScaler
4. Principal Component Analysis (PCA)
5. Random Forest Regression
6. Model Evaluation
7. Save Pipeline using Joblib

---

## PCA

Principal Component Analysis was applied to reduce dimensionality while preserving most of the information contained in the original features.

The notebook includes:

- Scree Plot
- Cumulative Explained Variance Plot
- PCA Loading Heatmap
- Model Comparison

---

## FastAPI Web Application

The application includes three pages:

### Home

- Project overview
- Navigation menu
- Model information

### Dashboard

Displays:

- Average Energy Consumption by Hour
- Load Type Distribution
- Correlation Heatmap

### Prediction

Users can enter feature values through a web form to predict industrial energy consumption in real time.

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- FastAPI
- Jinja2
- Joblib
- HTML
- CSS

---

## Running the Project

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start the FastAPI server

```bash
uvicorn main:app --reload
```

Open your browser and visit:

```
http://127.0.0.1:8000
```

---

## Future Improvements

- Improve UI with Bootstrap
- Add interactive charts
- Deploy online using Render or Railway
- Add input validation
- Support batch predictions

---

## Author

**Hania Sajjad**

AI/ML Internship Task – Week 3

---
