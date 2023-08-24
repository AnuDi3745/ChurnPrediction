# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 16:11:06 2023

@author: anish
"""

import pickle
import streamlit as st
import bz2

def decompress_pickle(file):

    data = bz2.BZ2File(file, 'rb')
    data = pickle.load(data)
    return data

loaded_model = decompress_pickle('C:/Users/anish/Documents/Sunbase task/finalmodel.pbz2')


  
st.title('Churn Prediction Web App')
churn_p = ''
res = ''
age = st.number_input("Customer's Age")
sub_mon = st.number_input("Customer's subscription Period(months)")
tug = st.text_input("Customer's Total Internet Usage(GB)")
gender = st.text_input("Customer's Gender")
loc = st.text_input("Customer's City")
tb = st.text_input("Customer's Total_Bill")
cpg = st.number_input(("Customer's Cost_per_GB"))


if gender == "Male":
    gender = 1
else:
    gender = 0

if st.button('Churn'):
    if loc == 'Chicago':
        churn_p = loaded_model.predict([[age,sub_mon,tug,gender,1,0,0,0,0,tb,cpg]])
    elif loc == 'Houston':
        churn_p = loaded_model.predict([[age,sub_mon,tug,gender,0,1,0,0,0,tb,cpg]])
    elif loc == 'Los Angeles':
        churn_p = loaded_model.predict([[age,sub_mon,tug,gender,0,0,1,0,0,tb,cpg]])
    elif loc == 'Miami':
        churn_p = loaded_model.predict([[age,sub_mon,tug,gender,0,0,0,1,0,tb,cpg]])
    elif loc == 'New York':
        churn_p = loaded_model.predict([[age,sub_mon,tug,gender,0,0,0,0,1,tb,cpg]])

    if churn_p[0] == 0:
        res = "The Customer is not interested"
    else:
        res = "The Customer is interested"


    
st.success(res)
