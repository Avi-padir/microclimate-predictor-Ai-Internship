
import streamlit as st
import numpy as np
import joblib

# Load your trained model
model = joblib.load("best_model.pkl")

st.title("Microclimate Predictor 🌦️")

# Input fields
temperature = st.number_input("Temperature (°C)")
humidity = st.number_input("Humidity (%)")
wind_speed = st.number_input("Wind Speed (km/h)")

# Prediction
if st.button("Predict"):
    input_data = np.array([[temperature, humidity, wind_speed]])
    prediction = model.predict(input_data)
    st.success(f"Predicted value: {prediction[0]:.2f}")
