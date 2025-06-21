import pandas as pd
import streamlit as st
import pickle
import numpy as np
st.header("Calories Burnt Prediction")
col1,col2 = st.columns(2)
status = st.radio("Select Gender:",('Male','Female'))
if(status=='Male'):
    Gender = 0
else:
    Gender = 1
with col1:
    Age = st.number_input("Age")
with col2:
    Height = st.number_input("Height(cms)")
with col1:
    Weight = st.number_input("Weight(kgs)")
with col2:
    Duration = st.number_input("Duration(mins)")
with col1:
    Heart_rate = st.number_input("Heart Rate")
with col2:
    Body_temp = st.number_input("Body Temmperature")

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
prediction_val = model.predict(df)
if st.button("Predict"):
    st.text("Calories you burnt: {}".format(prediction_val[0]))
