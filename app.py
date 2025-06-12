import numpy as np
import pandas as pd
import streamlit as st
import joblib as jb

model = jb.load("aircraft.pkl")
st.title("DashyBashy")
Flight_Distance = st.number_input("Distance in km")
Number_of_Passengers = st.number_input("Number of Passengers")
Flight_Duration = st.number_input("Duration of Flight")
Aircraft_Type = st.selectbox("Aircraft Type",["T1","T2","T3"])
Input_Data = pd.DataFrame({"Flight_Distance":Flight_Distance,
                           "Number_of_Passengers":Number_of_Passengers,
                           "Flight_Duration":Flight_Duration,
                           "Aircraft_Type_Type1":[1 if Aircraft_Type == "T1" else 0],
                           "Aircraft_Type_Type2":[1 if Aircraft_Type == "T2" else 0],
                           "Aircraft_Type_Type3":[1 if Aircraft_Type == "T3" else 0]})
if st.button("Predict"):
    Fuel_Consumption = model.predict(Input_Data)
    st.write(Fuel_Consumption)