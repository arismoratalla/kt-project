import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import locale

locale.setlocale(locale.LC_ALL, '')
area = 0 
bedroom = 0 
bathroom =0 
storey = 0 
parking = 0 
is_mainroad = 0 
has_guestroom = 0 
has_basement = 0 
has_heating = 0 
has_airconditioning = 0 
is_preferred = 0 
furnishingstatus = 'Unfurnished'
furnishing_list = [0,0,0]

st.title("KT Project - Climate Survey")

url = "data/housing.csv"

housing_df = pd.read_csv(url)

st.sidebar.title('About')

menu = st.sidebar.radio('This web application features the following:', (
    'Demographics', 
    'Overall Results',
    'Housing Calculator',
))

if menu == 'The dataframe':
    toggle = True
    st.sidebar.title('Actions')
    show = st.sidebar.button('Show/Hide DataFrame')
    
    if toggle:
        st.write(housing_df.head(20))
    else:
        st.write(housing_df)
    
if menu == 'Charts':
    
    line_chart_data = housing_df[['area', 'price']]
    area_chart_data = housing_df[['bedrooms', 'price']]
    bar_chart_data = housing_df[['area', 'stories']]
    
    st.line_chart(line_chart_data)
    st.area_chart(area_chart_data)
    st.bar_chart(bar_chart_data)
    
    st.sidebar.title('Actions')
    
if menu == 'Housing Calculator':
    
    st.sidebar.title('Parameters')

    area = st.sidebar.slider('Area', 3000, 20000, 5000)
    bedroom = st.sidebar.slider('Bedrooms', 0, 6, 2)
    bathroom = st.sidebar.slider('Bathrooms', 0, 6, 2)
    storey = st.sidebar.slider('Stories', 1, 4, 2)
    parking = st.sidebar.slider('Parking', 0, 3, 1)
    
    mainroad = st.sidebar.radio('Located at Main Road?', ('Yes', 'No'))
    if mainroad == 'Yes':
        is_mainroad = 1
    else:
        is_mainroad = 0

    guestroom = st.sidebar.radio('Has a Guest Room?', ('Yes', 'No'))
    if guestroom == 'Yes':
        has_guestroom = 1
    else:
        has_guestroom = 0
        
    basement = st.sidebar.radio('Has a Basement?', ('Yes', 'No'))
    if basement == 'Yes':
        has_basement = 1
    else:
        has_basement = 0
        
    heating = st.sidebar.radio('Has a Hot Water Heating?', ('Yes', 'No'))
    if heating == 'Yes':
        has_heating = 1
    else:
        has_heating = 0
    
    airconditioning = st.sidebar.radio('Has Airconditioning?', ('Yes', 'No'))
    if airconditioning == 'Yes':
        has_airconditioning = 1
    else:
        has_airconditioning = 0
        
    prefarea = st.sidebar.radio('Is this a Preferred Area?', ('Yes', 'No'))
    if prefarea == 'Yes':
        is_preferred = 1
    else:
        is_preferred = 0   

    furnishingstatus = st.sidebar.selectbox("Furnishing Status", ['Furnished', 'Semi-Furnished', 'Unfurnished'])
    if furnishingstatus == 'Furnished':
        furnishing_list = [1,0,0]
    if furnishingstatus == 'Semi-Furnished':
        furnishing_list = [0,1,0]
    if furnishingstatus == 'Unfurnished':
        furnishing_list = [0,0,1]

    st.subheader('Output Housing Price')

    filename = 'model/housing_model3.sav'
    loaded_model = joblib.load(filename)

    prediction = np.round(loaded_model.predict([[area, bedroom, bathroom, storey, parking, is_mainroad, has_guestroom, has_basement, has_heating, has_airconditioning, is_preferred]+  furnishing_list])[0])

    pricing = locale.format("%d", prediction, grouping=True)

    st.write(f"Predicted Housing Price is: {pricing}")