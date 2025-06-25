# XGBoost-Calorie-Predictor
## 📘 Overview
XGBoost-Calorie-Predictor is a **machine learning project** developed in *August 2024* that **estimates calorie expenditure** based on user input data. Leveraging an **XGBoost regression model** trained on a **Kaggle dataset**, the system features end-to-end functionality from data processing and model training to serialization and deployment within an **interactive Streamlit web application** for real-time predictions.

## 🎯 Motivation
Accurate calorie prediction is essential for fitness tracking, diet planning, and health monitoring. This project demonstrates a practical pipeline for training, saving, and deploying a calorie prediction model, making calorie estimation accessible and user-friendly through a web interface.

## 💡 Features
- 🔥 Predicts calories burnt from user input
- 🚀 Model trained using **XGBoost Regressor**
- 🎯 Root Mean Squared Error (RMSE): **4.26**
- ⚡ **Streamlit UI** for interactive predictions
- 💾 Pickle used for saving and loading the trained model

## ⚙️ Getting Started

This project requires Python and some common data science libraries. Setup is straightforward with a requirements.txt to install all dependencies.

### ✅ Requirements

- **Python 3.8+**
- Libraries listed in **requirement.txt**

[->install python](https://www.python.org/downloads/)

### 🚀 Running the System

```bash
# Clone the repository
git clone https://github.com/KDitsa/XGBoost-Calorie-Predictor.git
cd XGBoost-Calorie-Predictor

# (Optional) Create and activate a virtual environment
python -m venv <your_environment_name>
<your_environment_name>\Scripts\activate # For Windows

# Install dependencies
pip install -r requirement.txt

# Run the Streamlit app
streamlit run app.py
```

Once running, the app will open in your browser at http://localhost:8501, where you can input your data and get calorie predictions instantly.

## 🛠️ Implementation Journey

### 1. 📊 Data Preparation and Model Training

The model was trained using two CSV files:
- **Exercise data**: Contains user information and exercise metrics including `User_ID`, `Gender`, `Age`, `Height`, `Weight`, `Duration`, `Heart_Rate`, and `Body_Temp`.
- **Calories data**: Contains `User_ID` and corresponding `Calories` expenditure.

These datasets were merged on User_ID to create a complete training set. The pipeline involved data cleaning, exploratory data analysis with correlation checks, splitting the merged data into training and testing sets, and training an XGBoost regressor to optimize prediction accuracy.

---

### 🏋️ Model Performance
The final model achieved a **Root Mean Squared Error (RMSE)** of **4.26**, indicating strong predictive accuracy for calorie estimation.

---

### 2. 💾 Model Serialization with Pickle
The trained XGBoost model is saved using Python’s `pickle` module, allowing quick loading of the model for inference without retraining.

---

### 3. 🖥️ Interactive UI with Streamlit
The Streamlit app provides a simple, user-friendly interface to input data such as age, weight, height, activity type, and duration, returning real-time calorie predictions based on the model.

---

## 🔮 Future Improvements
- Expand dataset diversity and volume for improved model generalization.
- Deploy as a cloud-hosted web service with authentication and user management.
- Enhance UI with visualization of user calorie trends and goal tracking.
- Explore deep learning models for improved prediction accuracy.

## 📝 Closing Thoughts
This project highlights the end-to-end workflow for building and deploying a machine learning model in a practical, accessible way. By leveraging XGBoost for prediction accuracy, Pickle for model persistence, and Streamlit for UI simplicity, it offers a solid foundation for calorie prediction applications and health tech innovations.
