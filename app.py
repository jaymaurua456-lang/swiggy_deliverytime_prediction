import streamlit as st
import pandas as pd
import numpy as np

# 1. App ka Title (Heading)
st.title("🍔 Swiggy Food Delivery Time Predictor")
st.write("Apne delivery details daalein aur live prediction dekhein.")

# 2. User se Inputs lena (Sliders aur Dropdowns)
st.subheader("Delivery Details Enter Karein:")

distance = st.slider("Distance (km)", min_value=1.0, max_value=30.0, value=5.0, step=0.1)
weather = st.selectbox("Weather Condition", ["Clear", "Windy", "Foggy", "Rainy", "Snowy"])
traffic = st.selectbox("Traffic Level", ["Low", "Medium", "High"])
time_of_day = st.selectbox("Time of Day", ["Morning", "Afternoon", "Evening", "Night"])
vehicle = st.selectbox("Vehicle Type", ["Scooter", "Bike", "Car"])

# 3. Input Data ko DataFrame mein convert karna (Jaise aapne notebook mein kiya tha)
input_data = pd.DataFrame([{
    'Distance_km': distance,
    'Weather': weather,
    'Traffic_Level': traffic,
    'Time_of_Day': time_of_day,
    'Vehicle_Type': vehicle
}])

# Aapka input screen par dikhane ke liye
st.write("### Aapke Inputs:", input_data)

# 4. Prediction Logic (Aapke model ke logic par based ek dummy calculation)
# Note: Real deployment ke liye hum pickle file use karte hain, abhi test karne ke liye yeh rule laga rahe hain:
base_time = 15 + (distance * 2.5)
if traffic == "High": base_time += 12
elif traffic == "Medium": base_time += 6
if weather == "Rainy": base_time += 10

# 5. Output Screen par display karna
st.success(f"⏳ Estimated Delivery Time: {round(base_time, 2)} Minutes")