# ⛈️ Machine Learning Thunderstorm Forecasting with MLflow Tracking

[![Streamlit App](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://mlthunderstormforecasting-y8dd5ryqjj7zepxvapksmd.streamlit.app/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)](https://mlflow.org/)

A modern Machine Learning system designed to predict the likelihood of thunderstorm occurrences based on key atmospheric stability indices and profiles. The project incorporates experiment tracking with **MLflow**, a scalable **FastAPI** backend, and a responsive **Streamlit** user interface.

🚀 **Live Streamlit App:** [mlthunderstormforecasting-y8dd5ryqjj7zepxvapksmd.streamlit.app](https://mlthunderstormforecasting-y8dd5ryqjj7zepxvapksmd.streamlit.app/)

---

## 📌 Features

- **High-Performance Prediction**: Powered by a finely-tuned **Random Forest Classifier** selected after comprehensive experimentation.
- **Microservice Architecture**: Decoupled FastAPI backend acting as the prediction engine and a Streamlit frontend interface.
- **Production Standalone Mode**: Includes a self-contained Streamlit deployment script (`app.py`) for hosting on platforms like Streamlit Cloud.
- **Experiment Tracking**: Full lifecycle tracking of parameters, metrics, and model artifacts using MLflow.

---

## 🛠️ Tech Stack & Libraries

- **Machine Learning**: `scikit-learn`, `xgboost`, `imbalanced-learn` (for handling class imbalance)
- **Data Manipulation & Visuals**: `pandas`, `numpy`, `matplotlib`, `seaborn`
- **Experiment Tracking**: `mlflow`
- **API Engine**: `fastapi`, `uvicorn`, `pydantic`
- **Frontend App**: `streamlit`
- **Server Deployment**: `gunicorn`

---

## 📊 Atmospheric Features Used for Prediction

The forecasting model utilizes critical meteorological indices and profile indicators:

| Feature Name | Description |
| :--- | :--- |
| **SWEAT Index** | Severe Weather Threat Index – evaluates convective potential by combining wind shear and thermal instability. |
| **K Index** | Measures thunderstorm potential based on vertical temperature lapse rate, moisture content, and vertical extent of moisture. |
| **Totals Totals Index (TT)** | Combines the Static Energy Index and the Vertical Totals Index to evaluate static stability and moisture. |
| **Environmental Stability** | A cumulative measure of general tropospheric static stability indicators. |
| **Moisture Indices** | Indicators reflecting low-level atmospheric humidity levels. |
| **Convective Potential** | Indices reflecting potential buoyant energy (e.g., CAPE approximations). |
| **Temperature Pressure** | Correlated variables modeling temperature-pressure profile gradients. |
| **Moisture-Temperature Profiles** | Vertical profile metrics combining thermal and humidity gradients. |

---

## 📂 Project Structure

```directory
├── api/
│   └── main.py                     # FastAPI backend application
├── app/
│   ├── __init__.py
│   ├── config.py                   # App configurations
│   ├── model_loader.py             # Utility to load the model
│   ├── predictor.py                # Core prediction logic
│   └── schemas.py                  # Pydantic data schemas
├── streamlit_app/
│   └── ui.py                       # Streamlit UI calling FastAPI backend
├── models/
│   └── Random_Forest_best_model.pkl# Best-performing serialized model
├── exp/
│   ├── experiment.ipynb            # Jupyter Notebook for experimental runs
│   ├── experiments.ipynb           # Model comparison and MLflow logging
│   └── mlflow.db                   # Local MLflow SQLite Database
├── app.py                          # Standalone Streamlit deployment script (for Streamlit Cloud)
├── requirements.txt                # Deployment dependency configuration
├── local-requirements.txt          # Local setup requirements
└── README.md                       # Project documentation (this file)
```

---

## ⚙️ Setup & Installation

### Prerequisites
Make sure you have **Python 3.10+** installed. 

### 1. Clone the Repository
```bash
git clone https://github.com/SusmitCr7/ml_thunderstorm_forecasting.git
cd ml_thunderstorm_forecasting
```

### 2. Setup Virtual Environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Application

This repository supports two modes of execution: **Microservice Mode** (decoupled API & UI) and **Standalone Mode** (single script deployment).

### Option A: Standalone Streamlit App (Recommended for Simple Run)
Run the self-contained Streamlit application that directly loads the model:
```bash
streamlit run app.py
```

### Option B: Microservice Architecture (FastAPI Backend + Streamlit UI)

1. **Start the FastAPI Backend**:
   ```bash
   uvicorn api.main:app --host 127.0.0.1 --port 8000 --reload
   ```
   *Access the interactive API documentation at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)*

2. **Start the Streamlit Frontend**:
   In a new terminal window, activate your virtual environment and run:
   ```bash
   streamlit run streamlit_app/ui.py
   ```
   *Access the web client at: [http://localhost:8501](http://localhost:8501)*

---

## 📈 Experiment Tracking (MLflow)

Model experiments, hyperparameter tuning, and metrics were tracked using **MLflow**. 

To run your own experiments or review logging:
1. Open the Jupyter notebooks under the `exp/` folder.
2. Initialize and run the MLflow tracking server locally:
   ```bash
   mlflow server --backend-store-uri sqlite:///exp/mlflow.db --default-artifact-root ./mlruns
   ```
3. Open [http://localhost:5000](http://localhost:5000) in your browser to inspect runs, parameters, metrics, and models.

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
