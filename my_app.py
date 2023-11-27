

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image  # to deal with images (PIL: Python imaging library)
import subprocess

# Read the requirements.txt file and install packages



header_html = """
    <style>
        .header {
            text-align: center;
            padding: 2rem 0;
            background-color: #355E3B;
            color: white;
            position: relative;
            overflow: hidden;
        }
         .header h1 {
            color: red; /* Change text color to red */
            margin-bottom: 0.5rem; /* Adjust margin as needed */
        }
        .header::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(to right, ##355E3B, #ff9900);
            z-index: -1;
            animation: animateGradient 5s linear infinite;
        }
        @keyframes animateGradient {
            0% {
                background-position: 0% 50%;
            }
            100% {
                background-position: 100% 50%;
            }
        }
    </style>
    <div class="header">
        <h1>Welcome to Car Price Prediction!</h1>
        <p>Choose the car specifications from the sidebar and click 'Predict' below</p>
    </div>
"""

st.markdown(header_html, unsafe_allow_html=True)


# Example sidebar with car specifications
st.sidebar.header('Car Specifications')

# defining variables for user input
hp_kW = st.sidebar.slider("What is the hourse power in KW?", 40000, 294000, step=100)
km = st.sidebar.slider("what is the total KM the car has", 0, 317000, step=1000)
age = st.sidebar.slider("What is the age of the car?", 1, 3, step=1)
Gears = st.sidebar.slider("how many geers", 5, 8, step=1)
make_model = st.sidebar.selectbox("select_car model", ('Renault Espace','Renault Clio','Opel Corsa','Opel Astra','Audi A1','Opel Insignia','Audi A3'))


my_dict = {
    "hp_kW": hp_kW,
    "km": km,
    "age": age,
    'Gears': Gears,
    "make_model": make_model 
}


df = pd.DataFrame.from_dict([my_dict])

# displaying user inputs before prediction
st.header("The values you selected is below")
st.table(df)


# reading and preparing the user inputs as payload for prediction
import pickle
filename = "final_pipe_model"
model = pickle.load(open(filename, "rb"))
predict = st.button("Predict")
result = model.predict(df)
if predict :
     result = model.predict(df)
     st.success(f"The price of this car is approximately ${result[0]:,.2f}")



