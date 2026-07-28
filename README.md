# ⛏️ Mining Quality Prediction System

## AI-Based Silica Concentrate Prediction Using CatBoost Regression

An end-to-end Machine Learning project that predicts **% Silica Concentrate** in an iron ore flotation plant using industrial sensor data and an optimized **CatBoost Regression Model**.

This project demonstrates a complete Machine Learning pipeline including:

- Data preprocessing
- Exploratory Data Analysis
- Feature Engineering
- Model training and comparison
- CatBoost optimization
- FastAPI backend development
- Streamlit interactive dashboard
- Cloud deployment


---

# 🚀 Live Deployment

## 📊 Streamlit Dashboard

Live Application:

```
https://your-streamlit-app-url.streamlit.app
```


## ⚡ FastAPI Backend

API URL:

```
https://mining-quality-prediction.onrender.com
```


## 📚 API Documentation

Swagger Documentation:

```
https://mining-quality-prediction.onrender.com/docs
```


---

# 📌 Project Overview

In mining industries, maintaining the quality of iron ore concentrate is a critical challenge.

The percentage of **Silica Concentrate** is one of the important quality indicators that affects the final product quality.

This project uses historical flotation plant sensor data to build a Machine Learning model that predicts silica concentrate values based on different process parameters.

The deployed system allows users to:

1. Upload mining sensor CSV data
2. Process input features
3. Generate silica concentrate predictions
4. Visualize process parameters
5. Analyze prediction results through an interactive dashboard


---

# 🎯 Objective

The objective of this project is:

> To develop an AI-powered prediction system that can estimate % Silica Concentrate using machine learning techniques and provide an interactive dashboard for industrial analysis.


---

# 🏗️ System Architecture


```
                 User
                   |
                   |
                   ↓

        Streamlit Dashboard

                   |
                   |
                   ↓

          FastAPI Backend

                   |
                   |
                   ↓

       Feature Engineering Pipeline

                   |
                   |
                   ↓

        Optimized CatBoost Model

                   |
                   |
                   ↓

       Silica Concentrate Prediction

```


---

# ✨ Features


## 🤖 Machine Learning Features

- Data cleaning and preprocessing
- Exploratory Data Analysis
- Feature engineering
- Time-based feature creation
- Rolling statistical features
- Multiple ML model comparison
- CatBoost hyperparameter optimization
- Feature importance analysis


---

## 📊 Dashboard Features

The Streamlit dashboard provides:


### 📂 CSV Upload

- Upload mining sensor CSV files
- Automatically analyze uploaded data


### 📈 Dataset Overview

Displays:

- Total records
- Number of features
- Missing values


### 🔮 Prediction

Generates:

- Predicted Silica Concentrate value
- Model information
- Prediction summary


### 📊 Data Visualization

Includes:

- Historical silica concentrate trend
- Mining process parameter analysis
- Actual vs Predicted comparison
- Statistical summary


---

# 🤖 Machine Learning Model


## Final Selected Model

### Optimized CatBoost Regression


CatBoost was selected because:

- It handles complex nonlinear relationships
- It performs well on industrial datasets
- It captures feature interactions effectively
- It requires minimal preprocessing


---

# 📂 Dataset Information


Dataset Used:

**Mining Process Flotation Plant Database**


The dataset contains:

- Process sensor measurements
- Chemical parameters
- Flotation plant variables
- Silica concentrate values


Target Variable:

```
% Silica Concentrate
```


Important Input Features:

- % Iron Feed
- % Silica Feed
- Starch Flow
- Amina Flow
- Ore Pulp pH
- Ore Pulp Density
- Process sensor measurements


---

# 🛠️ Technologies Used


## Programming Language

- Python


## Machine Learning

- CatBoost
- Scikit-learn
- Pandas
- NumPy


## Data Visualization

- Plotly
- Streamlit


## Backend

- FastAPI
- Uvicorn


## Deployment

- Render
- Streamlit Cloud


## Version Control

- Git
- GitHub


---

# 📂 Project Structure


```
Mining-Quality-Prediction/

│
├── api/
│   ├── main.py
│   ├── predict.py
│   └── schemas.py
│
├── app/
│   └── app.py
│
├── models/
│   ├── feature_columns.pkl
│   ├── feature_names.pkl
│   └── final_optimized_catboost_model.cbm
│
├── src/
│   ├── feature_engineering.py
│   ├── predictor.py
│   └── utils.py
│
├── notebook/
│   └── Mining_Quality_Prediction.ipynb
│
├── data/
│
├── results/
│
├── requirements.txt
│
├── .gitignore
│
└── README.md

```


---

# ⚙️ Installation & Setup


## Clone Repository


```bash
git clone https://github.com/Tamanna7574/Mining-Quality-Prediction.git
```


Move into project directory:


```bash
cd Mining-Quality-Prediction
```


---

# 📦 Install Dependencies


```bash
pip install -r requirements.txt
```


---

# ▶️ Run Application Locally


## Start FastAPI Backend


```bash
uvicorn api.main:app --reload
```


Backend will run:

```
http://127.0.0.1:8000
```


API Documentation:

```
http://127.0.0.1:8000/docs
```


---

## Start Streamlit Dashboard


Open another terminal:


```bash
streamlit run app/app.py
```


Dashboard:

```
http://localhost:8501
```


---

# 🔌 API Usage


## Prediction Endpoint


```
POST /predict
```


Example Response:


```json
{
    "prediction": 2.412,
    "unit": "%",
    "target": "% Silica Concentrate",
    "model": "Optimized CatBoost + Time Features"
}
```


---

# 📈 Model Evaluation


The project includes:

- Model comparison
- Prediction analysis
- Feature importance
- SHAP interpretation


Evaluation metrics:

- MAE
- RMSE
- R² Score


---

# 📊 Results


The final deployed model provides:

✅ Silica concentrate prediction

✅ Fast API inference

✅ Interactive visualization dashboard

✅ End-to-end ML deployment


---

# 🌐 Deployment


## Backend

Platform:

```
Render
```


Technology:

```
FastAPI + Uvicorn
```


---

## Dashboard

Platform:

```
Streamlit Cloud
```


Technology:

```
Streamlit
```


---

# 🔮 Future Improvements


Future enhancements:

- Real-time sensor data integration
- Automated model retraining
- Database integration
- IoT sensor connectivity
- MLOps pipeline implementation
- Real-time monitoring dashboard


---

# 👩‍💻 Author


## Tamanna

B.Tech Computer Science Engineering


GitHub:

```
https://github.com/Tamanna7574
```


---

# ⭐ Acknowledgement


This project helped in applying practical concepts of:

- Machine Learning
- Data Analytics
- Industrial AI
- Backend Development
- Model Deployment


If you find this project useful, consider giving it a ⭐ on GitHub.