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

st.set_page_config(
    page_title="KT Project - PQA Survey",
    layout="wide"
#     page_icon="👋",
)

management_df = pd.read_csv('data/ktp_pqa_management_survey_2nd_cycle.csv').reset_index()
staff_df = pd.read_csv('data/ktp_pqa_staff_survey_2nd_cycle.csv').reset_index()

np_management_df = np.asarray(management_df)
np_staff_df = np.asarray(staff_df)

# managers = survey_df[survey_df["Are you part of Management or Staff?"] == "Management"]
# staffs = survey_df[survey_df["Are you part of Management or Staff?"] == "Staff"]

# regions_df = demo_respondents_group = survey_df['What region are you from?']
# regions_df = np.asarray(regions_df)

regs = [
    'Cordillera Administrative Region (CAR)',
    'National Capital Region (NCR)',
    'Region I: Ilocos Region',
    'Region II: Cagayan Valley', 
    'Region III: Central Luzon',
    'Region IV-A: Calabarzon',
    'Region IV-B: (Mimaropa) Southwestern Tagalog Region',
    'Region V: Bicol Region',
    'Region VI: Western Visayas',
    'Region VII: Central Visayas',
    'Region VIII: Eastern Visayas',
    'Region IX: Zamboanga Peninsula', 
    'Region X: Northern Mindanao', 
    'Region XI: Davao Region',
    'Region XII: Soccsksargen',
    'Region XIII: Caraga'
]

beneficiaries = []
beneficiaries.append(["VFM Food Products"])
beneficiaries.append(["Aretei Foods Corp."])
beneficiaries.append(["Nutridense Food Manufacturing Corp"])
beneficiaries.append(["Agri-Component Machineries and Construction Corporation (AMCC)", "Honey Buns Bakeshop"])
beneficiaries.append(["Angel Farmers Gourmet Food Corporation"])
beneficiaries.append(["Farmtec Foods Inc.", "C&H Cosmetics Industry"])
beneficiaries.append(["Rejanos Bakery"])
beneficiaries.append(["J. Emmanuel Pastries"])
beneficiaries.append(["Herbanext Laboratories Inc."])
beneficiaries.append(["Suki Trading Corporation"])
beneficiaries.append(["Rodriguez Burger and Bread Corporation"])
beneficiaries.append(["Diamond Noodles Factory", "Woodtech Builders"])
beneficiaries.append(["SLERS Industries Inc."])
beneficiaries.append(["Malagos Food Inc.", "Woodworks Collections, Inc."])
beneficiaries.append(["Kablon Farm Food Corporation"])
beneficiaries.append(["MAFFISCO-MPC"])

menu = st.sidebar.radio('Survey Results:', (
    'Demographics', 
    'Overall Results',
    'Cordillera Administrative Region (CAR)',
    'National Capital Region (NCR)',
    'Region I: Ilocos Region',
    'Region II: Cagayan Valley', 
    'Region III: Central Luzon',
    'Region IV-A: Calabarzon',
    'Region IV-B: (Mimaropa) Southwestern Tagalog Region',
    'Region V: Bicol Region',
    'Region VI: Western Visayas',
    'Region VII: Central Visayas',
    'Region VIII: Eastern Visayas',
    'Region IX: Zamboanga Peninsula', 
    'Region X: Northern Mindanao', 
    'Region XI: Davao Region',
    'Region XII: Soccsksargen',
    'Region XIII: Caraga'
))

# Region-III : Start

if menu == 'Region III: Central Luzon':
    region = 'Region III: Central Luzon'
    st.header(region)
    toggle = True

    st.sidebar.title('Actions')
    toggle = st.sidebar.button('Angel Farmers Gourmet Food Corporation')

#     region12_df = survey_df[survey_df["What region are you from?"] == region]

    firm_management_df = pd.DataFrame( management_df[management_df["Name of Your Company:"] == 'Angel Farmers Gourmet Food Corporation'] )
    st.caption('Management Data: '+ str(firm_management_df.shape[0])) 
    firm_management_df
    
    firm_staff_df =  staff_df[staff_df["Name of Your Company:"] == 'Angel Farmers Gourmet Food Corporation'] 
    
    st.caption('Staff Data: '+ str(firm_staff_df.shape[0]))
    firm_staff_df

#     if toggle:
#         firm = 'Angel Farmers Gourmet Food Corporation'
#         st.subheader(firm)
#         firm_df = survey_df[survey_df["Name of Your Company:"] == firm]
#         st.write(firm_df)
   
    firm_respondents_merged = firm_management_df.append(firm_staff_df)
    # Management / Staff
    group = pd.DataFrame( {'Management', 'Staff'})
    
    # Gender
    firm_respondents_sex = firm_respondents_merged['What is your sex?']
    sex_df = np.asarray(firm_respondents_sex)
    gender, gender_counts = np.unique(sex_df, return_counts=True)

    # Age Group
    firm_respondents_age_group = firm_respondents_merged['What age group do you belong to?']
    age_group_df = np.asarray(firm_respondents_age_group)
    age_group, age_group_counts = np.unique(age_group_df, return_counts=True)

    # Education
    firm_respondents_education = firm_respondents_merged['What is your highest education attainment?']
    education_df = np.asarray(firm_respondents_education)
    education, education_counts = np.unique(education_df, return_counts=True)

    st.subheader('Demographics')

    row1_1, row1_2, row1_3, row1_4 = st.columns((1,1,1,1))
    with row1_1:
        # Management / Staff
        fig1, ax1 = plt.subplots(figsize=(6, 6))
        fig1.subplots_adjust(0.3,0,1,1)
        ax1.axis('equal')
        plt.pie(
            [ firm_management_df.shape[0],firm_staff_df.shape[0] ], 
            labels = ['Management', 'Staff'], 
            autopct='%1.1f%%', 
            shadow=False, 
            startangle = 90
        )
        plt.legend(
            loc='upper left',
            prop={'size': 11},
            bbox_to_anchor=(0.98, 1.05), # x,y coordinates
            bbox_transform=fig1.transFigure
        )
        plt.title('Survey Respondents')
        plt.axis('equal')
        st.pyplot(fig1)

    with row1_2:        
        # Educational Attainment
        fig1, ax1 = plt.subplots(figsize=(8, 8))
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

    with row1_3:
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

    with row1_4:
        # Age Group
        fig1, ax1 = plt.subplots(figsize=(8, 8))
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

    st.subheader('Survey Results')

#     firm_managers = firm_df[firm_df["Are you part of Management or Staff?"] == "Management"]
#     firm_staff = firm_df[firm_df["Are you part of Management or Staff?"] == "Staff"]

    np_firm_managers = np.asarray(firm_management_df)
#     np_firm_managers[:,8:48]
    managers_mean = np.mean(np_firm_managers[:,8:48], axis=0)
#     managers_mean
    
    np_firm_staff = np.asarray(firm_staff_df)
#     np_firm_staff[:,8:48]
    staff_mean = np.mean(np_firm_staff[:,8:48], axis=0)
#     staff_mean
    
#     managers_mean
#     np_firm_managers
    # title
    objective_title = []
    objective_title.append("LEADERSHIP")
    objective_title.append("STRATEGY")
    objective_title.append("CUSTOMERS")
    objective_title.append("MEASUREMENT, ANALYSIS and KNOWLEDGE MANAGEMENT")
    objective_title.append("WORKFORCE")
    objective_title.append("OPERATIONS")
    objective_title.append("RESULTS")

    # Labels
    label_objective = []
    label_objective.append(['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'OVERALL'])
    label_objective.append(['Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'OVERALL'])
    label_objective.append(['Q12', 'Q13', 'Q14', 'Q15', 'Q16', 'OVERALL'])
    label_objective.append(['Q17', 'Q18', 'Q19', 'Q20', 'Q21', 'OVERALL'])
    label_objective.append(['Q22', 'Q23', 'Q24', 'Q25', 'Q26', 'Q27', 'OVERALL'])
    label_objective.append(['Q28', 'Q29', 'Q30', 'Q31', 'OVERALL'])
    label_objective.append(['Q32', 'Q33', 'Q34', 'Q35', 'Q36', 'Q37', 'Q38', 'Q39', 'OVERALL'])

    # Managers data
    firm_managers_obj = []
    mean_mngr1 = np.asarray([ managers_mean[0], managers_mean[1], managers_mean[2], managers_mean[3], managers_mean[4], managers_mean[5] ]).mean()
    firm_managers_obj.append(np.asarray([ managers_mean[0], managers_mean[1], managers_mean[2], managers_mean[3], managers_mean[4], managers_mean[5], mean_mngr1 ]))

    mean_mngr2 = np.asarray([ managers_mean[6], managers_mean[7], managers_mean[8], managers_mean[9], managers_mean[10] ]).mean()
    firm_managers_obj.append(np.asarray([ managers_mean[6], managers_mean[7], managers_mean[8], managers_mean[9], managers_mean[10], mean_mngr2 ]))
    
    mean_mngr3 = np.asarray([ managers_mean[11], managers_mean[12], managers_mean[13], managers_mean[14], managers_mean[15] ]).mean()
    firm_managers_obj.append(np.asarray([ managers_mean[1], managers_mean[2], managers_mean[9], managers_mean[21], managers_mean[22], mean_mngr3 ]))
    
    mean_mngr4 = np.asarray([ managers_mean[16], managers_mean[17], managers_mean[18], managers_mean[19], managers_mean[20] ]).mean()
    firm_managers_obj.append(np.asarray([ managers_mean[16], managers_mean[17], managers_mean[18], managers_mean[19], managers_mean[20], mean_mngr4 ]))
    
    mean_mngr5 = np.asarray([ managers_mean[21], managers_mean[22], managers_mean[23], managers_mean[24], managers_mean[25], managers_mean[26] ]).mean()
    firm_managers_obj.append(np.asarray([  managers_mean[21], managers_mean[22], managers_mean[23], managers_mean[24], managers_mean[25], managers_mean[26], mean_mngr5 ]))
    
    mean_mngr6 = np.asarray([ managers_mean[27], managers_mean[28], managers_mean[29], managers_mean[30] ]).mean()
    firm_managers_obj.append(np.asarray([ managers_mean[27], managers_mean[28], managers_mean[29], managers_mean[30], mean_mngr6 ]))
    
    mean_mngr7 = np.asarray([ managers_mean[31], managers_mean[32], managers_mean[33], managers_mean[34], managers_mean[35], managers_mean[36], managers_mean[37], managers_mean[38] ]).mean()
    firm_managers_obj.append(np.asarray([ managers_mean[31], managers_mean[32], managers_mean[33], managers_mean[34], managers_mean[35], managers_mean[36], managers_mean[37], managers_mean[38], mean_mngr7 ]))

    # Staff data
    firm_staff_obj = []
    mean_staff1 = np.asarray([ staff_mean[0], staff_mean[1], staff_mean[2], staff_mean[3], staff_mean[4], staff_mean[5] ]).mean()
    firm_staff_obj.append(np.asarray([ staff_mean[0], staff_mean[1], staff_mean[2], staff_mean[3], staff_mean[4], staff_mean[5], mean_staff1 ]))

    mean_staff2 = np.asarray([ staff_mean[6], staff_mean[7], staff_mean[8], staff_mean[9], staff_mean[10] ]).mean()
    firm_staff_obj.append(np.asarray([ staff_mean[6], staff_mean[7], staff_mean[8], staff_mean[9], staff_mean[10], mean_staff2 ]))
    
    mean_staff3 = np.asarray([ staff_mean[11], staff_mean[12], staff_mean[13], staff_mean[14], staff_mean[15] ]).mean()
    firm_staff_obj.append(np.asarray([ staff_mean[1], staff_mean[2], staff_mean[9], staff_mean[21], staff_mean[22], mean_staff3 ]))
    
    mean_staff4 = np.asarray([ staff_mean[16], staff_mean[17], staff_mean[18], staff_mean[19], staff_mean[20] ]).mean()
    firm_staff_obj.append(np.asarray([ staff_mean[16], staff_mean[17], staff_mean[18], staff_mean[19], staff_mean[20], mean_staff4 ]))
    
    mean_staff5 = np.asarray([ staff_mean[21], staff_mean[22], staff_mean[23], staff_mean[24], staff_mean[25], staff_mean[26] ]).mean()
    firm_staff_obj.append(np.asarray([  staff_mean[21], staff_mean[22], staff_mean[23], staff_mean[24], staff_mean[25], staff_mean[26], mean_staff5 ]))
    
    mean_staff6 = np.asarray([ staff_mean[27], staff_mean[28], staff_mean[29], staff_mean[30] ]).mean()
    firm_staff_obj.append(np.asarray([ staff_mean[27], staff_mean[28], staff_mean[29], staff_mean[30], mean_staff6 ]))
    
    mean_staff7 = np.asarray([ staff_mean[31], staff_mean[32], staff_mean[33], staff_mean[34], staff_mean[35], staff_mean[36], staff_mean[37], staff_mean[38] ]).mean()
    firm_staff_obj.append(np.asarray([ staff_mean[31], staff_mean[32], staff_mean[33], staff_mean[34], staff_mean[35], staff_mean[36], staff_mean[37], staff_mean[38], mean_staff7 ]))
    
    radar_df = pd.DataFrame({
        'group': ['Manager','Staff'],
        'LEADERSHIP': [firm_managers_obj[0][0:5].mean(), firm_staff_obj[0][0:5].mean()],
        'STRATEGY': [firm_managers_obj[1][0:4].mean(), firm_staff_obj[1][0:4].mean()],
        'CUSTOMERS': [firm_managers_obj[2][0:4].mean(), firm_staff_obj[2][0:4].mean()],
        'MEASUREMENT, ANALYSIS and KNOWLEDGE MANAGEMENT': [firm_managers_obj[3][0:4].mean(), firm_staff_obj[3][0:4].mean()],
        'WORKFORCE': [firm_managers_obj[4][0:6].mean(), firm_staff_obj[4][0:6].mean()],
        'OPERATIONS': [firm_managers_obj[5][0:3].mean(), firm_staff_obj[5][0:3].mean()],
        'RESULTS': [firm_managers_obj[6][0:8].mean(), firm_staff_obj[6][0:8].mean()],
        })

#     radar_df
    row0_1, row0_2, row0_3 = st.columns((1,3,1))
    
    with row0_2:
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
        plt.yticks([1,2,3,4,5], ["1.0","2.0","3.0","4.0","5.0"], color="grey", size=7)
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


#     firm_objective = []

#     i = 0
#     while i < len(objective_title):

#         row1_1, row1_2, row1_3 = st.columns((1,3,1))

#         with row1_2:
#             firm_objective.append([ label_objective[i], firm_managers_obj[i], firm_staff_obj[i] ])

#             X = np.arange(len(label_objective[i]))
#             width = 0.5  # the width of the bars

#             fig, ax = plt.subplots()
#             rects1 = ax.bar(X - width/2, firm_objective[i][1], width, label='Managers')
#             if i != 7:
#                 rects2 = ax.bar(X + width/2, firm_objective[i][2], width, label='Staff')

#             fig = plt.figure(figsize=(14, 8))
#             ax = fig.add_axes([0,0,1,1])

#             ax.set_ylabel('Rating')
#             ax.set_title(objective_title[i])
#             ax.set_xticks(X, firm_objective[i][0])

#             ax.bar(X + 0.00, firm_objective[i][1],  width = 0.25)
#             if i != 7:
#                 ax.bar(X + 0.25, firm_objective[i][2],  width = 0.25)

#             if i != 7:
#                 ax.legend(labels=['Managers', 'Staff'])
#             else:
#                 ax.legend(labels=['Managers'])

#             ax.bar_label(rects1)
#             ax.bar_label(rects2)
#             st.pyplot(fig)

#         i += 1
        
# Region-III : End