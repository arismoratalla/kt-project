import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title("Insurance Pricing Applicaiton")
st.write("""From the Insurance Data, we built a machine learning-based pricing model to get he quotation for each client based on their demographics.""")

# insurance_df = pd.read_csv('insurance_regression.csv')

# insurance_df.head()

st.sidebar.title('About')
st.sidebar.info('Change parameters to see how insurance prices change.')
st.sidebar.title('Parameters')
#Age
age = st.sidebar.slider('Age', 0, 100, 24)

#BMI
bmi = st.sidebar.slider('BMI', 13, 40, 31)

#Number of Children
num_children = st.sidebar.slider('Number of Children', 0, 12, 1)

#Gender
gender = st.sidebar.radio('Gender', ('Female', 'Male'))

if gender == 'Male':
    is_female = 0
else:
    is_female = 1
    

#Is smoker
smoker = st.sidebar.radio('Are you a smoker?', ('Yes', 'No'))
if smoker == 'Yes':
    is_smoker = 1
else:
    is_smoker = 0
    
#Region
region = st.sidebar.selectbox("Region", ['northwest', 'northeast', 'southeast', 'southwest'])

if region == 'northeast':
    loc_list = [1,0,0,0]
if region == 'northwest':
    loc_list = [0,1,0,0]
if region == 'southeast':
    loc_list = [0,0,1,0]
if region == 'southwest':
    loc_list = [0,0,0,1]
    
st.subheader('Output Insurance Price')

filename = 'model/finalized_model.sav'
loaded_model = joblib.load(filename)

prediction = np.round(loaded_model.predict([[age, bmi, num_children, is_female, is_smoker] + loc_list])[0])
# loaded_model.predict([[age, bmi, num_children, is_female, is_smoker] + loc_list])[0]

st.write(f"Suggested Insurance Price is: {prediction}")