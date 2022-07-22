import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import locale

# import plot_likert
from math import pi

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

st.set_page_config(layout="wide")


st.title("KT Project - Climate Survey")

url = "data/housing.csv"
survey_df = pd.read_csv('data/ktp_climate_survey_2nd_cycle.csv').reset_index()
# survey_df
np_survey_df = np.asarray(survey_df)

managers = survey_df[survey_df["Are you part of Management or Staff?"] == "Management"]
staffs = survey_df[survey_df["Are you part of Management or Staff?"] == "Staff"]

regions_df = demo_respondents_group = survey_df['What region are you from?']
regions_df = np.asarray(regions_df)

regions, region_counts = np.unique(regions_df, return_counts=True)
# regions

housing_df = pd.read_csv(url)

st.sidebar.title('Survey Results')

menu = st.sidebar.radio('This web application features the following:', (
    'Demographics', 
    'Overall Results',
    'Housing Calculator',
))

if menu == 'Demographics':
    toggle = True
    col1, col2, col3, col4 = st.columns((2,1,1,1))
    
    # Management / Staff
    demo_respondents_group = survey_df['Are you part of Management or Staff?']
    group_df = np.asarray(demo_respondents_group)
    group, group_counts = np.unique(group_df, return_counts=True)

    # Gender
    demo_respondents_sex = survey_df['What is your sex?']
    sex_df = np.asarray(demo_respondents_sex)
    gender, gender_counts = np.unique(sex_df, return_counts=True)

    # Age Group
    demo_respondents_age_group = survey_df['What age group do you belong to?']
    age_group_df = np.asarray(demo_respondents_age_group)
    age_group, age_group_counts = np.unique(age_group_df, return_counts=True)

    # Education
    demo_respondents_education = survey_df['What is your highest education attainment?']
    education_df = np.asarray(demo_respondents_education)
    education, education_counts = np.unique(education_df, return_counts=True)
    
    with col1:
        fig1, ax1 = plt.subplots(figsize=(14, 8))
        fig1.subplots_adjust(0.3,0,1,1)

        ax1.axis('equal')

        plt.pie(region_counts, labels = regions, autopct='%1.1f%%', shadow=False, startangle = 90)
        plt.legend(
            loc='upper left',
            prop={'size': 11},
            bbox_to_anchor=(0.98, 1.05), # x,y coordinates
            bbox_transform=fig1.transFigure
        )
        plt.title('Respondents by Region')
        plt.axis('equal')
        # plt.show() # only works in jupyter noteboook
        st.pyplot(fig1)
    
    with col2:
        # Management / Staff
        fig1, ax1 = plt.subplots(figsize=(4, 4))
        fig1.subplots_adjust(0.3,0,1,1)
        ax1.axis('equal')
        plt.pie(group_counts, labels = group, autopct='%1.1f%%', shadow=False, startangle = 90)
        plt.legend(
            loc='upper left',
            prop={'size': 11},
            bbox_to_anchor=(0.98, 1.05), # x,y coordinates
            bbox_transform=fig1.transFigure
        )
        plt.title('CS Respondents')
        plt.axis('equal')
        st.pyplot(fig1)
    
    with col3:
        # Gender Distribution
        fig1, ax1 = plt.subplots(figsize=(4, 4))
        fig1.subplots_adjust(0.3,0,1,1)
        ax1.axis('equal')
        plt.pie(gender_counts, labels = gender, autopct='%1.1f%%', shadow=False, startangle = 90)
        plt.legend(
            loc='upper left',
            prop={'size': 11},
            bbox_to_anchor=(0.98, 1.05), # x,y coordinates
            bbox_transform=fig1.transFigure
        )
        plt.title('Gender Distribution')
        plt.axis('equal')
        st.pyplot(fig1)
    
    with col4:
        # Age Group
        fig1, ax1 = plt.subplots(figsize=(4, 4))
        fig1.subplots_adjust(0.3,0,1,1)
        ax1.axis('equal')
        plt.pie(age_group_counts, labels = age_group, autopct='%1.1f%%', shadow=False, startangle = 90)
        plt.legend(
            loc='upper left',
            prop={'size': 11},
            bbox_to_anchor=(0.98, 1.05), # x,y coordinates
            bbox_transform=fig1.transFigure
        )
        plt.title('Age Group')
        plt.axis('equal')
        st.pyplot(fig1)
        
#     col1, col2, = st.columns((2,2))    
#     with col1:        
#         # Educational Attainment
#         fig1, ax1 = plt.subplots(figsize=(4, 4))
#         fig1.subplots_adjust(0.3,0,1,1)
#         ax1.axis('equal')
#         plt.pie(education_counts, labels = education, autopct='%1.1f%%', shadow=False, startangle = 90)
#         plt.legend(
#             loc='upper left',
#             prop={'size': 11},
#             bbox_to_anchor=(0.98, 1.05), # x,y coordinates
#             bbox_transform=fig1.transFigure
#         )
#         plt.title('Educational Attainment')
#         plt.axis('equal')
#         plt.show()
        
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