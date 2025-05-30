import streamlit as st
import pandas as pd
import numpy as np
st.title("Patient's Data")
st.write("This is a sample web app.")

first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
gender = st.selectbox("Gender", ["Male","Female","Transgender","Don't want to disclose"])
age = st.number_input("Your Age",0,100,30,1)
dob = st.date_input("Enter your Birth Date")
#id,radius_mean,texture_mean,perimeter_mean,area_mean,
#smoothness_mean,compactness_mean,concavity_mean,

id = st.number_input("Enter your id number")
radius_mean = st.number_input("Mean Radius")
texture_mean = st.number_input("Mean Texture")
perimeter_mean = st.number_input("Mean Perimeter")
area_mean = st.number_input("Mean Area")
smoothness_mean = st.number_input("Smoothness Mean")
compactness_mean = st.number_input("Compactness Mean")
concavity_mean = st.number_input("Concavity Mean")

#Mean_concave_points,symmetry_mean,fractal_dimension_mean,
concave_points_mean = st.number_input("Concave Points Mean")
symmetry_mean = st.number_input("Mean Symmetry")
fractal_dimension_mean = st.number_input("Mean Fractal Dimension")

#radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,
radius_se = st.number_input("Radius Se")
texture_se = st.number_input("Texture Se")
area_se = st.number_input("Area Se")
smoothness_se = st.number_input("Smoothness Se")
compactness_se = st.number_input("Compactness Se")

#concavity_se,concave points_se,symmetry_se,fractal_dimension_se,
concavity_se = st.number_input("Concavity Se")
concave_points_se = st.number_input("Concave Points Se")
symmetry_se = st.number_input("Symmetry Se")
fractal_dimension_se = st.number_input("Fractal Dimension Se")

#radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,
radius_worst = st.number_input("Worst Radius")
texture_worst = st.number_input("Worst Texture")
perimeter_worst = st.number_input("Worst Perimeter")
area_worst = st.number_input("Worst Area")
smoothness_worst = st.number_input("Worst Smoothness")

#compactness_worst,concavity_worst,concave points_worst,symmetry_worst,fractal_dimension_worst
compactness_worst = st.number_input("Worst Compactness")
concavity_worst = st.number_input("Worst Concavity")
concave_points_worst = st.number_input("Concave Points Worst")
symmetry_worst = st.number_input("Symmetry Worst")
fractal_dimension_worst = st.number_input("Fractual Dimension Worst")

