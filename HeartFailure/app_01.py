import numpy as np
import pickle
import streamlit as st

with open('MODEL.pkl', 'rb') as file:
    model = pickle.load(file)
file.close()

st.title("Heart Failure Prediction Using Machine Learning")

age = st.number_input('age')
sex = st.number_input('sex')
cp = st.number_input('cp')
trestbps = st.number_input('trestbps')
chol = st.number_input('chol')
fbs = st.number_input('fbs')
restecg = st.number_input('restecg')
thalach = st.number_input('thalach')
exang = st.number_input('exang')
oldpeak = st.number_input('oldpeak')
slope = st.number_input('slope')
ca = st.number_input('ca')
thal = st.number_input('thal')

if st.button('Predict'):
    x = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang,oldpeak, slope,ca,thal]])
    Y_predict = model.predict(x)
    st.success('Prediction is {}'.format(Y_predict))

    

