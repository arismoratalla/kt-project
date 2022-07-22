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
#     col1, col2, col3, col4 = st.columns((2,1,1,1))
    
    
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
    
    row1_1, row1_2 = st.columns((2, 2))
    
    with row1_1:
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
        
    with row1_2:        
        # Educational Attainment
        fig1, ax1 = plt.subplots(figsize=(4, 4))
        fig1.subplots_adjust(0.3,0,1,1)
        ax1.axis('equal')
        plt.pie(education_counts, labels = education, autopct='%1.1f%%', shadow=False, startangle = 90)
        plt.legend(
            loc='upper left',
            prop={'size': 11},
            bbox_to_anchor=(0.98, 1.05), # x,y coordinates
            bbox_transform=fig1.transFigure
        )
        plt.title('Educational Attainment')
        plt.axis('equal')
        st.pyplot(fig1)
    
    row2_1, row2_2, row2_3, row2_4 = st.columns((2, 1, 1, 1))
    
    with row2_1:
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
    
    with row2_2:
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
    
    with row2_3:
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

if menu == 'Overall Results':
    
    managers = survey_df[survey_df["Are you part of Management or Staff?"] == "Management"]
    staff = survey_df[survey_df["Are you part of Management or Staff?"] == "Staff"]

    np_managers = np.asarray(managers)
    np_staff = np.asarray(staff)

#     np_managers[:,9:59]
#     np_staff[:,59:99]
    
    managers_mean = np.mean(np_managers[:,9:59], axis=0)
    
    # Select MEANS for Objective 1 questions
    managers_objective_1 = [managers_mean[5], managers_mean[11], managers_mean[19], managers_mean[36], managers_mean[37]]
    managers_objective_1 = np.asarray(managers_objective_1)

    # Select MEANS for Objective 2 questions
    managers_objective_2 = [managers_mean[3], managers_mean[6], managers_mean[8], managers_mean[24], managers_mean[33], managers_mean[34]]
    managers_objective_2 = np.asarray(managers_objective_2)

    # Select MEANS for Objective 3 questions
    managers_objective_3 = [managers_mean[1], managers_mean[2], managers_mean[9], managers_mean[21], managers_mean[22]]
    managers_objective_3 = np.asarray(managers_objective_3)

    # Select MEANS for Objective 4 questions
    managers_objective_4 = [managers_mean[14], managers_mean[15], managers_mean[16], managers_mean[23], managers_mean[38]]
    managers_objective_4 = np.asarray(managers_objective_4)

    # Select MEANS for Objective 5 questions
    managers_objective_5 = [managers_mean[0], managers_mean[10], managers_mean[30], managers_mean[31], managers_mean[39]]
    managers_objective_5 = np.asarray(managers_objective_5)

    # Select MEANS for Objective 6 questions
    managers_objective_6 = [managers_mean[4], managers_mean[18], managers_mean[20], managers_mean[28], managers_mean[32]]
    managers_objective_6 = np.asarray(managers_objective_6)

    # Select MEANS for Objective 7 questions
    managers_objective_7 = [managers_mean[12], managers_mean[13], managers_mean[17], managers_mean[27]]
    managers_objective_7 = np.asarray(managers_objective_7)

    # Select MEANS for Objective 7 questions
    managers_objective_8 = [managers_mean[40], managers_mean[41], managers_mean[42], managers_mean[43], managers_mean[44], managers_mean[45], managers_mean[46], managers_mean[47], managers_mean[48], managers_mean[49]]
    managers_objective_8 = np.asarray(managers_objective_8)

    # Select MEANS for Objective 9 questions
    managers_objective_9 = [managers_mean[7], managers_mean[25], managers_mean[26], managers_mean[29], managers_mean[35]]
    managers_objective_9 = np.asarray(managers_objective_9)
    # managers_objective_9
    
    
    staff_mean = np.mean(np_staff[:,59:99], axis=0)
    
    # Select MEANS for Objective 1 questions
    staff_objective_1 = [staff_mean[5], staff_mean[11], staff_mean[19], staff_mean[36], staff_mean[37]]
    staff_objective_1 = np.asarray(staff_objective_1)

    # Select MEANS for Objective 2 questions
    staff_objective_2 = [staff_mean[3], staff_mean[6], staff_mean[8], staff_mean[24], staff_mean[33], staff_mean[34]]
    staff_objective_2 = np.asarray(staff_objective_2)

    # Select MEANS for Objective 3 questions
    staff_objective_3 = [staff_mean[1], staff_mean[2], staff_mean[9], staff_mean[21], staff_mean[22]]
    staff_objective_3 = np.asarray(staff_objective_3)

    # Select MEANS for Objective 4 questions
    staff_objective_4 = [staff_mean[14], staff_mean[15], staff_mean[16], staff_mean[23], staff_mean[38]]
    staff_objective_4 = np.asarray(staff_objective_4)

    # Select MEANS for Objective 5 questions
    staff_objective_5 = [staff_mean[0], staff_mean[10], staff_mean[30], staff_mean[31], staff_mean[39]]
    staff_objective_5 = np.asarray(staff_objective_5)

    # Select MEANS for Objective 6 questions
    staff_objective_6 = [staff_mean[4], staff_mean[18], staff_mean[20], staff_mean[28], staff_mean[32]]
    staff_objective_6 = np.asarray(staff_objective_6)

    # Select MEANS for Objective 7 questions
    staff_objective_7 = [staff_mean[12], staff_mean[13], staff_mean[17], staff_mean[27]]
    staff_objective_7 = np.asarray(staff_objective_7)

    # Select MEANS for Objective 9 questions
    staff_objective_9 = [staff_mean[7], staff_mean[25], staff_mean[26], staff_mean[29], staff_mean[35]]
    staff_objective_9 = np.asarray(staff_objective_9)
    
#     row1_1, row1_2 = st.columns((2, 2))
    
    
    
    # Set Bargraph Data

    # Labels
    label_objective_1 = ['Q6', 'Q12', 'Q20', 'Q37', 'Q38']
    label_objective_2 = ['Q4', 'Q7', 'Q9', 'Q34', 'Q35']
    label_objective_3 = []
    label_objective_4 = []
    label_objective_5 = []
    label_objective_6 = []
    label_objective_7 = []
    label_objective_8 = []
    label_objective_9 = []

    # Managers data
    bar_managers_obj1 = [ managers_mean[5], managers_mean[11], managers_mean[19], managers_mean[36], managers_mean[37] ]
    bar_managers_obj2 = [ managers_mean[3], managers_mean[6], managers_mean[8], managers_mean[33], managers_mean[34] ]
    bar_managers_obj3 = []
    bar_managers_obj4 = []
    bar_managers_obj5 = []
    bar_managers_obj6 = []
    bar_managers_obj7 = []
    bar_managers_obj8 = []
    bar_managers_obj9 = []


    # Staff data
    bar_staff_obj1 = [ staff_mean[5], staff_mean[11], staff_mean[19], staff_mean[36], staff_mean[37] ]
    bar_staff_obj2 = [ staff_mean[2], staff_mean[6], staff_mean[8], staff_mean[33], staff_mean[34] ]
    bar_staff_obj3 = []
    bar_staff_obj4 = []
    bar_staff_obj5 = []
    bar_staff_obj6 = []
    bar_staff_obj7 = []
    bar_staff_obj8 = []
    bar_staff_obj9 = []

    
    row1_1, row1_2, row1_3 = st.columns((1, 3, 1))
    
    with row1_2:
        # Radar Graph
        # Set data

        radar_df = pd.DataFrame({
        'group': ['Manager','Staff'],
        'Objective 1': [managers_objective_1.mean(), staff_objective_1.mean()],
        'Objective 2': [managers_objective_2.mean(), staff_objective_2.mean()],
        'Objective 3': [managers_objective_3.mean(), staff_objective_3.mean()],
        'Objective 4': [managers_objective_4.mean(), staff_objective_4.mean()],
        'Objective 5': [managers_objective_5.mean(), staff_objective_5.mean()],
        'Objective 6': [managers_objective_6.mean(), staff_objective_6.mean()],
        'Objective 7': [managers_objective_7.mean(), staff_objective_7.mean()],
        'Objective 9': [managers_objective_9.mean(), staff_objective_9.mean()]
        })

        ## Draw Dart ##

        # number of variable
        categories=list(radar_df)[1:]
        N = len(categories)

        # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]

        # Initialise the spider plot
        fig = plt.figure(figsize=(14, 10))
        ax = plt.subplot(111, polar=True)

        # If you want the first axis to be on top:
        ax.set_theta_offset(pi / 2)
        ax.set_theta_direction(-1)

        # Draw one axe per variable + add labels
        plt.xticks(angles[:-1], categories)

        # Draw ylabels
        ax.set_rlabel_position(0)
        plt.yticks([1,2,3,4,5,6,7], ["1.0","2.0","3.0","4.0","5.0","6.0","7.0"], color="grey", size=7)
        plt.ylim(0,)

    #     categories

        ## Plot Data ##

        # Manager
        values=radar_df.loc[0].drop('group').values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', label="Manager")
        ax.fill(angles, values, 'b', alpha=0.1)

        # # Staff
        values=radar_df.loc[1].drop('group').values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', label="Staff")
        ax.fill(angles, values, 'r', alpha=0.1)

        # Add legend
        plt.legend(loc='upper right', bbox_to_anchor=(1, 1))

        # Show the graph
        st.pyplot(fig)
    
    row2_1, row2_2, row2_3 = st.columns((1, 3, 1))
    
    with row2_2:
        bar_objective_1 = [ label_objective_1, bar_managers_obj1, bar_staff_obj1 ]

        X = np.arange(5)
        width = 0.5  # the width of the bars

        # fig, ax = plt.subplots()
        rects1 = ax.bar(X - width/2, bar_objective_1[1], width, label='Managers')
        rects2 = ax.bar(X + width/2, bar_objective_1[2], width, label='Staff')

        fig = plt.figure(figsize=(14, 8))
        ax = fig.add_axes([0,0,1,1])

        ax.set_ylabel('Rating')
        ax.set_title("Objective 1: To  determine the employees' extent of understanding of the company's vision, mission, quality policy, purposes and directions")
        ax.set_xticks(X, bar_objective_1[0])

        ax.bar(X + 0.00, bar_objective_1[1],  width = 0.25)
        ax.bar(X + 0.25, bar_objective_1[2],  width = 0.25)

        ax.legend(labels=['Managers', 'Staff'])

        ax.bar_label(rects1)
        ax.bar_label(rects2)
        st.pyplot(fig)
        
        
    row3_1, row3_2, row3_3 = st.columns((1, 3, 1))      
    
    with row3_2:
        bar_objective_2 = [ label_objective_2, bar_managers_obj2, bar_staff_obj2 ]

        X = np.arange(5)
        width = 0.5  # the width of the bars

        # fig, ax = plt.subplots()
        rects1 = ax.bar(X - width/2, bar_objective_2[1], width, label='Managers')
        rects2 = ax.bar(X + width/2, bar_objective_2[2], width, label='Staff')

        fig = plt.figure(figsize=(14, 8))
        ax = fig.add_axes([0,0,1,1])

        ax.set_ylabel('Rating')
        ax.set_title("Objective 2: To find out the employees’ perception of the company’s leadership")
        ax.set_xticks(X, bar_objective_2[0])

        ax.bar(X + 0.00, bar_objective_2[1],  width = 0.25)
        ax.bar(X + 0.25, bar_objective_2[2],  width = 0.25)

        ax.legend(labels=['Managers', 'Staff'])

        ax.bar_label(rects1)
        ax.bar_label(rects2)
        st.pyplot(fig)
    
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