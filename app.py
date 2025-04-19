# imports
import streamlit as st
import pandas as pd

# title for bmi calculator
st.title("💪🧮 BMI Calculator")

# Slider for initial selection
st.subheader("Adjust using slider or type manually 👇")

slider_height = st.slider("Select your height (in cm):", 100, 250, 175)
slider_weight = st.slider("Select your weight (in kg):", 40, 200, 70)

# Manual override (user can type value)
height = st.number_input("Or manually enter height (in cm):", min_value=100, max_value=250, value=slider_height)
weight = st.number_input("Or manually enter weight (in kg):", min_value=40, max_value=200, value=slider_weight)

# Calculate BMI
bmi = weight / ((height / 100) **2)

# show BMI
st.markdown(f"Your BMI is: <span style='color:blue; font-size:20px; font-weight:bold;'>{bmi:.2f}</span>", unsafe_allow_html=True)

# BMI categories
st.write("***⭐✨💥BMI CATEGORIES💥✨⭐***")
st.write("===================================")
st.write("- Underweight: BMI less than 18.5")
st.write("- Normal weight: BMI of 18.5 to 24.9")
st.write("- Overweight: BMI of 25 to 29.9")
st.write("- Obesity: BMI of 30 or higher")