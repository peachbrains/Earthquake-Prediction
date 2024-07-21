import streamlit as st
import numpy as np
import joblib

# Load your trained model (ensure the path is correct)
model_path = 'C:\\Users\\user\\Desktop\\Earthquake prediction project\\Model\model.pkl'
model = joblib.load(model_path)

st.title("Earthquake Prone Prediction")

st.write("""
         Enter the longitude and latitude of your location to check if it is earthquake prone.
         The prediction scale is from 1 to 10, where 10 indicates highly earthquake prone.
         """)

longitude = st.number_input("Longitude", min_value=-180.0, max_value=180.0, value=0.0)
latitude = st.number_input("Latitude", min_value=-90.0, max_value=90.0, value=0.0)

if st.button("Predict"):
    user_input = np.array([[longitude, latitude]])
    prediction = model.predict(user_input)
    st.write(f"The location with longitude {longitude} and latitude {latitude} is predicted to be earthquake prone on a scale of 1 to 10: {prediction[0]:.2f}")
