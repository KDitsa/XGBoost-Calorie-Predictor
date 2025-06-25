import pandas as pd
import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Calorie Burn Predictor", layout="centered")
st.title("Calorie Burn Predictor")
st.markdown("Estimate the number of calories burned based on your physical data and activity session.")

st.subheader("Personal Information")
# Gender Input
status = st.radio("Select Gender:",('Male','Female'))
if(status=='Male'):
    Gender = 0
else:
    Gender = 1

# Age
Age = st.number_input("Age(in years)",min_value=1, max_value=120)

st.subheader("Body Metrics")
col1,col2 = st.columns(2)
with col1:
    # Weight
    weight_unit = st.selectbox("Weight Unit", ["kg", "lb"])
    weight_input = st.number_input(f"Weight ({weight_unit})", min_value=1.0, value=70.0)
    Weight = weight_input if weight_unit == "kg" else round(weight_input * 0.453592, 2)
with col2:
    height_unit = st.selectbox("Height Unit", ["cm", "ft/in"])
    if height_unit == "cm":
        Height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=170.0)
    else:
        feet = st.number_input("Feet", min_value=1, max_value=8, value=5)
        inches = st.number_input("Inches", min_value=0, max_value=11, value=7)
        Height = round((feet * 30.48) + (inches * 2.54), 2)

st.subheader("Activity Details")
col3, col4 = st.columns(2)
with col3:
    Duration = st.number_input("Duration (minutes)", min_value=1.0, max_value=300.0, value=30.0)
    Heart_rate = st.number_input("Heart Rate (bpm)", min_value=40.0, max_value=200.0, value=100.0)
with col4:
    temp_unit = st.selectbox("Body Temperature Unit", ["Celsius (°C)", "Fahrenheit (°F)"])
    temp_input = st.number_input(f"Body Temperature ({temp_unit})", min_value=30.0, max_value=110.0, value=98.6)
    Body_temp = temp_input if temp_unit == "Celsius (°C)" else round((temp_input - 32) * 5/9, 2)

def features():
    feature = pd.DataFrame(
        {
            "Gender": Gender,
            "Age": Age,
            "Height": Height,
            "Weight": Weight,
            "Duration": Duration,
            "Heart_Rate": Heart_rate,
            "Body_Temp": Body_temp,
        }, index=[0])
    return feature

df = features()
model = pickle.load(open("prediction.pkl","rb"))
prediction_val = model.predict(df)[0]
if st.button("Predict"):
    st.success(f"Estimated Calories Burned: {prediction_val:.2f} kcal")