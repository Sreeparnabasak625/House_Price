import numpy as np
import streamlit as st
import joblib
model = joblib.load("rf.pkl")
st.title("House Price Prediction")
st.markdown("---")
bedroom = st.number_input("Enter the number of bedroom",min_value=0, value=0)

kitchen = st.number_input("Enter the number of kitchen",min_value=0, value=0)

living_area = st.number_input("Enter the living area",min_value=0, value=2000)

condition_of_house=st.number_input("Condition of house",min_value=0, value=3)

school = st.number_input("School",min_value=0,value=0)

x=[[bedroom,kitchen,living_area,condition_of_house,school]]

predict=st.button("Predict")
if predict==True:
    np_array=np.array(x)
    price=int(model.predict(np_array)[0])
    st.write(f"House price={price}")
else:
    st.write("Please Click the button to predict the house price")