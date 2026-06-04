import streamlit as st
import pandas as pd
import numpy as np

# App Title
st.title("🍔 Swiggy Food Delivery Time Predictor")
st.write("Apne delivery details daalein aur live prediction dekhein.")

st.subheader("Delivery Details Enter Karein:")

# Input Elements
distance = st.slider("Distance (km)", min_value=0.5, max_value=25.0, value=5.0, step=0.1)
weather = st.selectbox("Weather Condition", ["Clear", "Windy", "Foggy", "Rainy", "Snowy"])
traffic = st.selectbox("Traffic Level", ["Low", "Medium", "High"])
time_of_day = st.selectbox("Time of Day", ["Morning", "Afternoon", "Evening", "Night"])
vehicle = st.selectbox("Vehicle Type", ["Scooter", "Bike", "Car"])

# Making Input DataFrame
input_data = pd.DataFrame([{
    'Distance_km': distance,
    'Weather': weather,
    'Traffic_Level': traffic,
    'Time_of_Day': time_of_day,
    'Vehicle_Type': vehicle
}])

st.write("### Aapke Inputs:", input_data)

# Prediction Logic based on model observations
base_time = 15 + (distance * 2.5)
if traffic == "High": base_time += 12
elif traffic == "Medium": base_time += 6
if weather == "Rainy" or weather == "Foggy": base_time += 10

st.success(f"⏳ Estimated Delivery Time: {round(base_time, 2)} Minutes")
