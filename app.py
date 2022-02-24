# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 00:51:49 2022

@author: Lenovo
"""

import numpy as np
import pickle
import streamlit as st
from PIL import Image

#loading the saved model
loaded_model = pickle.load(open('F:/BE_Project/model/trained_model.sav', 'rb'))

def welcome():
        return 'Welcome to the App'
#creating a function for prediction
def fchtc_predictor(Q,Ts):
    prediction = loaded_model.predict([[Q, Ts]])
    print(prediction)
    return prediction

def main():
#    st.title('Forced Convection Heat Transfer Coefficient Predictor for Air AI app')
    html_temp = """
    <div style="background-color:#34495E ;padding:10px">
    <h2 style="color:LightSalmon;text-align:center;">Forced Convection Heat Transfer Coefficient Predictor app </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.write('''This is a web app to predict the Forced Convection Heat Transfer Coefficient based on average surface temperature(C) and power input(W).
    Please enter the\
    value of each feature. After that, click on the Predict button at the bottom to\
    see the prediction.''')
    Ts = st.text_input('Average surface temperature in °C')
    Q = st.text_input('Power input in Watts')
    
    result = ""
    if st.button('predict'):
        result = fchtc_predictor(Q, Ts)
    st.success('The Forced Convection Heat Transfer Coefficient is {} W/(m²-°C)'.format(result))
    if st.button("About"):
        st.text("Developed by")
        st.text("Project Group No. 10, A.Y. 2021-22")
        st.text("Mechanical Engineering, Sinhgad College of Engineering, Pune")
        
if __name__=='__main__':
    main()
    
        