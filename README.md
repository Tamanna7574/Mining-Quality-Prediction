# ⛏️ Mining Quality Prediction System

An end-to-end **Machine Learning based Mining Quality Prediction System** that predicts **% Silica Concentrate** in an iron ore flotation plant using advanced regression techniques.

The project uses an **Optimized CatBoost Regression Model with Time-Series Feature Engineering** to analyze mining process parameters and predict silica concentration.

The system includes:

- Data preprocessing pipeline
- Feature engineering
- Machine learning model comparison
- Optimized CatBoost model
- FastAPI prediction API
- Streamlit interactive dashboard
- Data visualization and analysis


---

# 📌 Project Overview

In mining industries, maintaining the quality of iron ore concentrate is a critical task. The silica concentration level directly impacts the final product quality and operational efficiency.

This project develops an AI-based prediction system that can estimate future **Silica Concentrate (%)** using historical mining process data and sensor parameters.

The solution helps industries to:

- Monitor mineral quality
- Improve production efficiency
- Reduce manual analysis
- Enable data-driven decision making


---

# 🎯 Objective

The main objective of this project is:

> To build a Machine Learning model capable of predicting silica concentrate percentage using mining process parameters and time-based features.

### Prediction Target

```
% Silica Concentrate
```


---

# 🏗️ System Architecture


```
                    Mining Sensor Data

                           |
                           ↓

              Data Cleaning & Preprocessing

                           |
                           ↓

              Feature Engineering Pipeline

                           |
                           ↓

          Multiple Machine Learning Models

                           |
                           ↓

          Optimized CatBoost Regression Model

                           |
             -----------------------------
             |                           |
             ↓                           ↓

       FastAPI Backend            Streamlit Dashboard

             |                           |
             ↓                           ↓

    Real-Time Prediction       Visualization & Analytics

```


---

# 📂 Project Structure


```
Mining_Quality_Prediction/

│
├── api/
│   ├── main.py
│   ├── predict.py
│   └── schemas.py
│
├── app/
│   └── app.py
│
├── artifacts/
│   └── Generated training artifacts
│
├── data/
│   └── Mining process datasets
│
├── deployment/
│   └── requirements.txt
│
├── models/
│   ├── final_optimized_catboost_model.cbm
│   ├── feature_columns.pkl
│   ├── feature_names.pkl
│   └── model_metadata.json
│
├── notebook/
│   └── Mining_Quality_Prediction.ipynb
│
├── results/
│   ├── final_predictions.csv
│   ├── future_predictions.csv
│   ├── model_comparison.csv
│   └── shap_feature_importance.csv
│
├── src/
│   ├── predictor.py
│   ├── feature_engineering.py
│   └── utils.py
│
├── .gitignore
│
└── README.md

```


---

# 📊 Dataset Information

The project uses the:

## Mining Process Flotation Plant Database


The dataset contains real-world operational measurements collected from an iron ore flotation plant.


### Input Features Include:

- Iron Feed Percentage
- Silica Feed Percentage
- Starch Flow
- Amine Flow
- Ore Pulp pH
- Ore Pulp Density
- Process Sensor Measurements
- Time-based Features


### Output Target:

```
% Silica Concentrate
```


---

# 🔄 Data Processing Pipeline


## 1. Data Cleaning

Performed preprocessing steps:

- Missing value handling
- Data type correction
- Duplicate removal
- Data consistency checking


---

## 2. Feature Engineering


Created advanced features:

### Time Features

- Hour
- Day
- Month
- Day of Week


### Rolling Statistics

- Rolling Mean
- Rolling Standard Deviation
- Lag Features


These features help the model understand process behavior over time.


---

# 🤖 Machine Learning Models


Multiple regression models were trained and evaluated.


| Model | Algorithm |
|---|---|
| Linear Regression | Regression |
| Random Forest | Ensemble Learning |
| Extra Trees | Ensemble Learning |
| XGBoost | Gradient Boosting |
| LightGBM | Gradient Boosting |
| Artificial Neural Network | Deep Learning |
| CatBoost | Gradient Boosting |


---

# 🏆 Final Model


After model comparison and optimization, the best performing model selected was:


## Optimized CatBoost Regression Model


Model File:

```
final_optimized_catboost_model.cbm
```


### Why CatBoost?

- Excellent performance on tabular datasets
- Handles complex feature relationships
- Robust against overfitting
- Efficient training performance


---

# 📈 Model Evaluation


The models were evaluated using:


### Evaluation Metrics

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score


Model comparison results are available inside:


```
results/
```


---

# 🚀 Application Features


# 1. FastAPI Backend


The project provides a REST API for prediction.


### Endpoint


```
POST /predict
```


### Example Request

```json
[
 {
  "% Iron Feed": 55.2,
  "% Silica Feed": 1.5,
  "Ore Pulp pH": 10.2
 }
]
```


### Example Response


```json
{
    "prediction": 2.412,
    "unit": "%",
    "target": "% Silica Concentrate",
    "model": "Optimized CatBoost + Time Features"
}
```


---

# 2. Streamlit Dashboard


The interactive dashboard provides:


## Dataset Overview

Features:

- CSV upload
- Dataset preview
- Total records
- Number of features
- Missing value analysis


## Prediction

Users can:

- Upload mining sensor CSV
- Run prediction
- View predicted silica concentration


## Visualization


Dashboard includes:

- Silica Concentrate Trend
- Mining Parameter Analysis
- Actual vs Predicted Comparison
- Statistical Summary


---

# 🛠️ Technology Stack


## Programming Language

- Python


## Data Processing

- Pandas
- NumPy


## Machine Learning

- Scikit-learn
- CatBoost
- XGBoost
- LightGBM


## Visualization

- Plotly
- Streamlit


## Backend

- FastAPI
- Uvicorn


## Development Tools

- Jupyter Notebook
- Git
- GitHub


---

# ⚙️ Installation and Setup


## Clone Repository


```bash
git clone https://github.com/Tamanna7574/Mining-Quality-Prediction.git
```


Move into project directory:


```bash
cd Mining-Quality-Prediction
```


---

# Install Dependencies


```bash
pip install -r deployment/requirements.txt
```


---

# ▶️ Run FastAPI Server


Start backend:


```bash
uvicorn api.main:app --reload
```


API URL:


```
http://127.0.0.1:8000
```


Swagger Documentation:


```
http://127.0.0.1:8000/docs
```


---

# ▶️ Run Streamlit Dashboard


Open another terminal:


```bash
streamlit run app/app.py
```


Dashboard URL:


```
http://localhost:8501
```


---

# 📸 Dashboard Preview


Add your dashboard screenshots here:


```
assets/

└── dashboard.png

```


---

# 📁 Model Files


Important trained files:


```
models/

├── final_optimized_catboost_model.cbm
├── feature_columns.pkl
├── feature_names.pkl
└── model_metadata.json

```


---

# 🔮 Future Improvements


Planned improvements:


- Real-time sensor data integration
- Cloud deployment
- Docker deployment
- Automated model retraining
- MLOps pipeline implementation
- Model monitoring system


---

# 👩‍💻 Author


## Tamanna

B.Tech Computer Science Engineering


### Areas of Interest

- Machine Learning
- Data Analytics
- Artificial Intelligence
- Data Visualization
- Software Development


---

# ⭐ Project Highlights


✅ End-to-End Machine Learning Pipeline  
✅ Advanced Time-Series Feature Engineering  
✅ Multiple Model Comparison  
✅ Optimized CatBoost Regression  
✅ FastAPI Deployment  
✅ Streamlit Analytics Dashboard  
✅ Real-Time Prediction Capability  


---

# 📜 License


This project is developed for educational and research purposes.