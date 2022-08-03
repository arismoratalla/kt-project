import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import locale

# import plot_likert
from math import pi
import plot_likert

locale.setlocale(locale.LC_ALL, '')

st.set_page_config(layout="wide")


st.title("KT Project - Climate Survey")

survey_df = pd.read_csv('data/ktp_climate_survey_2nd_cycle.csv').reset_index()
# survey_df
np_survey_df = np.asarray(survey_df)

managers = survey_df[survey_df["Are you part of Management or Staff?"] == "Management"]
staffs = survey_df[survey_df["Are you part of Management or Staff?"] == "Staff"]

regions_df = demo_respondents_group = survey_df['What region are you from?']
regions_df = np.asarray(regions_df)

regions, region_counts = np.unique(regions_df, return_counts=True)
# regions

st.sidebar.title('Survey Results')

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

# regs
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
# for beneficiary in beneficiaries:
#     beneficiary




menu = st.sidebar.radio('Consolidated Results:', (
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

if menu == 'Demographics':
    
#     rng = np.random.default_rng(seed=42)
#     data = pd.DataFrame(rng.choice(plot_likert.scales.agree, (10,2)), columns=['Q1','Q2'])
#     fig, plot_likert = plt.figure(figsize=(10, 4))
#     plot_likert.plot_likert(data, plot_likert.scales.agree);
    
#     st.pyplot(fig)
    
    toggle = True
    
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
#         st.pyplot(fig1)
        
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
    
    #get manager questions
    managers_mean = np.mean(np_managers[:,9:59], axis=0)
    
    # Select MEANS for Objective 1 questions
    managers_objective = []
    managers_objective.append([managers_mean[5], managers_mean[11], managers_mean[19], managers_mean[36], managers_mean[37]])
    managers_objective[0] = np.asarray(managers_objective[0])

    # Select MEANS for Objective 2 questions
    managers_objective.append(np.asarray([ managers_mean[3], managers_mean[6], managers_mean[8], managers_mean[24], managers_mean[33], managers_mean[34]]))

    managers_objective.append(np.asarray([managers_mean[1], managers_mean[2], managers_mean[9], managers_mean[21], managers_mean[22]]))

    managers_objective.append(np.asarray([managers_mean[14], managers_mean[15], managers_mean[16], managers_mean[23], managers_mean[38]]))

    managers_objective.append(np.asarray([managers_mean[0], managers_mean[10], managers_mean[30], managers_mean[31], managers_mean[39]]))

#     # Select MEANS for Objective 6 questions
    managers_objective.append(np.asarray([managers_mean[4], managers_mean[18], managers_mean[20], managers_mean[28], managers_mean[32]]))

#     # Select MEANS for Objective 7 questions
    managers_objective.append(np.asarray([managers_mean[12], managers_mean[13], managers_mean[17], managers_mean[27]]))

#     # Select MEANS for Objective 7 questions
    managers_objective.append(np.asarray([managers_mean[40], managers_mean[41], managers_mean[42], managers_mean[43], managers_mean[44], managers_mean[45], managers_mean[46], managers_mean[47], managers_mean[48], managers_mean[49]]))

#     managers_objective.append(['test'])
#     # Select MEANS for Objective 9 questions
    managers_objective.append(np.asarray([managers_mean[7], managers_mean[25], managers_mean[26], managers_mean[29], managers_mean[35]]))
    # managers_objective_9
    
    
    staff_mean = np.mean(np_staff[:,59:99], axis=0)
    
    staff_objective = []
    # Select MEANS for Objective 1 questions
    staff_objective.append(np.asarray([staff_mean[5], staff_mean[11], staff_mean[19], staff_mean[36], staff_mean[37]]))

    # Select MEANS for Objective 2 questions
    staff_objective.append(np.asarray([staff_mean[3], staff_mean[6], staff_mean[8], staff_mean[24], staff_mean[33], staff_mean[34]]))

    # Select MEANS for Objective 3 questions
    staff_objective.append(np.asarray([staff_mean[1], staff_mean[2], staff_mean[9], staff_mean[21], staff_mean[22]]))

    # Select MEANS for Objective 4 questions
#     staff_objective_4 = [staff_mean[14], staff_mean[15], staff_mean[16], staff_mean[23], staff_mean[38]]
    staff_objective.append(np.asarray([staff_mean[14], staff_mean[15], staff_mean[16], staff_mean[23], staff_mean[38]]))

#     # Select MEANS for Objective 5 questions
    staff_objective.append(np.asarray([staff_mean[0], staff_mean[10], staff_mean[30], staff_mean[31], staff_mean[39]]))

#     # Select MEANS for Objective 6 questions
    staff_objective.append(np.asarray([staff_mean[4], staff_mean[18], staff_mean[20], staff_mean[28], staff_mean[32]]))

#     # Select MEANS for Objective 7 questions
    staff_objective.append(np.asarray([staff_mean[12], staff_mean[13], staff_mean[17], staff_mean[27]]))

    staff_objective.append(['test'])
#     # Select MEANS for Objective 9 questions
    staff_objective.append(np.asarray([staff_mean[7], staff_mean[25], staff_mean[26], staff_mean[29], staff_mean[35]]))
    
    
    # Set Bargraph Data

    # Labels
    label_objective = []
    label_objective.append(['Q6', 'Q12', 'Q20', 'Q37', 'Q38'])
    label_objective.append(['Q4', 'Q7', 'Q9', 'Q34', 'Q35'])
    label_objective.append(['Q2', 'Q3', 'Q10', 'Q22', 'Q23'])
    label_objective.append(['Q15', 'Q16', 'Q17', 'Q24', 'Q39'])
    label_objective.append(['Q1', 'Q10', 'Q31', 'Q32', 'Q40'])
    label_objective.append(['Q5', 'Q19', 'Q21', 'Q29', 'Q33'])
    label_objective.append(['Q13', 'Q14', 'Q18', 'Q28'])
    label_objective.append(['Q41', 'Q42', 'Q43', 'Q44', 'Q45', 'Q46', 'Q47', 'Q48', 'Q49', 'Q50'])
    label_objective.append(['Q8', 'Q26', 'Q27', 'Q30', 'Q36'])

    # Managers data
    bar_managers_obj = []
    bar_managers_obj.append([ managers_mean[5], managers_mean[11], managers_mean[19], managers_mean[36], managers_mean[37] ])
    bar_managers_obj.append([ managers_mean[3], managers_mean[6], managers_mean[8], managers_mean[33], managers_mean[34] ])
    bar_managers_obj.append([ managers_mean[1], managers_mean[2], managers_mean[9], managers_mean[21], managers_mean[22] ])
    bar_managers_obj.append([ managers_mean[14], managers_mean[15], managers_mean[16], managers_mean[23], managers_mean[38] ])
    bar_managers_obj.append([ managers_mean[0], managers_mean[9], managers_mean[30], managers_mean[31], managers_mean[39] ])
    bar_managers_obj.append([ managers_mean[4], managers_mean[18], managers_mean[20], managers_mean[28], managers_mean[32] ])
    bar_managers_obj.append([ managers_mean[12], managers_mean[13], managers_mean[1], managers_mean[27] ])
    bar_managers_obj.append([ managers_mean[40], managers_mean[41], managers_mean[42], managers_mean[43], managers_mean[44], managers_mean[45], managers_mean[46], managers_mean[47], managers_mean[48], managers_mean[49] ])
    bar_managers_obj.append([ managers_mean[7], managers_mean[25], managers_mean[26], managers_mean[29], managers_mean[35] ])


    # Staff data
    bar_staff_obj = []
    bar_staff_obj.append([ staff_mean[5], staff_mean[11], staff_mean[19], staff_mean[36], staff_mean[37] ])
    bar_staff_obj.append([ staff_mean[2], staff_mean[6], staff_mean[8], staff_mean[33], staff_mean[34] ])
    bar_staff_obj.append([ staff_mean[1], staff_mean[2], staff_mean[9], staff_mean[21], staff_mean[22] ])
    bar_staff_obj.append([ staff_mean[14], staff_mean[15], staff_mean[16], staff_mean[23], staff_mean[38] ])
    bar_staff_obj.append([ staff_mean[0], staff_mean[9], staff_mean[30], staff_mean[31], staff_mean[39] ])
    bar_staff_obj.append([ staff_mean[4], staff_mean[18], staff_mean[20], staff_mean[28], staff_mean[32] ])
    bar_staff_obj.append([ staff_mean[12], staff_mean[13], staff_mean[1], staff_mean[27] ])
    bar_staff_obj.append(['test'])
    bar_staff_obj.append([ staff_mean[7], staff_mean[25], staff_mean[26], staff_mean[29], staff_mean[35] ])

    row1_1, row1_2, row1_3 = st.columns((1, 3, 1))
    
    with row1_2:
        # Radar Graph
        # Set data

        radar_df = pd.DataFrame({
        'group': ['Manager','Staff'],
        'Objective 1': [managers_objective[0].mean(), staff_objective[0].mean()],
        'Objective 2': [managers_objective[1].mean(), staff_objective[1].mean()],
        'Objective 3': [managers_objective[2].mean(), staff_objective[2].mean()],
        'Objective 4': [managers_objective[3].mean(), staff_objective[3].mean()],
        'Objective 5': [managers_objective[4].mean(), staff_objective[4].mean()],
        'Objective 6': [managers_objective[5].mean(), staff_objective[5].mean()],
        'Objective 7': [managers_objective[6].mean(), staff_objective[6].mean()],
        'Objective 9': [
            managers_objective[8].mean(), 
            staff_objective[8].mean()]
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
    
    bar_objective = []
    
    with row2_2:
        bar_objective.append([ label_objective[0], bar_managers_obj[0], bar_staff_obj[0] ])

        X = np.arange(5)
        width = 0.5  # the width of the bars

        # fig, ax = plt.subplots()
        rects1 = ax.bar(X - width/2, bar_objective[0][1], width, label='Managers')
        rects2 = ax.bar(X + width/2, bar_objective[0][2], width, label='Staff')

        fig = plt.figure(figsize=(14, 8))
        ax = fig.add_axes([0,0,1,1])

        ax.set_ylabel('Rating')
        ax.set_title("Objective 1: To  determine the employees' extent of understanding of the company's vision, mission, quality policy, purposes and directions")
        ax.set_xticks(X, bar_objective[0][0])

        ax.bar(X + 0.00, bar_objective[0][1],  width = 0.25)
        ax.bar(X + 0.25, bar_objective[0][2],  width = 0.25)

        ax.legend(labels=['Managers', 'Staff'])

        ax.bar_label(rects1)
        ax.bar_label(rects2)
        st.pyplot(fig)
        
        
    row3_1, row3_2, row3_3 = st.columns((1, 3, 1))      
    
    with row3_2:
        bar_objective.append([ label_objective[1], bar_managers_obj[1], bar_staff_obj[1]])

        X = np.arange(5)
        width = 0.5  # the width of the bars
        rects1 = ax.bar(X - width/2, bar_objective[1][1], width, label='Managers')
        rects2 = ax.bar(X + width/2, bar_objective[1][2], width, label='Staff')

        fig = plt.figure(figsize=(14, 8))
        ax = fig.add_axes([0,0,1,1])

        ax.set_ylabel('Rating')
        ax.set_title("Objective 2: To find out the employees’ perception of the company’s leadership")
        ax.set_xticks(X, bar_objective[1][0])

        ax.bar(X + 0.00, bar_objective[1][1],  width = 0.25)
        ax.bar(X + 0.25, bar_objective[1][2],  width = 0.25)

        ax.legend(labels=['Managers', 'Staff'])

        ax.bar_label(rects1)
        ax.bar_label(rects2)
        st.pyplot(fig)
        
    row4_1, row4_2, row4_3 = st.columns((1, 3, 1))      
    
    with row4_2:
        bar_objective.append([ label_objective[2], bar_managers_obj[2], bar_staff_obj[2]])

        X = np.arange(5)
        width = 0.5  # the width of the bars
        rects1 = ax.bar(X - width/2, bar_objective[2][1], width, label='Managers')
        rects2 = ax.bar(X + width/2, bar_objective[2][2], width, label='Staff')

        fig = plt.figure(figsize=(14, 8))
        ax = fig.add_axes([0,0,1,1])

        ax.set_ylabel('Rating')
        ax.set_title("Objective 3: To have an indication of the employee supervisor relationships in the company")
        ax.set_xticks(X, bar_objective[2][0])

        ax.bar(X + 0.00, bar_objective[2][1],  width = 0.25)
        ax.bar(X + 0.25, bar_objective[2][2],  width = 0.25)

        ax.legend(labels=['Managers', 'Staff'])

        ax.bar_label(rects1)
        ax.bar_label(rects2)
        st.pyplot(fig)
        
    row5_1, row5_2, row5_3 = st.columns((1, 3, 1)) 
    with row5_2:
        bar_objective.append([ label_objective[3], bar_managers_obj[3], bar_staff_obj[3]])

        X = np.arange(5)
        width = 0.5  # the width of the bars
        rects1 = ax.bar(X - width/2, bar_objective[3][1], width, label='Managers')
        rects2 = ax.bar(X + width/2, bar_objective[3][2], width, label='Staff')

        fig = plt.figure(figsize=(14, 8))
        ax = fig.add_axes([0,0,1,1])

        ax.set_ylabel('Rating')
        ax.set_title("Objective 4: Evaluate  the pervading  conditions for  Total Quality Implementation")
        ax.set_xticks(X, bar_objective[3][0])

        ax.bar(X + 0.00, bar_objective[3][1],  width = 0.25)
        ax.bar(X + 0.25, bar_objective[3][2],  width = 0.25)

        ax.legend(labels=['Managers', 'Staff'])

        ax.bar_label(rects1)
        ax.bar_label(rects2)
        st.pyplot(fig)
        
    row6_1, row6_2, row6_3 = st.columns((1, 3, 1)) 
    with row6_2:
        bar_objective.append([ label_objective[4], bar_managers_obj[4], bar_staff_obj[4]])

        X = np.arange(5)
        width = 0.5  # the width of the bars
        rects1 = ax.bar(X - width/2, bar_objective[4][1], width, label='Managers')
        rects2 = ax.bar(X + width/2, bar_objective[4][2], width, label='Staff')

        fig = plt.figure(figsize=(14, 8))
        ax = fig.add_axes([0,0,1,1])

        ax.set_ylabel('Rating')
        ax.set_title("Objective 5: Find out if strategic plans were prepared, evaluated and shared company-wide")
        ax.set_xticks(X, bar_objective[4][0])

        ax.bar(X + 0.00, bar_objective[4][1],  width = 0.25)
        ax.bar(X + 0.25, bar_objective[4][2],  width = 0.25)

        ax.legend(labels=['Managers', 'Staff'])

        ax.bar_label(rects1)
        ax.bar_label(rects2)
        st.pyplot(fig)

    row7_1, row7_2, row7_3 = st.columns((1, 3, 1)) 
    with row7_2:
        bar_objective.append([ label_objective[5], bar_managers_obj[5], bar_staff_obj[5]])

        X = np.arange(5)
        width = 0.5  # the width of the bars
        rects1 = ax.bar(X - width/2, bar_objective[5][1], width, label='Managers')
        rects2 = ax.bar(X + width/2, bar_objective[5][2], width, label='Staff')

        fig = plt.figure(figsize=(14, 8))
        ax = fig.add_axes([0,0,1,1])

        ax.set_ylabel('Rating')
        ax.set_title("Objective 6: To find out the Company’s willingness to change towards a TQM direction")
        ax.set_xticks(X, bar_objective[5][0])

        ax.bar(X + 0.00, bar_objective[5][1],  width = 0.25)
        ax.bar(X + 0.25, bar_objective[5][2],  width = 0.25)

        ax.legend(labels=['Managers', 'Staff'])

        ax.bar_label(rects1)
        ax.bar_label(rects2)
        st.pyplot(fig)
        

    row8_1, row8_2, row8_3 = st.columns((1, 3, 1)) 
    with row8_2:
        bar_objective.append([ label_objective[6], bar_managers_obj[6], bar_staff_obj[6]])

        X = np.arange(4)
        width = 0.5  # the width of the bars
        rects1 = ax.bar(X - width/2, bar_objective[6][1], width, label='Managers')
        rects2 = ax.bar(X + width/2, bar_objective[6][2], width, label='Staff')

        fig = plt.figure(figsize=(14, 8))
        ax = fig.add_axes([0,0,1,1])

        ax.set_ylabel('Rating')
        ax.set_title("Objective 7: Understand the management’s extent of support towards TQM")
        ax.set_xticks(X, bar_objective[6][0])

        ax.bar(X + 0.00, bar_objective[6][1],  width = 0.25)
        ax.bar(X + 0.25, bar_objective[6][2],  width = 0.25)

        ax.legend(labels=['Managers', 'Staff'])

        ax.bar_label(rects1)
        ax.bar_label(rects2)
        st.pyplot(fig) 
        

    row9_1, row9_2, row9_3 = st.columns((1, 3, 1)) 
    with row9_2:
        bar_objective.append([ label_objective[7], bar_managers_obj[7], bar_staff_obj[7]])

        X = np.arange(10)
        width = 0.5  # the width of the bars
        rects1 = ax.bar(X - width/2, bar_objective[7][1], width, label='Managers')
#         rects2 = ax.bar(X + width/2, bar_objective[8][2], width, label='Staff')

        fig = plt.figure(figsize=(14, 8))
        ax = fig.add_axes([0,0,1,1])

        ax.set_ylabel('Rating')
        ax.set_title("Objective 8: To know the Management's TQM perspectives")
        ax.set_xticks(X, bar_objective[7][0])

        ax.bar(X + 0.00, bar_objective[7][1],  width = 0.25)
#         ax.bar(X + 0.25, bar_objective[7][2],  width = 0.25)

        ax.legend(labels=['Managers'])

        ax.bar_label(rects1)
#         ax.bar_label(rects2)
        st.pyplot(fig)
    
    row10_1, row10_2, row10_3 = st.columns((1, 3, 1)) 
    
    with row10_2:
        bar_objective.append([ label_objective[8], bar_managers_obj[8], bar_staff_obj[8]])

        X = np.arange(5)
        width = 0.5  # the width of the bars
        rects1 = ax.bar(X - width/2, bar_objective[8][1], width, label='Managers')
        rects2 = ax.bar(X + width/2, bar_objective[8][2], width, label='Staff')

        fig = plt.figure(figsize=(14, 8))
        ax = fig.add_axes([0,0,1,1])

        ax.set_ylabel('Rating')
        ax.set_title("Objective 9: To know the Company’s extent of resiliency")
        ax.set_xticks(X, bar_objective[8][0])

        ax.bar(X + 0.00, bar_objective[8][1],  width = 0.25)
        ax.bar(X + 0.25, bar_objective[8][2],  width = 0.25)

        ax.legend(labels=['Managers'])

        ax.bar_label(rects1)
        ax.bar_label(rects2)
        st.pyplot(fig)

# Region-CAR : Start

if menu == 'Cordillera Administrative Region (CAR)':
    region = 'Cordillera Administrative Region (CAR)'
    st.header(region)
    toggle = True

    st.sidebar.title('Actions')
    toggle = st.sidebar.button('VFM Food Products')

    region12_df = survey_df[survey_df["What region are you from?"] == region]

    firm_df = survey_df[survey_df["Name of Your Company:"] == 'VFM Food Products']
    firm_df
    if toggle:
        firm = 'VFM Food Products'
        st.subheader(firm)
        firm_df = survey_df[survey_df["Name of Your Company:"] == firm]
        st.write(firm_df)
       
    # Management / Staff
    firm_respondents_group = firm_df['Are you part of Management or Staff?']
    group_df = np.asarray(firm_respondents_group)
    group, group_counts = np.unique(group_df, return_counts=True)

    # Gender
    firm_respondents_sex = firm_df['What is your sex?']
    sex_df = np.asarray(firm_respondents_sex)
    gender, gender_counts = np.unique(sex_df, return_counts=True)

    # Age Group
    firm_respondents_age_group = firm_df['What age group do you belong to?']
    age_group_df = np.asarray(firm_respondents_age_group)
    age_group, age_group_counts = np.unique(age_group_df, return_counts=True)

    # Education
    firm_respondents_education = firm_df['What is your highest education attainment?']
    education_df = np.asarray(firm_respondents_education)
    education, education_counts = np.unique(education_df, return_counts=True)

    st.subheader('Demographics')

    row1_1, row1_2, row1_3, row1_4 = st.columns((1,1,1,1))
    with row1_1:
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

#     row2_1, row2_2= st.columns((2, 2))
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

    st.subheader('Survey Results')

    firm_managers = firm_df[firm_df["Are you part of Management or Staff?"] == "Management"]
    firm_staff = firm_df[firm_df["Are you part of Management or Staff?"] == "Staff"]

    np_firm_managers = np.asarray(firm_managers)
    np_firm_staff = np.asarray(firm_staff)

    managers_mean = np.mean(np_firm_managers[:,9:59], axis=0)

    # title
    objective_title = []
    objective_title.append("Objective 1: To  determine the employees' extent of understanding of the company's vision, mission, quality policy, purposes and directions")
    objective_title.append("Objective 2: To find out the employees’ perception of the company’s leadership")
    objective_title.append("Objective 3: To have an indication of the employee supervisor relationships in the company")
    objective_title.append("Objective 4: Evaluate  the pervading  conditions for  Total Quality Implementation")
    objective_title.append("Objective 5: Find out if strategic plans were prepared, evaluated and shared company-wide")
    objective_title.append("Objective 6: To find out the Company’s willingness to change towards a TQM direction")
    objective_title.append("Objective 7: Understand the management’s extent of support towards TQM")
    objective_title.append("Objective 8: To know the Management's TQM perspectives")
    objective_title.append("Objective 9: To know the Company’s extent of resiliency")

    # Labels
    label_objective = []
    label_objective.append(['Q6', 'Q12', 'Q20', 'Q37', 'Q38'])
    label_objective.append(['Q4', 'Q7', 'Q9', 'Q34', 'Q35'])
    label_objective.append(['Q2', 'Q3', 'Q10', 'Q22', 'Q23'])
    label_objective.append(['Q15', 'Q16', 'Q17', 'Q24', 'Q39'])
    label_objective.append(['Q1', 'Q10', 'Q31', 'Q32', 'Q40'])
    label_objective.append(['Q5', 'Q19', 'Q21', 'Q29', 'Q33'])
    label_objective.append(['Q13', 'Q14', 'Q18', 'Q28'])
    label_objective.append(['Q41', 'Q42', 'Q43', 'Q44', 'Q45', 'Q46', 'Q47', 'Q48', 'Q49', 'Q50'])
    label_objective.append(['Q8', 'Q26', 'Q27', 'Q30', 'Q36'])

    # Managers data
    firm_managers_obj = []
    firm_managers_obj.append(np.asarray([ managers_mean[5], managers_mean[11], managers_mean[19], managers_mean[36], managers_mean[37] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[3], managers_mean[6], managers_mean[8], managers_mean[33], managers_mean[34] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[1], managers_mean[2], managers_mean[9], managers_mean[21], managers_mean[22] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[14], managers_mean[15], managers_mean[16], managers_mean[23], managers_mean[38] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[0], managers_mean[9], managers_mean[30], managers_mean[31], managers_mean[39] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[4], managers_mean[18], managers_mean[20], managers_mean[28], managers_mean[32] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[12], managers_mean[13], managers_mean[1], managers_mean[27] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[40], managers_mean[41], managers_mean[42], managers_mean[43], managers_mean[44], managers_mean[45], managers_mean[46], managers_mean[47], managers_mean[48], managers_mean[49] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[7], managers_mean[25], managers_mean[26], managers_mean[29], managers_mean[35] ]))


    staff_mean = np.mean(np_firm_staff[:,59:99], axis=0)
    # Staff data
    firm_staff_obj = []
    firm_staff_obj.append(np.asarray([ staff_mean[5], staff_mean[11], staff_mean[19], staff_mean[36], staff_mean[37] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[2], staff_mean[6], staff_mean[8], staff_mean[33], staff_mean[34] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[1], staff_mean[2], staff_mean[9], staff_mean[21], staff_mean[22] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[14], staff_mean[15], staff_mean[16], staff_mean[23], staff_mean[38] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[0], staff_mean[9], staff_mean[30], staff_mean[31], staff_mean[39] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[4], staff_mean[18], staff_mean[20], staff_mean[28], staff_mean[32] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[12], staff_mean[13], staff_mean[1], staff_mean[27] ]))
    firm_staff_obj.append(['test'])
    firm_staff_obj.append(np.asarray([ staff_mean[7], staff_mean[25], staff_mean[26], staff_mean[29], staff_mean[35] ]))

    radar_df = pd.DataFrame({
        'group': ['Manager','Staff'],
        'Objective 1': [firm_managers_obj[0].mean(), firm_staff_obj[0].mean()],
        'Objective 2': [firm_managers_obj[1].mean(), firm_staff_obj[1].mean()],
        'Objective 3': [firm_managers_obj[2].mean(), firm_staff_obj[2].mean()],
        'Objective 4': [firm_managers_obj[3].mean(), firm_staff_obj[3].mean()],
        'Objective 5': [firm_managers_obj[4].mean(), firm_staff_obj[4].mean()],
        'Objective 6': [firm_managers_obj[5].mean(), firm_staff_obj[5].mean()],
        'Objective 7': [firm_managers_obj[6].mean(), firm_staff_obj[6].mean()],
        'Objective 9': [firm_managers_obj[8].mean(), firm_staff_obj[8].mean()]
        })

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

    firm_objective = []

    i = 0
    while i < len(objective_title):

        row1_1, row1_2, row1_3 = st.columns((1,3,1))

        with row1_2:
            firm_objective.append([ label_objective[i], firm_managers_obj[i], firm_staff_obj[i] ])

            X = np.arange(len(label_objective[i]))
            width = 0.5  # the width of the bars

            fig, ax = plt.subplots()
            rects1 = ax.bar(X - width/2, firm_objective[i][1], width, label='Managers')
            if i != 7:
                rects2 = ax.bar(X + width/2, firm_objective[i][2], width, label='Staff')

            fig = plt.figure(figsize=(14, 8))
            ax = fig.add_axes([0,0,1,1])

            ax.set_ylabel('Rating')
            ax.set_title(objective_title[i])
            ax.set_xticks(X, firm_objective[i][0])

            ax.bar(X + 0.00, firm_objective[i][1],  width = 0.25)
            if i != 7:
                ax.bar(X + 0.25, firm_objective[i][2],  width = 0.25)

            if i != 7:
                ax.legend(labels=['Managers', 'Staff'])
            else:
                ax.legend(labels=['Managers'])

            ax.bar_label(rects1)
            ax.bar_label(rects2)
            st.pyplot(fig)

        i += 1
        
# Region-CAR : End

# Region-NCR : Start

if menu == 'National Capital Region (NCR)':
    region = 'National Capital Region (NCR)'
    st.header(region)
    toggle = True

    st.sidebar.title('Actions')
    toggle = st.sidebar.button('Aretei Foods Corp.')

    region12_df = survey_df[survey_df["What region are you from?"] == region]

    firm_df = survey_df[survey_df["Name of Your Company:"] == 'Aretei Foods Corp.']
    firm_df
    if toggle:
        firm = 'Aretei Foods Corp.'
        st.subheader(firm)
        firm_df = survey_df[survey_df["Name of Your Company:"] == firm]
        st.write(firm_df)
       
    # Management / Staff
    firm_respondents_group = firm_df['Are you part of Management or Staff?']
    group_df = np.asarray(firm_respondents_group)
    group, group_counts = np.unique(group_df, return_counts=True)

    # Gender
    firm_respondents_sex = firm_df['What is your sex?']
    sex_df = np.asarray(firm_respondents_sex)
    gender, gender_counts = np.unique(sex_df, return_counts=True)

    # Age Group
    firm_respondents_age_group = firm_df['What age group do you belong to?']
    age_group_df = np.asarray(firm_respondents_age_group)
    age_group, age_group_counts = np.unique(age_group_df, return_counts=True)

    # Education
    firm_respondents_education = firm_df['What is your highest education attainment?']
    education_df = np.asarray(firm_respondents_education)
    education, education_counts = np.unique(education_df, return_counts=True)

    st.subheader('Demographics')

    row1_1, row1_2, row1_3, row1_4 = st.columns((1,1,1,1))
    with row1_1:
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

#     row2_1, row2_2= st.columns((2, 2))
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

    st.subheader('Survey Results')

    firm_managers = firm_df[firm_df["Are you part of Management or Staff?"] == "Management"]
    firm_staff = firm_df[firm_df["Are you part of Management or Staff?"] == "Staff"]

    np_firm_managers = np.asarray(firm_managers)
    np_firm_staff = np.asarray(firm_staff)

    managers_mean = np.mean(np_firm_managers[:,9:59], axis=0)

    # title
    objective_title = []
    objective_title.append("Objective 1: To  determine the employees' extent of understanding of the company's vision, mission, quality policy, purposes and directions")
    objective_title.append("Objective 2: To find out the employees’ perception of the company’s leadership")
    objective_title.append("Objective 3: To have an indication of the employee supervisor relationships in the company")
    objective_title.append("Objective 4: Evaluate  the pervading  conditions for  Total Quality Implementation")
    objective_title.append("Objective 5: Find out if strategic plans were prepared, evaluated and shared company-wide")
    objective_title.append("Objective 6: To find out the Company’s willingness to change towards a TQM direction")
    objective_title.append("Objective 7: Understand the management’s extent of support towards TQM")
    objective_title.append("Objective 8: To know the Management's TQM perspectives")
    objective_title.append("Objective 9: To know the Company’s extent of resiliency")

    # Labels
    label_objective = []
    label_objective.append(['Q6', 'Q12', 'Q20', 'Q37', 'Q38'])
    label_objective.append(['Q4', 'Q7', 'Q9', 'Q34', 'Q35'])
    label_objective.append(['Q2', 'Q3', 'Q10', 'Q22', 'Q23'])
    label_objective.append(['Q15', 'Q16', 'Q17', 'Q24', 'Q39'])
    label_objective.append(['Q1', 'Q10', 'Q31', 'Q32', 'Q40'])
    label_objective.append(['Q5', 'Q19', 'Q21', 'Q29', 'Q33'])
    label_objective.append(['Q13', 'Q14', 'Q18', 'Q28'])
    label_objective.append(['Q41', 'Q42', 'Q43', 'Q44', 'Q45', 'Q46', 'Q47', 'Q48', 'Q49', 'Q50'])
    label_objective.append(['Q8', 'Q26', 'Q27', 'Q30', 'Q36'])

    # Managers data
    firm_managers_obj = []
    firm_managers_obj.append(np.asarray([ managers_mean[5], managers_mean[11], managers_mean[19], managers_mean[36], managers_mean[37] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[3], managers_mean[6], managers_mean[8], managers_mean[33], managers_mean[34] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[1], managers_mean[2], managers_mean[9], managers_mean[21], managers_mean[22] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[14], managers_mean[15], managers_mean[16], managers_mean[23], managers_mean[38] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[0], managers_mean[9], managers_mean[30], managers_mean[31], managers_mean[39] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[4], managers_mean[18], managers_mean[20], managers_mean[28], managers_mean[32] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[12], managers_mean[13], managers_mean[1], managers_mean[27] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[40], managers_mean[41], managers_mean[42], managers_mean[43], managers_mean[44], managers_mean[45], managers_mean[46], managers_mean[47], managers_mean[48], managers_mean[49] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[7], managers_mean[25], managers_mean[26], managers_mean[29], managers_mean[35] ]))


    staff_mean = np.mean(np_firm_staff[:,59:99], axis=0)
    # Staff data
    firm_staff_obj = []
    firm_staff_obj.append(np.asarray([ staff_mean[5], staff_mean[11], staff_mean[19], staff_mean[36], staff_mean[37] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[2], staff_mean[6], staff_mean[8], staff_mean[33], staff_mean[34] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[1], staff_mean[2], staff_mean[9], staff_mean[21], staff_mean[22] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[14], staff_mean[15], staff_mean[16], staff_mean[23], staff_mean[38] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[0], staff_mean[9], staff_mean[30], staff_mean[31], staff_mean[39] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[4], staff_mean[18], staff_mean[20], staff_mean[28], staff_mean[32] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[12], staff_mean[13], staff_mean[1], staff_mean[27] ]))
    firm_staff_obj.append(['test'])
    firm_staff_obj.append(np.asarray([ staff_mean[7], staff_mean[25], staff_mean[26], staff_mean[29], staff_mean[35] ]))

    radar_df = pd.DataFrame({
        'group': ['Manager','Staff'],
        'Objective 1': [firm_managers_obj[0].mean(), firm_staff_obj[0].mean()],
        'Objective 2': [firm_managers_obj[1].mean(), firm_staff_obj[1].mean()],
        'Objective 3': [firm_managers_obj[2].mean(), firm_staff_obj[2].mean()],
        'Objective 4': [firm_managers_obj[3].mean(), firm_staff_obj[3].mean()],
        'Objective 5': [firm_managers_obj[4].mean(), firm_staff_obj[4].mean()],
        'Objective 6': [firm_managers_obj[5].mean(), firm_staff_obj[5].mean()],
        'Objective 7': [firm_managers_obj[6].mean(), firm_staff_obj[6].mean()],
        'Objective 9': [firm_managers_obj[8].mean(), firm_staff_obj[8].mean()]
        })

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
        
    firm_objective = []

    i = 0
    while i < len(objective_title):

        row1_1, row1_2, row1_3 = st.columns((1,3,1))

        with row1_2:
            firm_objective.append([ label_objective[i], firm_managers_obj[i], firm_staff_obj[i] ])

            X = np.arange(len(label_objective[i]))
            width = 0.5  # the width of the bars

            fig, ax = plt.subplots()
            rects1 = ax.bar(X - width/2, firm_objective[i][1], width, label='Managers')
            if i != 7:
                rects2 = ax.bar(X + width/2, firm_objective[i][2], width, label='Staff')

            fig = plt.figure(figsize=(14, 8))
            ax = fig.add_axes([0,0,1,1])

            ax.set_ylabel('Rating')
            ax.set_title(objective_title[i])
            ax.set_xticks(X, firm_objective[i][0])

            ax.bar(X + 0.00, firm_objective[i][1],  width = 0.25)
            if i != 7:
                ax.bar(X + 0.25, firm_objective[i][2],  width = 0.25)

            if i != 7:
                ax.legend(labels=['Managers', 'Staff'])
            else:
                ax.legend(labels=['Managers'])

            ax.bar_label(rects1)
            ax.bar_label(rects2)
            st.pyplot(fig)

        i += 1
        
# Region-NCR : End

# Region-I : Start

if menu == 'Region I: Ilocos Region':
    region = 'Region I: Ilocos Region'
    st.header(region)
    toggle = True

    st.sidebar.title('Actions')
    toggle = st.sidebar.button('Nutridense Food Manufacturing Corp')

    region12_df = survey_df[survey_df["What region are you from?"] == region]

    firm_df = survey_df[survey_df["Name of Your Company:"] == 'Nutridense Food Manufacturing Corp']
    firm_df
    if toggle:
        firm = 'Nutridense Food Manufacturing Corp'
        st.subheader(firm)
        firm_df = survey_df[survey_df["Name of Your Company:"] == firm]
        st.write(firm_df)
       
    # Management / Staff
    firm_respondents_group = firm_df['Are you part of Management or Staff?']
    group_df = np.asarray(firm_respondents_group)
    group, group_counts = np.unique(group_df, return_counts=True)

    # Gender
    firm_respondents_sex = firm_df['What is your sex?']
    sex_df = np.asarray(firm_respondents_sex)
    gender, gender_counts = np.unique(sex_df, return_counts=True)

    # Age Group
    firm_respondents_age_group = firm_df['What age group do you belong to?']
    age_group_df = np.asarray(firm_respondents_age_group)
    age_group, age_group_counts = np.unique(age_group_df, return_counts=True)

    # Education
    firm_respondents_education = firm_df['What is your highest education attainment?']
    education_df = np.asarray(firm_respondents_education)
    education, education_counts = np.unique(education_df, return_counts=True)

    st.subheader('Demographics')

    row1_1, row1_2, row1_3, row1_4 = st.columns((1,1,1,1))
    with row1_1:
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

#     row2_1, row2_2= st.columns((2, 2))
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

    st.subheader('Survey Results')

    firm_managers = firm_df[firm_df["Are you part of Management or Staff?"] == "Management"]
    firm_staff = firm_df[firm_df["Are you part of Management or Staff?"] == "Staff"]

    np_firm_managers = np.asarray(firm_managers)
    np_firm_staff = np.asarray(firm_staff)

    managers_mean = np.mean(np_firm_managers[:,9:59], axis=0)

    # title
    objective_title = []
    objective_title.append("Objective 1: To  determine the employees' extent of understanding of the company's vision, mission, quality policy, purposes and directions")
    objective_title.append("Objective 2: To find out the employees’ perception of the company’s leadership")
    objective_title.append("Objective 3: To have an indication of the employee supervisor relationships in the company")
    objective_title.append("Objective 4: Evaluate  the pervading  conditions for  Total Quality Implementation")
    objective_title.append("Objective 5: Find out if strategic plans were prepared, evaluated and shared company-wide")
    objective_title.append("Objective 6: To find out the Company’s willingness to change towards a TQM direction")
    objective_title.append("Objective 7: Understand the management’s extent of support towards TQM")
    objective_title.append("Objective 8: To know the Management's TQM perspectives")
    objective_title.append("Objective 9: To know the Company’s extent of resiliency")

    # Labels
    label_objective = []
    label_objective.append(['Q6', 'Q12', 'Q20', 'Q37', 'Q38'])
    label_objective.append(['Q4', 'Q7', 'Q9', 'Q34', 'Q35'])
    label_objective.append(['Q2', 'Q3', 'Q10', 'Q22', 'Q23'])
    label_objective.append(['Q15', 'Q16', 'Q17', 'Q24', 'Q39'])
    label_objective.append(['Q1', 'Q10', 'Q31', 'Q32', 'Q40'])
    label_objective.append(['Q5', 'Q19', 'Q21', 'Q29', 'Q33'])
    label_objective.append(['Q13', 'Q14', 'Q18', 'Q28'])
    label_objective.append(['Q41', 'Q42', 'Q43', 'Q44', 'Q45', 'Q46', 'Q47', 'Q48', 'Q49', 'Q50'])
    label_objective.append(['Q8', 'Q26', 'Q27', 'Q30', 'Q36'])

    # Managers data
    firm_managers_obj = []
    firm_managers_obj.append(np.asarray([ managers_mean[5], managers_mean[11], managers_mean[19], managers_mean[36], managers_mean[37] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[3], managers_mean[6], managers_mean[8], managers_mean[33], managers_mean[34] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[1], managers_mean[2], managers_mean[9], managers_mean[21], managers_mean[22] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[14], managers_mean[15], managers_mean[16], managers_mean[23], managers_mean[38] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[0], managers_mean[9], managers_mean[30], managers_mean[31], managers_mean[39] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[4], managers_mean[18], managers_mean[20], managers_mean[28], managers_mean[32] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[12], managers_mean[13], managers_mean[1], managers_mean[27] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[40], managers_mean[41], managers_mean[42], managers_mean[43], managers_mean[44], managers_mean[45], managers_mean[46], managers_mean[47], managers_mean[48], managers_mean[49] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[7], managers_mean[25], managers_mean[26], managers_mean[29], managers_mean[35] ]))


    staff_mean = np.mean(np_firm_staff[:,59:99], axis=0)
    # Staff data
    firm_staff_obj = []
    firm_staff_obj.append(np.asarray([ staff_mean[5], staff_mean[11], staff_mean[19], staff_mean[36], staff_mean[37] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[2], staff_mean[6], staff_mean[8], staff_mean[33], staff_mean[34] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[1], staff_mean[2], staff_mean[9], staff_mean[21], staff_mean[22] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[14], staff_mean[15], staff_mean[16], staff_mean[23], staff_mean[38] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[0], staff_mean[9], staff_mean[30], staff_mean[31], staff_mean[39] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[4], staff_mean[18], staff_mean[20], staff_mean[28], staff_mean[32] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[12], staff_mean[13], staff_mean[1], staff_mean[27] ]))
    firm_staff_obj.append(['test'])
    firm_staff_obj.append(np.asarray([ staff_mean[7], staff_mean[25], staff_mean[26], staff_mean[29], staff_mean[35] ]))

    radar_df = pd.DataFrame({
        'group': ['Manager','Staff'],
        'Objective 1': [firm_managers_obj[0].mean(), firm_staff_obj[0].mean()],
        'Objective 2': [firm_managers_obj[1].mean(), firm_staff_obj[1].mean()],
        'Objective 3': [firm_managers_obj[2].mean(), firm_staff_obj[2].mean()],
        'Objective 4': [firm_managers_obj[3].mean(), firm_staff_obj[3].mean()],
        'Objective 5': [firm_managers_obj[4].mean(), firm_staff_obj[4].mean()],
        'Objective 6': [firm_managers_obj[5].mean(), firm_staff_obj[5].mean()],
        'Objective 7': [firm_managers_obj[6].mean(), firm_staff_obj[6].mean()],
        'Objective 9': [firm_managers_obj[8].mean(), firm_staff_obj[8].mean()]
        })

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


    firm_objective = []

    i = 0
    while i < len(objective_title):

        row1_1, row1_2, row1_3 = st.columns((1,3,1))

        with row1_2:
            firm_objective.append([ label_objective[i], firm_managers_obj[i], firm_staff_obj[i] ])

            X = np.arange(len(label_objective[i]))
            width = 0.5  # the width of the bars

            fig, ax = plt.subplots()
            rects1 = ax.bar(X - width/2, firm_objective[i][1], width, label='Managers')
            if i != 7:
                rects2 = ax.bar(X + width/2, firm_objective[i][2], width, label='Staff')

            fig = plt.figure(figsize=(14, 8))
            ax = fig.add_axes([0,0,1,1])

            ax.set_ylabel('Rating')
            ax.set_title(objective_title[i])
            ax.set_xticks(X, firm_objective[i][0])

            ax.bar(X + 0.00, firm_objective[i][1],  width = 0.25)
            if i != 7:
                ax.bar(X + 0.25, firm_objective[i][2],  width = 0.25)

            if i != 7:
                ax.legend(labels=['Managers', 'Staff'])
            else:
                ax.legend(labels=['Managers'])

            ax.bar_label(rects1)
            ax.bar_label(rects2)
            st.pyplot(fig)

        i += 1
        
# Region-I : End

# Region-II : Start

if menu == 'Region II: Cagayan Valley':
    region = 'Region II: Cagayan Valley'
    st.header(region)
    toggle = True

    st.sidebar.title('Actions')
    toggle = st.sidebar.button('Agri-Component Machineries and Construction Corporation (AMCC)')
    toggle = st.sidebar.button('Honey Buns Bakeshop')

    region12_df = survey_df[survey_df["What region are you from?"] == region]

    firm_df = survey_df[survey_df["Name of Your Company:"] == 'Agri-Component Machineries and Construction Corporation (AMCC)']
    firm_df

    if toggle:
        firm = 'Agri-Component Machineries and Construction Corporation (AMCC)'
        st.subheader(firm)
        firm_df = survey_df[survey_df["Name of Your Company:"] == firm]
        st.write(firm_df)
    else:
        firm = 'Honey Buns Bakeshop'
        st.subheader(firm)
        firm_df = survey_df[survey_df["Name of Your Company:"] == firm]
        st.write(firm_df)
   
    # Management / Staff
    firm_respondents_group = firm_df['Are you part of Management or Staff?']
    group_df = np.asarray(firm_respondents_group)
    group, group_counts = np.unique(group_df, return_counts=True)

    # Gender
    firm_respondents_sex = firm_df['What is your sex?']
    sex_df = np.asarray(firm_respondents_sex)
    gender, gender_counts = np.unique(sex_df, return_counts=True)

    # Age Group
    firm_respondents_age_group = firm_df['What age group do you belong to?']
    age_group_df = np.asarray(firm_respondents_age_group)
    age_group, age_group_counts = np.unique(age_group_df, return_counts=True)

    # Education
    firm_respondents_education = firm_df['What is your highest education attainment?']
    education_df = np.asarray(firm_respondents_education)
    education, education_counts = np.unique(education_df, return_counts=True)

    st.subheader('Demographics')

    row1_1, row1_2, row1_3, row1_4 = st.columns((1,1,1,1))
    with row1_1:
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

#     row2_1, row2_2= st.columns((2, 2))
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

    st.subheader('Survey Results')

    firm_managers = firm_df[firm_df["Are you part of Management or Staff?"] == "Management"]
    firm_staff = firm_df[firm_df["Are you part of Management or Staff?"] == "Staff"]

    np_firm_managers = np.asarray(firm_managers)
    np_firm_staff = np.asarray(firm_staff)

    managers_mean = np.mean(np_firm_managers[:,9:59], axis=0)

    # title
    objective_title = []
    objective_title.append("Objective 1: To  determine the employees' extent of understanding of the company's vision, mission, quality policy, purposes and directions")
    objective_title.append("Objective 2: To find out the employees’ perception of the company’s leadership")
    objective_title.append("Objective 3: To have an indication of the employee supervisor relationships in the company")
    objective_title.append("Objective 4: Evaluate  the pervading  conditions for  Total Quality Implementation")
    objective_title.append("Objective 5: Find out if strategic plans were prepared, evaluated and shared company-wide")
    objective_title.append("Objective 6: To find out the Company’s willingness to change towards a TQM direction")
    objective_title.append("Objective 7: Understand the management’s extent of support towards TQM")
    objective_title.append("Objective 8: To know the Management's TQM perspectives")
    objective_title.append("Objective 9: To know the Company’s extent of resiliency")

    # Labels
    label_objective = []
    label_objective.append(['Q6', 'Q12', 'Q20', 'Q37', 'Q38'])
    label_objective.append(['Q4', 'Q7', 'Q9', 'Q34', 'Q35'])
    label_objective.append(['Q2', 'Q3', 'Q10', 'Q22', 'Q23'])
    label_objective.append(['Q15', 'Q16', 'Q17', 'Q24', 'Q39'])
    label_objective.append(['Q1', 'Q10', 'Q31', 'Q32', 'Q40'])
    label_objective.append(['Q5', 'Q19', 'Q21', 'Q29', 'Q33'])
    label_objective.append(['Q13', 'Q14', 'Q18', 'Q28'])
    label_objective.append(['Q41', 'Q42', 'Q43', 'Q44', 'Q45', 'Q46', 'Q47', 'Q48', 'Q49', 'Q50'])
    label_objective.append(['Q8', 'Q26', 'Q27', 'Q30', 'Q36'])

    # Managers data
    firm_managers_obj = []
    firm_managers_obj.append(np.asarray([ managers_mean[5], managers_mean[11], managers_mean[19], managers_mean[36], managers_mean[37] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[3], managers_mean[6], managers_mean[8], managers_mean[33], managers_mean[34] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[1], managers_mean[2], managers_mean[9], managers_mean[21], managers_mean[22] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[14], managers_mean[15], managers_mean[16], managers_mean[23], managers_mean[38] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[0], managers_mean[9], managers_mean[30], managers_mean[31], managers_mean[39] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[4], managers_mean[18], managers_mean[20], managers_mean[28], managers_mean[32] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[12], managers_mean[13], managers_mean[1], managers_mean[27] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[40], managers_mean[41], managers_mean[42], managers_mean[43], managers_mean[44], managers_mean[45], managers_mean[46], managers_mean[47], managers_mean[48], managers_mean[49] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[7], managers_mean[25], managers_mean[26], managers_mean[29], managers_mean[35] ]))


    staff_mean = np.mean(np_firm_staff[:,59:99], axis=0)
    # Staff data
    firm_staff_obj = []
    firm_staff_obj.append(np.asarray([ staff_mean[5], staff_mean[11], staff_mean[19], staff_mean[36], staff_mean[37] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[2], staff_mean[6], staff_mean[8], staff_mean[33], staff_mean[34] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[1], staff_mean[2], staff_mean[9], staff_mean[21], staff_mean[22] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[14], staff_mean[15], staff_mean[16], staff_mean[23], staff_mean[38] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[0], staff_mean[9], staff_mean[30], staff_mean[31], staff_mean[39] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[4], staff_mean[18], staff_mean[20], staff_mean[28], staff_mean[32] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[12], staff_mean[13], staff_mean[1], staff_mean[27] ]))
    firm_staff_obj.append(['test'])
    firm_staff_obj.append(np.asarray([ staff_mean[7], staff_mean[25], staff_mean[26], staff_mean[29], staff_mean[35] ]))

    radar_df = pd.DataFrame({
        'group': ['Manager','Staff'],
        'Objective 1': [firm_managers_obj[0].mean(), firm_staff_obj[0].mean()],
        'Objective 2': [firm_managers_obj[1].mean(), firm_staff_obj[1].mean()],
        'Objective 3': [firm_managers_obj[2].mean(), firm_staff_obj[2].mean()],
        'Objective 4': [firm_managers_obj[3].mean(), firm_staff_obj[3].mean()],
        'Objective 5': [firm_managers_obj[4].mean(), firm_staff_obj[4].mean()],
        'Objective 6': [firm_managers_obj[5].mean(), firm_staff_obj[5].mean()],
        'Objective 7': [firm_managers_obj[6].mean(), firm_staff_obj[6].mean()],
        'Objective 9': [firm_managers_obj[8].mean(), firm_staff_obj[8].mean()]
        })

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


    firm_objective = []

    i = 0
    while i < len(objective_title):

        row1_1, row1_2, row1_3 = st.columns((1,3,1))

        with row1_2:
            firm_objective.append([ label_objective[i], firm_managers_obj[i], firm_staff_obj[i] ])

            X = np.arange(len(label_objective[i]))
            width = 0.5  # the width of the bars

            fig, ax = plt.subplots()
            rects1 = ax.bar(X - width/2, firm_objective[i][1], width, label='Managers')
            if i != 7:
                rects2 = ax.bar(X + width/2, firm_objective[i][2], width, label='Staff')

            fig = plt.figure(figsize=(14, 8))
            ax = fig.add_axes([0,0,1,1])

            ax.set_ylabel('Rating')
            ax.set_title(objective_title[i])
            ax.set_xticks(X, firm_objective[i][0])

            ax.bar(X + 0.00, firm_objective[i][1],  width = 0.25)
            if i != 7:
                ax.bar(X + 0.25, firm_objective[i][2],  width = 0.25)

            if i != 7:
                ax.legend(labels=['Managers', 'Staff'])
            else:
                ax.legend(labels=['Managers'])

            ax.bar_label(rects1)
            ax.bar_label(rects2)
            st.pyplot(fig)

        i += 1
        
# Region-II : End

# Region-III : Start

if menu == 'Region III: Central Luzon':
    region = 'Region III: Central Luzon'
    st.header(region)
    toggle = True

    st.sidebar.title('Actions')
    toggle = st.sidebar.button('Angel Farmers Gourmet Food Corporation')

    region12_df = survey_df[survey_df["What region are you from?"] == region]

    firm_df = survey_df[survey_df["Name of Your Company:"] == 'Angel Farmers Gourmet Food Corporation']
    firm_df

    if toggle:
        firm = 'Angel Farmers Gourmet Food Corporation'
        st.subheader(firm)
        firm_df = survey_df[survey_df["Name of Your Company:"] == firm]
        st.write(firm_df)
   
    # Management / Staff
    firm_respondents_group = firm_df['Are you part of Management or Staff?']
    group_df = np.asarray(firm_respondents_group)
    group, group_counts = np.unique(group_df, return_counts=True)

    # Gender
    firm_respondents_sex = firm_df['What is your sex?']
    sex_df = np.asarray(firm_respondents_sex)
    gender, gender_counts = np.unique(sex_df, return_counts=True)

    # Age Group
    firm_respondents_age_group = firm_df['What age group do you belong to?']
    age_group_df = np.asarray(firm_respondents_age_group)
    age_group, age_group_counts = np.unique(age_group_df, return_counts=True)

    # Education
    firm_respondents_education = firm_df['What is your highest education attainment?']
    education_df = np.asarray(firm_respondents_education)
    education, education_counts = np.unique(education_df, return_counts=True)

    st.subheader('Demographics')

    row1_1, row1_2, row1_3, row1_4 = st.columns((1,1,1,1))
    with row1_1:
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

#     row2_1, row2_2= st.columns((2, 2))
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

    st.subheader('Survey Results')

    firm_managers = firm_df[firm_df["Are you part of Management or Staff?"] == "Management"]
    firm_staff = firm_df[firm_df["Are you part of Management or Staff?"] == "Staff"]

    np_firm_managers = np.asarray(firm_managers)
    np_firm_staff = np.asarray(firm_staff)

    managers_mean = np.mean(np_firm_managers[:,9:59], axis=0)

    # title
    objective_title = []
    objective_title.append("Objective 1: To  determine the employees' extent of understanding of the company's vision, mission, quality policy, purposes and directions")
    objective_title.append("Objective 2: To find out the employees’ perception of the company’s leadership")
    objective_title.append("Objective 3: To have an indication of the employee supervisor relationships in the company")
    objective_title.append("Objective 4: Evaluate  the pervading  conditions for  Total Quality Implementation")
    objective_title.append("Objective 5: Find out if strategic plans were prepared, evaluated and shared company-wide")
    objective_title.append("Objective 6: To find out the Company’s willingness to change towards a TQM direction")
    objective_title.append("Objective 7: Understand the management’s extent of support towards TQM")
    objective_title.append("Objective 8: To know the Management's TQM perspectives")
    objective_title.append("Objective 9: To know the Company’s extent of resiliency")

    # Labels
    label_objective = []
    label_objective.append(['Q6', 'Q12', 'Q20', 'Q37', 'Q38'])
    label_objective.append(['Q4', 'Q7', 'Q9', 'Q34', 'Q35'])
    label_objective.append(['Q2', 'Q3', 'Q10', 'Q22', 'Q23'])
    label_objective.append(['Q15', 'Q16', 'Q17', 'Q24', 'Q39'])
    label_objective.append(['Q1', 'Q10', 'Q31', 'Q32', 'Q40'])
    label_objective.append(['Q5', 'Q19', 'Q21', 'Q29', 'Q33'])
    label_objective.append(['Q13', 'Q14', 'Q18', 'Q28'])
    label_objective.append(['Q41', 'Q42', 'Q43', 'Q44', 'Q45', 'Q46', 'Q47', 'Q48', 'Q49', 'Q50'])
    label_objective.append(['Q8', 'Q26', 'Q27', 'Q30', 'Q36'])

    # Managers data
    firm_managers_obj = []
    firm_managers_obj.append(np.asarray([ managers_mean[5], managers_mean[11], managers_mean[19], managers_mean[36], managers_mean[37] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[3], managers_mean[6], managers_mean[8], managers_mean[33], managers_mean[34] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[1], managers_mean[2], managers_mean[9], managers_mean[21], managers_mean[22] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[14], managers_mean[15], managers_mean[16], managers_mean[23], managers_mean[38] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[0], managers_mean[9], managers_mean[30], managers_mean[31], managers_mean[39] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[4], managers_mean[18], managers_mean[20], managers_mean[28], managers_mean[32] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[12], managers_mean[13], managers_mean[1], managers_mean[27] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[40], managers_mean[41], managers_mean[42], managers_mean[43], managers_mean[44], managers_mean[45], managers_mean[46], managers_mean[47], managers_mean[48], managers_mean[49] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[7], managers_mean[25], managers_mean[26], managers_mean[29], managers_mean[35] ]))


    staff_mean = np.mean(np_firm_staff[:,59:99], axis=0)
    # Staff data
    firm_staff_obj = []
    firm_staff_obj.append(np.asarray([ staff_mean[5], staff_mean[11], staff_mean[19], staff_mean[36], staff_mean[37] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[2], staff_mean[6], staff_mean[8], staff_mean[33], staff_mean[34] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[1], staff_mean[2], staff_mean[9], staff_mean[21], staff_mean[22] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[14], staff_mean[15], staff_mean[16], staff_mean[23], staff_mean[38] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[0], staff_mean[9], staff_mean[30], staff_mean[31], staff_mean[39] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[4], staff_mean[18], staff_mean[20], staff_mean[28], staff_mean[32] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[12], staff_mean[13], staff_mean[1], staff_mean[27] ]))
    firm_staff_obj.append(['test'])
    firm_staff_obj.append(np.asarray([ staff_mean[7], staff_mean[25], staff_mean[26], staff_mean[29], staff_mean[35] ]))

    radar_df = pd.DataFrame({
        'group': ['Manager','Staff'],
        'Objective 1': [firm_managers_obj[0].mean(), firm_staff_obj[0].mean()],
        'Objective 2': [firm_managers_obj[1].mean(), firm_staff_obj[1].mean()],
        'Objective 3': [firm_managers_obj[2].mean(), firm_staff_obj[2].mean()],
        'Objective 4': [firm_managers_obj[3].mean(), firm_staff_obj[3].mean()],
        'Objective 5': [firm_managers_obj[4].mean(), firm_staff_obj[4].mean()],
        'Objective 6': [firm_managers_obj[5].mean(), firm_staff_obj[5].mean()],
        'Objective 7': [firm_managers_obj[6].mean(), firm_staff_obj[6].mean()],
        'Objective 9': [firm_managers_obj[8].mean(), firm_staff_obj[8].mean()]
        })

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


    firm_objective = []

    i = 0
    while i < len(objective_title):

        row1_1, row1_2, row1_3 = st.columns((1,3,1))

        with row1_2:
            firm_objective.append([ label_objective[i], firm_managers_obj[i], firm_staff_obj[i] ])

            X = np.arange(len(label_objective[i]))
            width = 0.5  # the width of the bars

            fig, ax = plt.subplots()
            rects1 = ax.bar(X - width/2, firm_objective[i][1], width, label='Managers')
            if i != 7:
                rects2 = ax.bar(X + width/2, firm_objective[i][2], width, label='Staff')

            fig = plt.figure(figsize=(14, 8))
            ax = fig.add_axes([0,0,1,1])

            ax.set_ylabel('Rating')
            ax.set_title(objective_title[i])
            ax.set_xticks(X, firm_objective[i][0])

            ax.bar(X + 0.00, firm_objective[i][1],  width = 0.25)
            if i != 7:
                ax.bar(X + 0.25, firm_objective[i][2],  width = 0.25)

            if i != 7:
                ax.legend(labels=['Managers', 'Staff'])
            else:
                ax.legend(labels=['Managers'])

            ax.bar_label(rects1)
            ax.bar_label(rects2)
            st.pyplot(fig)

        i += 1
        
# Region-III : End

# Region-IV : Start

if menu == 'Region IV-A: Calabarzon':
    region = 'Region IV-A: Calabarzon'
    st.header(region)
    toggle = True

    st.sidebar.title('Actions')
    toggle = st.sidebar.button('Farmtec Foods Inc.')
    toggle = st.sidebar.button('C&H Cosmetics Industry')

    region4a_df = survey_df[survey_df["What region are you from?"] == region]

    firm_df = survey_df[survey_df["Name of Your Company:"] == 'Farmtec Foods Inc.']
    firm_df

    if toggle:
        firm = 'Farmtec Foods Inc.'
        st.subheader(firm)
        firm_df = survey_df[survey_df["Name of Your Company:"] == firm]
        st.write(firm_df)
    else:
        firm = 'C&H Cosmetics Industry'
        st.subheader(firm)
        firm_df = survey_df[survey_df["Name of Your Company:"] == firm]
        st.write(firm_df)

    # Management / Staff
    firm_respondents_group = firm_df['Are you part of Management or Staff?']
    group_df = np.asarray(firm_respondents_group)
    group, group_counts = np.unique(group_df, return_counts=True)

    # Gender
    firm_respondents_sex = firm_df['What is your sex?']
    sex_df = np.asarray(firm_respondents_sex)
    gender, gender_counts = np.unique(sex_df, return_counts=True)

    # Age Group
    firm_respondents_age_group = firm_df['What age group do you belong to?']
    age_group_df = np.asarray(firm_respondents_age_group)
    age_group, age_group_counts = np.unique(age_group_df, return_counts=True)

    # Education
    firm_respondents_education = firm_df['What is your highest education attainment?']
    education_df = np.asarray(firm_respondents_education)
    education, education_counts = np.unique(education_df, return_counts=True)

    st.subheader('Demographics')

    row1_1, row1_2, row1_3, row1_4 = st.columns((1,1,1,1))
    with row1_1:
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

#     row2_1, row2_2= st.columns((2, 2))
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

    st.subheader('Survey Results')

    firm_managers = firm_df[firm_df["Are you part of Management or Staff?"] == "Management"]
    firm_staff = firm_df[firm_df["Are you part of Management or Staff?"] == "Staff"]

    np_firm_managers = np.asarray(firm_managers)
    np_firm_staff = np.asarray(firm_staff)

    managers_mean = np.mean(np_firm_managers[:,9:59], axis=0)

    # title
    objective_title = []
    objective_title.append("Objective 1: To  determine the employees' extent of understanding of the company's vision, mission, quality policy, purposes and directions")
    objective_title.append("Objective 2: To find out the employees’ perception of the company’s leadership")
    objective_title.append("Objective 3: To have an indication of the employee supervisor relationships in the company")
    objective_title.append("Objective 4: Evaluate  the pervading  conditions for  Total Quality Implementation")
    objective_title.append("Objective 5: Find out if strategic plans were prepared, evaluated and shared company-wide")
    objective_title.append("Objective 6: To find out the Company’s willingness to change towards a TQM direction")
    objective_title.append("Objective 7: Understand the management’s extent of support towards TQM")
    objective_title.append("Objective 8: To know the Management's TQM perspectives")
    objective_title.append("Objective 9: To know the Company’s extent of resiliency")

    # Labels
    label_objective = []
    label_objective.append(['Q6', 'Q12', 'Q20', 'Q37', 'Q38'])
    label_objective.append(['Q4', 'Q7', 'Q9', 'Q34', 'Q35'])
    label_objective.append(['Q2', 'Q3', 'Q10', 'Q22', 'Q23'])
    label_objective.append(['Q15', 'Q16', 'Q17', 'Q24', 'Q39'])
    label_objective.append(['Q1', 'Q10', 'Q31', 'Q32', 'Q40'])
    label_objective.append(['Q5', 'Q19', 'Q21', 'Q29', 'Q33'])
    label_objective.append(['Q13', 'Q14', 'Q18', 'Q28'])
    label_objective.append(['Q41', 'Q42', 'Q43', 'Q44', 'Q45', 'Q46', 'Q47', 'Q48', 'Q49', 'Q50'])
    label_objective.append(['Q8', 'Q26', 'Q27', 'Q30', 'Q36'])

    # Managers data
    firm_managers_obj = []
    firm_managers_obj.append(np.asarray([ managers_mean[5], managers_mean[11], managers_mean[19], managers_mean[36], managers_mean[37] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[3], managers_mean[6], managers_mean[8], managers_mean[33], managers_mean[34] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[1], managers_mean[2], managers_mean[9], managers_mean[21], managers_mean[22] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[14], managers_mean[15], managers_mean[16], managers_mean[23], managers_mean[38] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[0], managers_mean[9], managers_mean[30], managers_mean[31], managers_mean[39] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[4], managers_mean[18], managers_mean[20], managers_mean[28], managers_mean[32] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[12], managers_mean[13], managers_mean[1], managers_mean[27] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[40], managers_mean[41], managers_mean[42], managers_mean[43], managers_mean[44], managers_mean[45], managers_mean[46], managers_mean[47], managers_mean[48], managers_mean[49] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[7], managers_mean[25], managers_mean[26], managers_mean[29], managers_mean[35] ]))


    staff_mean = np.mean(np_firm_staff[:,59:99], axis=0)
    # Staff data
    firm_staff_obj = []
    firm_staff_obj.append(np.asarray([ staff_mean[5], staff_mean[11], staff_mean[19], staff_mean[36], staff_mean[37] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[2], staff_mean[6], staff_mean[8], staff_mean[33], staff_mean[34] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[1], staff_mean[2], staff_mean[9], staff_mean[21], staff_mean[22] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[14], staff_mean[15], staff_mean[16], staff_mean[23], staff_mean[38] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[0], staff_mean[9], staff_mean[30], staff_mean[31], staff_mean[39] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[4], staff_mean[18], staff_mean[20], staff_mean[28], staff_mean[32] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[12], staff_mean[13], staff_mean[1], staff_mean[27] ]))
    firm_staff_obj.append(['test'])
    firm_staff_obj.append(np.asarray([ staff_mean[7], staff_mean[25], staff_mean[26], staff_mean[29], staff_mean[35] ]))

    radar_df = pd.DataFrame({
        'group': ['Manager','Staff'],
        'Objective 1': [firm_managers_obj[0].mean(), firm_staff_obj[0].mean()],
        'Objective 2': [firm_managers_obj[1].mean(), firm_staff_obj[1].mean()],
        'Objective 3': [firm_managers_obj[2].mean(), firm_staff_obj[2].mean()],
        'Objective 4': [firm_managers_obj[3].mean(), firm_staff_obj[3].mean()],
        'Objective 5': [firm_managers_obj[4].mean(), firm_staff_obj[4].mean()],
        'Objective 6': [firm_managers_obj[5].mean(), firm_staff_obj[5].mean()],
        'Objective 7': [firm_managers_obj[6].mean(), firm_staff_obj[6].mean()],
        'Objective 9': [firm_managers_obj[8].mean(), firm_staff_obj[8].mean()]
        })

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


    firm_objective = []

    i = 0
    while i < len(objective_title):

        row1_1, row1_2, row1_3 = st.columns((1,3,1))

        with row1_2:
            firm_objective.append([ label_objective[i], firm_managers_obj[i], firm_staff_obj[i] ])

            X = np.arange(len(label_objective[i]))
            width = 0.5  # the width of the bars

            fig, ax = plt.subplots()
            rects1 = ax.bar(X - width/2, firm_objective[i][1], width, label='Managers')
            if i != 7:
                rects2 = ax.bar(X + width/2, firm_objective[i][2], width, label='Staff')

            fig = plt.figure(figsize=(14, 8))
            ax = fig.add_axes([0,0,1,1])

            ax.set_ylabel('Rating')
            ax.set_title(objective_title[i])
            ax.set_xticks(X, firm_objective[i][0])

            ax.bar(X + 0.00, firm_objective[i][1],  width = 0.25)
            if i != 7:
                ax.bar(X + 0.25, firm_objective[i][2],  width = 0.25)

            if i != 7:
                ax.legend(labels=['Managers', 'Staff'])
            else:
                ax.legend(labels=['Managers'])

            ax.bar_label(rects1)
            ax.bar_label(rects2)
            st.pyplot(fig)

        i += 1
        
# Region-IVA : End

# Region-IVB : Start

if menu == 'Region IV-B: (Mimaropa) Southwestern Tagalog Region':
    region = 'Region IV-B: (Mimaropa) Southwestern Tagalog Region'
    st.header(region)
    toggle = True

    st.sidebar.title('Actions')
    toggle = st.sidebar.button('Rejanos Bakery')

    region4b_df = survey_df[survey_df["What region are you from?"] == region]

    firm_df = survey_df[survey_df["Name of Your Company:"] == 'Rejanos Bakery']
    firm_df

    if toggle:
        firm = 'Rejanos Bakery'
        st.subheader(firm)
        firm_df = survey_df[survey_df["Name of Your Company:"] == firm]
        st.write(firm_df)

    # Management / Staff
    firm_respondents_group = firm_df['Are you part of Management or Staff?']
    group_df = np.asarray(firm_respondents_group)
    group, group_counts = np.unique(group_df, return_counts=True)

    # Gender
    firm_respondents_sex = firm_df['What is your sex?']
    sex_df = np.asarray(firm_respondents_sex)
    gender, gender_counts = np.unique(sex_df, return_counts=True)

    # Age Group
    firm_respondents_age_group = firm_df['What age group do you belong to?']
    age_group_df = np.asarray(firm_respondents_age_group)
    age_group, age_group_counts = np.unique(age_group_df, return_counts=True)

    # Education
    firm_respondents_education = firm_df['What is your highest education attainment?']
    education_df = np.asarray(firm_respondents_education)
    education, education_counts = np.unique(education_df, return_counts=True)

    st.subheader('Demographics')

    row1_1, row1_2, row1_3, row1_4 = st.columns((1,1,1,1))
    with row1_1:
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

#     row2_1, row2_2= st.columns((2, 2))
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

    st.subheader('Survey Results')

    firm_managers = firm_df[firm_df["Are you part of Management or Staff?"] == "Management"]
    firm_staff = firm_df[firm_df["Are you part of Management or Staff?"] == "Staff"]

    np_firm_managers = np.asarray(firm_managers)
    np_firm_staff = np.asarray(firm_staff)

    managers_mean = np.mean(np_firm_managers[:,9:59], axis=0)

    # title
    objective_title = []
    objective_title.append("Objective 1: To  determine the employees' extent of understanding of the company's vision, mission, quality policy, purposes and directions")
    objective_title.append("Objective 2: To find out the employees’ perception of the company’s leadership")
    objective_title.append("Objective 3: To have an indication of the employee supervisor relationships in the company")
    objective_title.append("Objective 4: Evaluate  the pervading  conditions for  Total Quality Implementation")
    objective_title.append("Objective 5: Find out if strategic plans were prepared, evaluated and shared company-wide")
    objective_title.append("Objective 6: To find out the Company’s willingness to change towards a TQM direction")
    objective_title.append("Objective 7: Understand the management’s extent of support towards TQM")
    objective_title.append("Objective 8: To know the Management's TQM perspectives")
    objective_title.append("Objective 9: To know the Company’s extent of resiliency")

    # Labels
    label_objective = []
    label_objective.append(['Q6', 'Q12', 'Q20', 'Q37', 'Q38'])
    label_objective.append(['Q4', 'Q7', 'Q9', 'Q34', 'Q35'])
    label_objective.append(['Q2', 'Q3', 'Q10', 'Q22', 'Q23'])
    label_objective.append(['Q15', 'Q16', 'Q17', 'Q24', 'Q39'])
    label_objective.append(['Q1', 'Q10', 'Q31', 'Q32', 'Q40'])
    label_objective.append(['Q5', 'Q19', 'Q21', 'Q29', 'Q33'])
    label_objective.append(['Q13', 'Q14', 'Q18', 'Q28'])
    label_objective.append(['Q41', 'Q42', 'Q43', 'Q44', 'Q45', 'Q46', 'Q47', 'Q48', 'Q49', 'Q50'])
    label_objective.append(['Q8', 'Q26', 'Q27', 'Q30', 'Q36'])

    # Managers data
    firm_managers_obj = []
    firm_managers_obj.append(np.asarray([ managers_mean[5], managers_mean[11], managers_mean[19], managers_mean[36], managers_mean[37] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[3], managers_mean[6], managers_mean[8], managers_mean[33], managers_mean[34] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[1], managers_mean[2], managers_mean[9], managers_mean[21], managers_mean[22] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[14], managers_mean[15], managers_mean[16], managers_mean[23], managers_mean[38] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[0], managers_mean[9], managers_mean[30], managers_mean[31], managers_mean[39] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[4], managers_mean[18], managers_mean[20], managers_mean[28], managers_mean[32] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[12], managers_mean[13], managers_mean[1], managers_mean[27] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[40], managers_mean[41], managers_mean[42], managers_mean[43], managers_mean[44], managers_mean[45], managers_mean[46], managers_mean[47], managers_mean[48], managers_mean[49] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[7], managers_mean[25], managers_mean[26], managers_mean[29], managers_mean[35] ]))


    staff_mean = np.mean(np_firm_staff[:,59:99], axis=0)
    # Staff data
    firm_staff_obj = []
    firm_staff_obj.append(np.asarray([ staff_mean[5], staff_mean[11], staff_mean[19], staff_mean[36], staff_mean[37] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[2], staff_mean[6], staff_mean[8], staff_mean[33], staff_mean[34] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[1], staff_mean[2], staff_mean[9], staff_mean[21], staff_mean[22] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[14], staff_mean[15], staff_mean[16], staff_mean[23], staff_mean[38] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[0], staff_mean[9], staff_mean[30], staff_mean[31], staff_mean[39] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[4], staff_mean[18], staff_mean[20], staff_mean[28], staff_mean[32] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[12], staff_mean[13], staff_mean[1], staff_mean[27] ]))
    firm_staff_obj.append(['test'])
    firm_staff_obj.append(np.asarray([ staff_mean[7], staff_mean[25], staff_mean[26], staff_mean[29], staff_mean[35] ]))

    radar_df = pd.DataFrame({
        'group': ['Manager','Staff'],
        'Objective 1': [firm_managers_obj[0].mean(), firm_staff_obj[0].mean()],
        'Objective 2': [firm_managers_obj[1].mean(), firm_staff_obj[1].mean()],
        'Objective 3': [firm_managers_obj[2].mean(), firm_staff_obj[2].mean()],
        'Objective 4': [firm_managers_obj[3].mean(), firm_staff_obj[3].mean()],
        'Objective 5': [firm_managers_obj[4].mean(), firm_staff_obj[4].mean()],
        'Objective 6': [firm_managers_obj[5].mean(), firm_staff_obj[5].mean()],
        'Objective 7': [firm_managers_obj[6].mean(), firm_staff_obj[6].mean()],
        'Objective 9': [firm_managers_obj[8].mean(), firm_staff_obj[8].mean()]
        })

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


    firm_objective = []

    i = 0
    while i < len(objective_title):

        row1_1, row1_2, row1_3 = st.columns((1,3,1))

        with row1_2:
            firm_objective.append([ label_objective[i], firm_managers_obj[i], firm_staff_obj[i] ])

            X = np.arange(len(label_objective[i]))
            width = 0.5  # the width of the bars

            fig, ax = plt.subplots()
            rects1 = ax.bar(X - width/2, firm_objective[i][1], width, label='Managers')
            if i != 7:
                rects2 = ax.bar(X + width/2, firm_objective[i][2], width, label='Staff')

            fig = plt.figure(figsize=(14, 8))
            ax = fig.add_axes([0,0,1,1])

            ax.set_ylabel('Rating')
            ax.set_title(objective_title[i])
            ax.set_xticks(X, firm_objective[i][0])

            ax.bar(X + 0.00, firm_objective[i][1],  width = 0.25)
            if i != 7:
                ax.bar(X + 0.25, firm_objective[i][2],  width = 0.25)

            if i != 7:
                ax.legend(labels=['Managers', 'Staff'])
            else:
                ax.legend(labels=['Managers'])

            ax.bar_label(rects1)
            ax.bar_label(rects2)
            st.pyplot(fig)

        i += 1
        
# Region-IVB : End

# Region-V : Start

if menu == 'Region V: Bicol Region':
    region = 'Region V: Bicol Region'
    st.header(region)
    toggle = True

    st.sidebar.title('Actions')
    toggle = st.sidebar.button('J. Emmanuel Pastries')

    region4b_df = survey_df[survey_df["What region are you from?"] == region]

    firm_df = survey_df[survey_df["Name of Your Company:"] == 'J. Emmanuel Pastries']
    firm_df

    if toggle:
        firm = 'J. Emmanuel Pastries'
        st.subheader(firm)
        firm_df = survey_df[survey_df["Name of Your Company:"] == firm]
        st.write(firm_df)

    # Management / Staff
    firm_respondents_group = firm_df['Are you part of Management or Staff?']
    group_df = np.asarray(firm_respondents_group)
    group, group_counts = np.unique(group_df, return_counts=True)

    # Gender
    firm_respondents_sex = firm_df['What is your sex?']
    sex_df = np.asarray(firm_respondents_sex)
    gender, gender_counts = np.unique(sex_df, return_counts=True)

    # Age Group
    firm_respondents_age_group = firm_df['What age group do you belong to?']
    age_group_df = np.asarray(firm_respondents_age_group)
    age_group, age_group_counts = np.unique(age_group_df, return_counts=True)

    # Education
    firm_respondents_education = firm_df['What is your highest education attainment?']
    education_df = np.asarray(firm_respondents_education)
    education, education_counts = np.unique(education_df, return_counts=True)

    st.subheader('Demographics')

    row1_1, row1_2, row1_3, row1_4 = st.columns((1,1,1,1))
    with row1_1:
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

#     row2_1, row2_2= st.columns((2, 2))
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

    st.subheader('Survey Results')

    firm_managers = firm_df[firm_df["Are you part of Management or Staff?"] == "Management"]
    firm_staff = firm_df[firm_df["Are you part of Management or Staff?"] == "Staff"]

    np_firm_managers = np.asarray(firm_managers)
    np_firm_staff = np.asarray(firm_staff)

    managers_mean = np.mean(np_firm_managers[:,9:59], axis=0)

    # title
    objective_title = []
    objective_title.append("Objective 1: To  determine the employees' extent of understanding of the company's vision, mission, quality policy, purposes and directions")
    objective_title.append("Objective 2: To find out the employees’ perception of the company’s leadership")
    objective_title.append("Objective 3: To have an indication of the employee supervisor relationships in the company")
    objective_title.append("Objective 4: Evaluate  the pervading  conditions for  Total Quality Implementation")
    objective_title.append("Objective 5: Find out if strategic plans were prepared, evaluated and shared company-wide")
    objective_title.append("Objective 6: To find out the Company’s willingness to change towards a TQM direction")
    objective_title.append("Objective 7: Understand the management’s extent of support towards TQM")
    objective_title.append("Objective 8: To know the Management's TQM perspectives")
    objective_title.append("Objective 9: To know the Company’s extent of resiliency")

    # Labels
    label_objective = []
    label_objective.append(['Q6', 'Q12', 'Q20', 'Q37', 'Q38'])
    label_objective.append(['Q4', 'Q7', 'Q9', 'Q34', 'Q35'])
    label_objective.append(['Q2', 'Q3', 'Q10', 'Q22', 'Q23'])
    label_objective.append(['Q15', 'Q16', 'Q17', 'Q24', 'Q39'])
    label_objective.append(['Q1', 'Q10', 'Q31', 'Q32', 'Q40'])
    label_objective.append(['Q5', 'Q19', 'Q21', 'Q29', 'Q33'])
    label_objective.append(['Q13', 'Q14', 'Q18', 'Q28'])
    label_objective.append(['Q41', 'Q42', 'Q43', 'Q44', 'Q45', 'Q46', 'Q47', 'Q48', 'Q49', 'Q50'])
    label_objective.append(['Q8', 'Q26', 'Q27', 'Q30', 'Q36'])

    # Managers data
    firm_managers_obj = []
    firm_managers_obj.append(np.asarray([ managers_mean[5], managers_mean[11], managers_mean[19], managers_mean[36], managers_mean[37] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[3], managers_mean[6], managers_mean[8], managers_mean[33], managers_mean[34] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[1], managers_mean[2], managers_mean[9], managers_mean[21], managers_mean[22] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[14], managers_mean[15], managers_mean[16], managers_mean[23], managers_mean[38] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[0], managers_mean[9], managers_mean[30], managers_mean[31], managers_mean[39] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[4], managers_mean[18], managers_mean[20], managers_mean[28], managers_mean[32] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[12], managers_mean[13], managers_mean[1], managers_mean[27] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[40], managers_mean[41], managers_mean[42], managers_mean[43], managers_mean[44], managers_mean[45], managers_mean[46], managers_mean[47], managers_mean[48], managers_mean[49] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[7], managers_mean[25], managers_mean[26], managers_mean[29], managers_mean[35] ]))


    staff_mean = np.mean(np_firm_staff[:,59:99], axis=0)
    # Staff data
    firm_staff_obj = []
    firm_staff_obj.append(np.asarray([ staff_mean[5], staff_mean[11], staff_mean[19], staff_mean[36], staff_mean[37] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[2], staff_mean[6], staff_mean[8], staff_mean[33], staff_mean[34] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[1], staff_mean[2], staff_mean[9], staff_mean[21], staff_mean[22] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[14], staff_mean[15], staff_mean[16], staff_mean[23], staff_mean[38] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[0], staff_mean[9], staff_mean[30], staff_mean[31], staff_mean[39] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[4], staff_mean[18], staff_mean[20], staff_mean[28], staff_mean[32] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[12], staff_mean[13], staff_mean[1], staff_mean[27] ]))
    firm_staff_obj.append(['test'])
    firm_staff_obj.append(np.asarray([ staff_mean[7], staff_mean[25], staff_mean[26], staff_mean[29], staff_mean[35] ]))

    radar_df = pd.DataFrame({
        'group': ['Manager','Staff'],
        'Objective 1': [firm_managers_obj[0].mean(), firm_staff_obj[0].mean()],
        'Objective 2': [firm_managers_obj[1].mean(), firm_staff_obj[1].mean()],
        'Objective 3': [firm_managers_obj[2].mean(), firm_staff_obj[2].mean()],
        'Objective 4': [firm_managers_obj[3].mean(), firm_staff_obj[3].mean()],
        'Objective 5': [firm_managers_obj[4].mean(), firm_staff_obj[4].mean()],
        'Objective 6': [firm_managers_obj[5].mean(), firm_staff_obj[5].mean()],
        'Objective 7': [firm_managers_obj[6].mean(), firm_staff_obj[6].mean()],
        'Objective 9': [firm_managers_obj[8].mean(), firm_staff_obj[8].mean()]
        })

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


    firm_objective = []

    i = 0
    while i < len(objective_title):

        row1_1, row1_2, row1_3 = st.columns((1,3,1))

        with row1_2:
            firm_objective.append([ label_objective[i], firm_managers_obj[i], firm_staff_obj[i] ])

            X = np.arange(len(label_objective[i]))
            width = 0.5  # the width of the bars

            fig, ax = plt.subplots()
            rects1 = ax.bar(X - width/2, firm_objective[i][1], width, label='Managers')
            if i != 7:
                rects2 = ax.bar(X + width/2, firm_objective[i][2], width, label='Staff')

            fig = plt.figure(figsize=(14, 8))
            ax = fig.add_axes([0,0,1,1])

            ax.set_ylabel('Rating')
            ax.set_title(objective_title[i])
            ax.set_xticks(X, firm_objective[i][0])

            ax.bar(X + 0.00, firm_objective[i][1],  width = 0.25)
            if i != 7:
                ax.bar(X + 0.25, firm_objective[i][2],  width = 0.25)

            if i != 7:
                ax.legend(labels=['Managers', 'Staff'])
            else:
                ax.legend(labels=['Managers'])

            ax.bar_label(rects1)
            ax.bar_label(rects2)
            st.pyplot(fig)

        i += 1
        
# Region-V : End

# Region-VI : Start

if menu == 'Region VI: Western Visayas':
    region = 'Region VI: Western Visayas'
    st.header(region)
    toggle = True

    st.sidebar.title('Actions')
    toggle = st.sidebar.button('Herbanext Laboratories Inc.')

    region4b_df = survey_df[survey_df["What region are you from?"] == region]

    firm_df = survey_df[survey_df["Name of Your Company:"] == 'Herbanext Laboratories Inc.']
    firm_df

    if toggle:
        firm = 'Herbanext Laboratories Inc.'
        st.subheader(firm)
        firm_df = survey_df[survey_df["Name of Your Company:"] == firm]
        st.write(firm_df)

    # Management / Staff
    firm_respondents_group = firm_df['Are you part of Management or Staff?']
    group_df = np.asarray(firm_respondents_group)
    group, group_counts = np.unique(group_df, return_counts=True)

    # Gender
    firm_respondents_sex = firm_df['What is your sex?']
    sex_df = np.asarray(firm_respondents_sex)
    gender, gender_counts = np.unique(sex_df, return_counts=True)

    # Age Group
    firm_respondents_age_group = firm_df['What age group do you belong to?']
    age_group_df = np.asarray(firm_respondents_age_group)
    age_group, age_group_counts = np.unique(age_group_df, return_counts=True)

    # Education
    firm_respondents_education = firm_df['What is your highest education attainment?']
    education_df = np.asarray(firm_respondents_education)
    education, education_counts = np.unique(education_df, return_counts=True)

    st.subheader('Demographics')

    row1_1, row1_2, row1_3, row1_4 = st.columns((1,1,1,1))
    with row1_1:
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

#     row2_1, row2_2= st.columns((2, 2))
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

    st.subheader('Survey Results')

    firm_managers = firm_df[firm_df["Are you part of Management or Staff?"] == "Management"]
    firm_staff = firm_df[firm_df["Are you part of Management or Staff?"] == "Staff"]

    np_firm_managers = np.asarray(firm_managers)
    np_firm_staff = np.asarray(firm_staff)

    managers_mean = np.mean(np_firm_managers[:,9:59], axis=0)

    # title
    objective_title = []
    objective_title.append("Objective 1: To  determine the employees' extent of understanding of the company's vision, mission, quality policy, purposes and directions")
    objective_title.append("Objective 2: To find out the employees’ perception of the company’s leadership")
    objective_title.append("Objective 3: To have an indication of the employee supervisor relationships in the company")
    objective_title.append("Objective 4: Evaluate  the pervading  conditions for  Total Quality Implementation")
    objective_title.append("Objective 5: Find out if strategic plans were prepared, evaluated and shared company-wide")
    objective_title.append("Objective 6: To find out the Company’s willingness to change towards a TQM direction")
    objective_title.append("Objective 7: Understand the management’s extent of support towards TQM")
    objective_title.append("Objective 8: To know the Management's TQM perspectives")
    objective_title.append("Objective 9: To know the Company’s extent of resiliency")

    # Labels
    label_objective = []
    label_objective.append(['Q6', 'Q12', 'Q20', 'Q37', 'Q38'])
    label_objective.append(['Q4', 'Q7', 'Q9', 'Q34', 'Q35'])
    label_objective.append(['Q2', 'Q3', 'Q10', 'Q22', 'Q23'])
    label_objective.append(['Q15', 'Q16', 'Q17', 'Q24', 'Q39'])
    label_objective.append(['Q1', 'Q10', 'Q31', 'Q32', 'Q40'])
    label_objective.append(['Q5', 'Q19', 'Q21', 'Q29', 'Q33'])
    label_objective.append(['Q13', 'Q14', 'Q18', 'Q28'])
    label_objective.append(['Q41', 'Q42', 'Q43', 'Q44', 'Q45', 'Q46', 'Q47', 'Q48', 'Q49', 'Q50'])
    label_objective.append(['Q8', 'Q26', 'Q27', 'Q30', 'Q36'])

    # Managers data
    firm_managers_obj = []
    firm_managers_obj.append(np.asarray([ managers_mean[5], managers_mean[11], managers_mean[19], managers_mean[36], managers_mean[37] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[3], managers_mean[6], managers_mean[8], managers_mean[33], managers_mean[34] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[1], managers_mean[2], managers_mean[9], managers_mean[21], managers_mean[22] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[14], managers_mean[15], managers_mean[16], managers_mean[23], managers_mean[38] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[0], managers_mean[9], managers_mean[30], managers_mean[31], managers_mean[39] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[4], managers_mean[18], managers_mean[20], managers_mean[28], managers_mean[32] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[12], managers_mean[13], managers_mean[1], managers_mean[27] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[40], managers_mean[41], managers_mean[42], managers_mean[43], managers_mean[44], managers_mean[45], managers_mean[46], managers_mean[47], managers_mean[48], managers_mean[49] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[7], managers_mean[25], managers_mean[26], managers_mean[29], managers_mean[35] ]))


    staff_mean = np.mean(np_firm_staff[:,59:99], axis=0)
    # Staff data
    firm_staff_obj = []
    firm_staff_obj.append(np.asarray([ staff_mean[5], staff_mean[11], staff_mean[19], staff_mean[36], staff_mean[37] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[2], staff_mean[6], staff_mean[8], staff_mean[33], staff_mean[34] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[1], staff_mean[2], staff_mean[9], staff_mean[21], staff_mean[22] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[14], staff_mean[15], staff_mean[16], staff_mean[23], staff_mean[38] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[0], staff_mean[9], staff_mean[30], staff_mean[31], staff_mean[39] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[4], staff_mean[18], staff_mean[20], staff_mean[28], staff_mean[32] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[12], staff_mean[13], staff_mean[1], staff_mean[27] ]))
    firm_staff_obj.append(['test'])
    firm_staff_obj.append(np.asarray([ staff_mean[7], staff_mean[25], staff_mean[26], staff_mean[29], staff_mean[35] ]))

    radar_df = pd.DataFrame({
        'group': ['Manager','Staff'],
        'Objective 1': [firm_managers_obj[0].mean(), firm_staff_obj[0].mean()],
        'Objective 2': [firm_managers_obj[1].mean(), firm_staff_obj[1].mean()],
        'Objective 3': [firm_managers_obj[2].mean(), firm_staff_obj[2].mean()],
        'Objective 4': [firm_managers_obj[3].mean(), firm_staff_obj[3].mean()],
        'Objective 5': [firm_managers_obj[4].mean(), firm_staff_obj[4].mean()],
        'Objective 6': [firm_managers_obj[5].mean(), firm_staff_obj[5].mean()],
        'Objective 7': [firm_managers_obj[6].mean(), firm_staff_obj[6].mean()],
        'Objective 9': [firm_managers_obj[8].mean(), firm_staff_obj[8].mean()]
        })

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


    firm_objective = []

    i = 0
    while i < len(objective_title):

        row1_1, row1_2, row1_3 = st.columns((1,3,1))

        with row1_2:
            firm_objective.append([ label_objective[i], firm_managers_obj[i], firm_staff_obj[i] ])

            X = np.arange(len(label_objective[i]))
            width = 0.5  # the width of the bars

            fig, ax = plt.subplots()
            rects1 = ax.bar(X - width/2, firm_objective[i][1], width, label='Managers')
            if i != 7:
                rects2 = ax.bar(X + width/2, firm_objective[i][2], width, label='Staff')

            fig = plt.figure(figsize=(14, 8))
            ax = fig.add_axes([0,0,1,1])

            ax.set_ylabel('Rating')
            ax.set_title(objective_title[i])
            ax.set_xticks(X, firm_objective[i][0])

            ax.bar(X + 0.00, firm_objective[i][1],  width = 0.25)
            if i != 7:
                ax.bar(X + 0.25, firm_objective[i][2],  width = 0.25)

            if i != 7:
                ax.legend(labels=['Managers', 'Staff'])
            else:
                ax.legend(labels=['Managers'])

            ax.bar_label(rects1)
            ax.bar_label(rects2)
            st.pyplot(fig)

        i += 1
        
# Region-VI : End

# Region-VII : Start

if menu == 'Region VII: Central Visayas':
    region = 'Region VII: Central Visayas'
    st.header(region)
    toggle = True

    st.sidebar.title('Actions')
    toggle = st.sidebar.button('Suki Trading Corporation')

    region4b_df = survey_df[survey_df["What region are you from?"] == region]

    firm_df = survey_df[survey_df["Name of Your Company:"] == 'Suki Trading Corporation']
    firm_df

    if toggle:
        firm = 'Suki Trading Corporation'
        st.subheader(firm)
        firm_df = survey_df[survey_df["Name of Your Company:"] == firm]
        st.write(firm_df)

    # Management / Staff
    firm_respondents_group = firm_df['Are you part of Management or Staff?']
    group_df = np.asarray(firm_respondents_group)
    group, group_counts = np.unique(group_df, return_counts=True)

    # Gender
    firm_respondents_sex = firm_df['What is your sex?']
    sex_df = np.asarray(firm_respondents_sex)
    gender, gender_counts = np.unique(sex_df, return_counts=True)

    # Age Group
    firm_respondents_age_group = firm_df['What age group do you belong to?']
    age_group_df = np.asarray(firm_respondents_age_group)
    age_group, age_group_counts = np.unique(age_group_df, return_counts=True)

    # Education
    firm_respondents_education = firm_df['What is your highest education attainment?']
    education_df = np.asarray(firm_respondents_education)
    education, education_counts = np.unique(education_df, return_counts=True)

    st.subheader('Demographics')

    row1_1, row1_2, row1_3, row1_4 = st.columns((1,1,1,1))
    with row1_1:
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

#     row2_1, row2_2= st.columns((2, 2))
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

    st.subheader('Survey Results')

    firm_managers = firm_df[firm_df["Are you part of Management or Staff?"] == "Management"]
    firm_staff = firm_df[firm_df["Are you part of Management or Staff?"] == "Staff"]

    np_firm_managers = np.asarray(firm_managers)
    np_firm_staff = np.asarray(firm_staff)

    managers_mean = np.mean(np_firm_managers[:,9:59], axis=0)

    # title
    objective_title = []
    objective_title.append("Objective 1: To  determine the employees' extent of understanding of the company's vision, mission, quality policy, purposes and directions")
    objective_title.append("Objective 2: To find out the employees’ perception of the company’s leadership")
    objective_title.append("Objective 3: To have an indication of the employee supervisor relationships in the company")
    objective_title.append("Objective 4: Evaluate  the pervading  conditions for  Total Quality Implementation")
    objective_title.append("Objective 5: Find out if strategic plans were prepared, evaluated and shared company-wide")
    objective_title.append("Objective 6: To find out the Company’s willingness to change towards a TQM direction")
    objective_title.append("Objective 7: Understand the management’s extent of support towards TQM")
    objective_title.append("Objective 8: To know the Management's TQM perspectives")
    objective_title.append("Objective 9: To know the Company’s extent of resiliency")

    # Labels
    label_objective = []
    label_objective.append(['Q6', 'Q12', 'Q20', 'Q37', 'Q38'])
    label_objective.append(['Q4', 'Q7', 'Q9', 'Q34', 'Q35'])
    label_objective.append(['Q2', 'Q3', 'Q10', 'Q22', 'Q23'])
    label_objective.append(['Q15', 'Q16', 'Q17', 'Q24', 'Q39'])
    label_objective.append(['Q1', 'Q10', 'Q31', 'Q32', 'Q40'])
    label_objective.append(['Q5', 'Q19', 'Q21', 'Q29', 'Q33'])
    label_objective.append(['Q13', 'Q14', 'Q18', 'Q28'])
    label_objective.append(['Q41', 'Q42', 'Q43', 'Q44', 'Q45', 'Q46', 'Q47', 'Q48', 'Q49', 'Q50'])
    label_objective.append(['Q8', 'Q26', 'Q27', 'Q30', 'Q36'])

    # Managers data
    firm_managers_obj = []
    firm_managers_obj.append(np.asarray([ managers_mean[5], managers_mean[11], managers_mean[19], managers_mean[36], managers_mean[37] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[3], managers_mean[6], managers_mean[8], managers_mean[33], managers_mean[34] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[1], managers_mean[2], managers_mean[9], managers_mean[21], managers_mean[22] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[14], managers_mean[15], managers_mean[16], managers_mean[23], managers_mean[38] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[0], managers_mean[9], managers_mean[30], managers_mean[31], managers_mean[39] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[4], managers_mean[18], managers_mean[20], managers_mean[28], managers_mean[32] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[12], managers_mean[13], managers_mean[1], managers_mean[27] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[40], managers_mean[41], managers_mean[42], managers_mean[43], managers_mean[44], managers_mean[45], managers_mean[46], managers_mean[47], managers_mean[48], managers_mean[49] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[7], managers_mean[25], managers_mean[26], managers_mean[29], managers_mean[35] ]))


    staff_mean = np.mean(np_firm_staff[:,59:99], axis=0)
    # Staff data
    firm_staff_obj = []
    firm_staff_obj.append(np.asarray([ staff_mean[5], staff_mean[11], staff_mean[19], staff_mean[36], staff_mean[37] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[2], staff_mean[6], staff_mean[8], staff_mean[33], staff_mean[34] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[1], staff_mean[2], staff_mean[9], staff_mean[21], staff_mean[22] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[14], staff_mean[15], staff_mean[16], staff_mean[23], staff_mean[38] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[0], staff_mean[9], staff_mean[30], staff_mean[31], staff_mean[39] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[4], staff_mean[18], staff_mean[20], staff_mean[28], staff_mean[32] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[12], staff_mean[13], staff_mean[1], staff_mean[27] ]))
    firm_staff_obj.append(['test'])
    firm_staff_obj.append(np.asarray([ staff_mean[7], staff_mean[25], staff_mean[26], staff_mean[29], staff_mean[35] ]))

    radar_df = pd.DataFrame({
        'group': ['Manager','Staff'],
        'Objective 1': [firm_managers_obj[0].mean(), firm_staff_obj[0].mean()],
        'Objective 2': [firm_managers_obj[1].mean(), firm_staff_obj[1].mean()],
        'Objective 3': [firm_managers_obj[2].mean(), firm_staff_obj[2].mean()],
        'Objective 4': [firm_managers_obj[3].mean(), firm_staff_obj[3].mean()],
        'Objective 5': [firm_managers_obj[4].mean(), firm_staff_obj[4].mean()],
        'Objective 6': [firm_managers_obj[5].mean(), firm_staff_obj[5].mean()],
        'Objective 7': [firm_managers_obj[6].mean(), firm_staff_obj[6].mean()],
        'Objective 9': [firm_managers_obj[8].mean(), firm_staff_obj[8].mean()]
        })

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


    firm_objective = []

    i = 0
    while i < len(objective_title):

        row1_1, row1_2, row1_3 = st.columns((1,3,1))

        with row1_2:
            firm_objective.append([ label_objective[i], firm_managers_obj[i], firm_staff_obj[i] ])

            X = np.arange(len(label_objective[i]))
            width = 0.5  # the width of the bars

            fig, ax = plt.subplots()
            rects1 = ax.bar(X - width/2, firm_objective[i][1], width, label='Managers')
            if i != 7:
                rects2 = ax.bar(X + width/2, firm_objective[i][2], width, label='Staff')

            fig = plt.figure(figsize=(14, 8))
            ax = fig.add_axes([0,0,1,1])

            ax.set_ylabel('Rating')
            ax.set_title(objective_title[i])
            ax.set_xticks(X, firm_objective[i][0])

            ax.bar(X + 0.00, firm_objective[i][1],  width = 0.25)
            if i != 7:
                ax.bar(X + 0.25, firm_objective[i][2],  width = 0.25)

            if i != 7:
                ax.legend(labels=['Managers', 'Staff'])
            else:
                ax.legend(labels=['Managers'])

            ax.bar_label(rects1)
            ax.bar_label(rects2)
            st.pyplot(fig)

        i += 1
        
# Region-VII : End

# Region-VIII : Start

if menu == 'Region VIII: Eastern Visayas':
    region = 'Region VIII: Eastern Visayas'
    st.header(region)
    toggle = True

    st.sidebar.title('Actions')
    toggle = st.sidebar.button('Rodriguez Burger and Bread Corporation')

    region4b_df = survey_df[survey_df["What region are you from?"] == region]

    firm_df = survey_df[survey_df["Name of Your Company:"] == 'Rodriguez Burger and Bread Corporation']
    firm_df

    if toggle:
        firm = 'Rodriguez Burger and Bread Corporation'
        st.subheader(firm)
        firm_df = survey_df[survey_df["Name of Your Company:"] == firm]
        st.write(firm_df)

    # Management / Staff
    firm_respondents_group = firm_df['Are you part of Management or Staff?']
    group_df = np.asarray(firm_respondents_group)
    group, group_counts = np.unique(group_df, return_counts=True)

    # Gender
    firm_respondents_sex = firm_df['What is your sex?']
    sex_df = np.asarray(firm_respondents_sex)
    gender, gender_counts = np.unique(sex_df, return_counts=True)

    # Age Group
    firm_respondents_age_group = firm_df['What age group do you belong to?']
    age_group_df = np.asarray(firm_respondents_age_group)
    age_group, age_group_counts = np.unique(age_group_df, return_counts=True)

    # Education
    firm_respondents_education = firm_df['What is your highest education attainment?']
    education_df = np.asarray(firm_respondents_education)
    education, education_counts = np.unique(education_df, return_counts=True)

    st.subheader('Demographics')

    row1_1, row1_2, row1_3, row1_4 = st.columns((1,1,1,1))
    with row1_1:
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

#     row2_1, row2_2= st.columns((2, 2))
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

    st.subheader('Survey Results')

    firm_managers = firm_df[firm_df["Are you part of Management or Staff?"] == "Management"]
    firm_staff = firm_df[firm_df["Are you part of Management or Staff?"] == "Staff"]

    np_firm_managers = np.asarray(firm_managers)
    np_firm_staff = np.asarray(firm_staff)

    managers_mean = np.mean(np_firm_managers[:,9:59], axis=0)

    # title
    objective_title = []
    objective_title.append("Objective 1: To  determine the employees' extent of understanding of the company's vision, mission, quality policy, purposes and directions")
    objective_title.append("Objective 2: To find out the employees’ perception of the company’s leadership")
    objective_title.append("Objective 3: To have an indication of the employee supervisor relationships in the company")
    objective_title.append("Objective 4: Evaluate  the pervading  conditions for  Total Quality Implementation")
    objective_title.append("Objective 5: Find out if strategic plans were prepared, evaluated and shared company-wide")
    objective_title.append("Objective 6: To find out the Company’s willingness to change towards a TQM direction")
    objective_title.append("Objective 7: Understand the management’s extent of support towards TQM")
    objective_title.append("Objective 8: To know the Management's TQM perspectives")
    objective_title.append("Objective 9: To know the Company’s extent of resiliency")

    # Labels
    label_objective = []
    label_objective.append(['Q6', 'Q12', 'Q20', 'Q37', 'Q38'])
    label_objective.append(['Q4', 'Q7', 'Q9', 'Q34', 'Q35'])
    label_objective.append(['Q2', 'Q3', 'Q10', 'Q22', 'Q23'])
    label_objective.append(['Q15', 'Q16', 'Q17', 'Q24', 'Q39'])
    label_objective.append(['Q1', 'Q10', 'Q31', 'Q32', 'Q40'])
    label_objective.append(['Q5', 'Q19', 'Q21', 'Q29', 'Q33'])
    label_objective.append(['Q13', 'Q14', 'Q18', 'Q28'])
    label_objective.append(['Q41', 'Q42', 'Q43', 'Q44', 'Q45', 'Q46', 'Q47', 'Q48', 'Q49', 'Q50'])
    label_objective.append(['Q8', 'Q26', 'Q27', 'Q30', 'Q36'])

    # Managers data
    firm_managers_obj = []
    firm_managers_obj.append(np.asarray([ managers_mean[5], managers_mean[11], managers_mean[19], managers_mean[36], managers_mean[37] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[3], managers_mean[6], managers_mean[8], managers_mean[33], managers_mean[34] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[1], managers_mean[2], managers_mean[9], managers_mean[21], managers_mean[22] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[14], managers_mean[15], managers_mean[16], managers_mean[23], managers_mean[38] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[0], managers_mean[9], managers_mean[30], managers_mean[31], managers_mean[39] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[4], managers_mean[18], managers_mean[20], managers_mean[28], managers_mean[32] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[12], managers_mean[13], managers_mean[1], managers_mean[27] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[40], managers_mean[41], managers_mean[42], managers_mean[43], managers_mean[44], managers_mean[45], managers_mean[46], managers_mean[47], managers_mean[48], managers_mean[49] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[7], managers_mean[25], managers_mean[26], managers_mean[29], managers_mean[35] ]))


    staff_mean = np.mean(np_firm_staff[:,59:99], axis=0)
    # Staff data
    firm_staff_obj = []
    firm_staff_obj.append(np.asarray([ staff_mean[5], staff_mean[11], staff_mean[19], staff_mean[36], staff_mean[37] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[2], staff_mean[6], staff_mean[8], staff_mean[33], staff_mean[34] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[1], staff_mean[2], staff_mean[9], staff_mean[21], staff_mean[22] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[14], staff_mean[15], staff_mean[16], staff_mean[23], staff_mean[38] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[0], staff_mean[9], staff_mean[30], staff_mean[31], staff_mean[39] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[4], staff_mean[18], staff_mean[20], staff_mean[28], staff_mean[32] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[12], staff_mean[13], staff_mean[1], staff_mean[27] ]))
    firm_staff_obj.append(['test'])
    firm_staff_obj.append(np.asarray([ staff_mean[7], staff_mean[25], staff_mean[26], staff_mean[29], staff_mean[35] ]))

    radar_df = pd.DataFrame({
        'group': ['Manager','Staff'],
        'Objective 1': [firm_managers_obj[0].mean(), firm_staff_obj[0].mean()],
        'Objective 2': [firm_managers_obj[1].mean(), firm_staff_obj[1].mean()],
        'Objective 3': [firm_managers_obj[2].mean(), firm_staff_obj[2].mean()],
        'Objective 4': [firm_managers_obj[3].mean(), firm_staff_obj[3].mean()],
        'Objective 5': [firm_managers_obj[4].mean(), firm_staff_obj[4].mean()],
        'Objective 6': [firm_managers_obj[5].mean(), firm_staff_obj[5].mean()],
        'Objective 7': [firm_managers_obj[6].mean(), firm_staff_obj[6].mean()],
        'Objective 9': [firm_managers_obj[8].mean(), firm_staff_obj[8].mean()]
        })

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


    firm_objective = []

    i = 0
    while i < len(objective_title):

        row1_1, row1_2, row1_3 = st.columns((1,3,1))

        with row1_2:
            firm_objective.append([ label_objective[i], firm_managers_obj[i], firm_staff_obj[i] ])

            X = np.arange(len(label_objective[i]))
            width = 0.5  # the width of the bars

            fig, ax = plt.subplots()
            rects1 = ax.bar(X - width/2, firm_objective[i][1], width, label='Managers')
            if i != 7:
                rects2 = ax.bar(X + width/2, firm_objective[i][2], width, label='Staff')

            fig = plt.figure(figsize=(14, 8))
            ax = fig.add_axes([0,0,1,1])

            ax.set_ylabel('Rating')
            ax.set_title(objective_title[i])
            ax.set_xticks(X, firm_objective[i][0])

            ax.bar(X + 0.00, firm_objective[i][1],  width = 0.25)
            if i != 7:
                ax.bar(X + 0.25, firm_objective[i][2],  width = 0.25)

            if i != 7:
                ax.legend(labels=['Managers', 'Staff'])
            else:
                ax.legend(labels=['Managers'])

            ax.bar_label(rects1)
            ax.bar_label(rects2)
            st.pyplot(fig)

        i += 1
        
# Region-VIII : End

# Region-IX : Start

if menu == 'Region IX: Zamboanga Peninsula':
    region = 'Region IX: Zamboanga Peninsula'
    st.header(region)
    toggle = True

    st.sidebar.title('Actions')

    toggle = st.sidebar.button('Diamond Noodles Factory')
    toggle = st.sidebar.button('Wood Tech Builders')


    region9_df = survey_df[survey_df["What region are you from?"] == region]

    firm_df = survey_df[survey_df["Name of Your Company:"] == 'Diamond Noodles Factory']

    if toggle:
        firm = 'Wood Tech Builders'
        st.subheader(firm)
        firm_df = survey_df[survey_df["Name of Your Company:"] == firm]
        st.write(firm_df)

    else:
        firm = 'Diamond Noodles Factory'
        st.subheader(firm)
        firm_df = survey_df[survey_df["Name of Your Company:"] == firm]
        st.write(firm_df)

    # Management / Staff
    firm_respondents_group = firm_df['Are you part of Management or Staff?']
    group_df = np.asarray(firm_respondents_group)
    group, group_counts = np.unique(group_df, return_counts=True)

    # Gender
    firm_respondents_sex = firm_df['What is your sex?']
    sex_df = np.asarray(firm_respondents_sex)
    gender, gender_counts = np.unique(sex_df, return_counts=True)

    # Age Group
    firm_respondents_age_group = firm_df['What age group do you belong to?']
    age_group_df = np.asarray(firm_respondents_age_group)
    age_group, age_group_counts = np.unique(age_group_df, return_counts=True)

    # Education
    firm_respondents_education = firm_df['What is your highest education attainment?']
    education_df = np.asarray(firm_respondents_education)
    education, education_counts = np.unique(education_df, return_counts=True)

    st.subheader('Demographics')

    row1_1, row1_2, row1_3, row1_4 = st.columns((1,1,1,1))
    with row1_1:
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

#     row2_1, row2_2= st.columns((2, 2))
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

    st.subheader('Survey Results')

    firm_managers = firm_df[firm_df["Are you part of Management or Staff?"] == "Management"]
    firm_staff = firm_df[firm_df["Are you part of Management or Staff?"] == "Staff"]

    np_firm_managers = np.asarray(firm_managers)
    np_firm_staff = np.asarray(firm_staff)

    managers_mean = np.mean(np_firm_managers[:,9:59], axis=0)

    # title
    objective_title = []
    objective_title.append("Objective 1: To  determine the employees' extent of understanding of the company's vision, mission, quality policy, purposes and directions")
    objective_title.append("Objective 2: To find out the employees’ perception of the company’s leadership")
    objective_title.append("Objective 3: To have an indication of the employee supervisor relationships in the company")
    objective_title.append("Objective 4: Evaluate  the pervading  conditions for  Total Quality Implementation")
    objective_title.append("Objective 5: Find out if strategic plans were prepared, evaluated and shared company-wide")
    objective_title.append("Objective 6: To find out the Company’s willingness to change towards a TQM direction")
    objective_title.append("Objective 7: Understand the management’s extent of support towards TQM")
    objective_title.append("Objective 8: To know the Management's TQM perspectives")
    objective_title.append("Objective 9: To know the Company’s extent of resiliency")

    # Labels
    label_objective = []
    label_objective.append(['Q6', 'Q12', 'Q20', 'Q37', 'Q38'])
    label_objective.append(['Q4', 'Q7', 'Q9', 'Q34', 'Q35'])
    label_objective.append(['Q2', 'Q3', 'Q10', 'Q22', 'Q23'])
    label_objective.append(['Q15', 'Q16', 'Q17', 'Q24', 'Q39'])
    label_objective.append(['Q1', 'Q10', 'Q31', 'Q32', 'Q40'])
    label_objective.append(['Q5', 'Q19', 'Q21', 'Q29', 'Q33'])
    label_objective.append(['Q13', 'Q14', 'Q18', 'Q28'])
    label_objective.append(['Q41', 'Q42', 'Q43', 'Q44', 'Q45', 'Q46', 'Q47', 'Q48', 'Q49', 'Q50'])
    label_objective.append(['Q8', 'Q26', 'Q27', 'Q30', 'Q36'])

    # Managers data
    firm_managers_obj = []
    firm_managers_obj.append(np.asarray([ managers_mean[5], managers_mean[11], managers_mean[19], managers_mean[36], managers_mean[37] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[3], managers_mean[6], managers_mean[8], managers_mean[33], managers_mean[34] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[1], managers_mean[2], managers_mean[9], managers_mean[21], managers_mean[22] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[14], managers_mean[15], managers_mean[16], managers_mean[23], managers_mean[38] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[0], managers_mean[9], managers_mean[30], managers_mean[31], managers_mean[39] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[4], managers_mean[18], managers_mean[20], managers_mean[28], managers_mean[32] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[12], managers_mean[13], managers_mean[1], managers_mean[27] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[40], managers_mean[41], managers_mean[42], managers_mean[43], managers_mean[44], managers_mean[45], managers_mean[46], managers_mean[47], managers_mean[48], managers_mean[49] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[7], managers_mean[25], managers_mean[26], managers_mean[29], managers_mean[35] ]))

    staff_mean = np.mean(np_firm_staff[:,59:99], axis=0)
    # Staff data
    firm_staff_obj = []
    firm_staff_obj.append(np.asarray([ staff_mean[5], staff_mean[11], staff_mean[19], staff_mean[36], staff_mean[37] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[2], staff_mean[6], staff_mean[8], staff_mean[33], staff_mean[34] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[1], staff_mean[2], staff_mean[9], staff_mean[21], staff_mean[22] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[14], staff_mean[15], staff_mean[16], staff_mean[23], staff_mean[38] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[0], staff_mean[9], staff_mean[30], staff_mean[31], staff_mean[39] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[4], staff_mean[18], staff_mean[20], staff_mean[28], staff_mean[32] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[12], staff_mean[13], staff_mean[1], staff_mean[27] ]))
    firm_staff_obj.append(np.asarray(['test']))
    firm_staff_obj.append(np.asarray([ staff_mean[7], staff_mean[25], staff_mean[26], staff_mean[29], staff_mean[35] ]))


    
    radar_df = pd.DataFrame({
        'group': ['Manager','Staff'],
        'Objective 1': [firm_managers_obj[0].mean(), firm_staff_obj[0].mean()],
        'Objective 2': [firm_managers_obj[1].mean(), firm_staff_obj[1].mean()],
        'Objective 3': [firm_managers_obj[2].mean(), firm_staff_obj[2].mean()],
        'Objective 4': [firm_managers_obj[3].mean(), firm_staff_obj[3].mean()],
        'Objective 5': [firm_managers_obj[4].mean(), firm_staff_obj[4].mean()],
        'Objective 6': [firm_managers_obj[5].mean(), firm_staff_obj[5].mean()],
        'Objective 7': [firm_managers_obj[6].mean(), firm_staff_obj[6].mean()],
        'Objective 9': [firm_managers_obj[8].mean(), firm_staff_obj[8].mean()]
        })

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
    
    
    firm_objective = []

    i = 0
    while i < len(objective_title):

        row1_1, row1_2, row1_3 = st.columns((1,3,1))

        with row1_2:
            firm_objective.append([ label_objective[i], firm_managers_obj[i], firm_staff_obj[i] ])

            X = np.arange(len(label_objective[i]))
            width = 0.5  # the width of the bars

            fig, ax = plt.subplots()
            rects1 = ax.bar(X - width/2, firm_objective[i][1], width, label='Managers')
            if i != 7:
                rects2 = ax.bar(X + width/2, firm_objective[i][2], width, label='Staff')

            fig = plt.figure(figsize=(14, 8))
            ax = fig.add_axes([0,0,1,1])

            ax.set_ylabel('Rating')
            ax.set_title(objective_title[i])
            ax.set_xticks(X, firm_objective[i][0])

            ax.bar(X + 0.00, firm_objective[i][1],  width = 0.25)
            if i != 7:
                ax.bar(X + 0.25, firm_objective[i][2],  width = 0.25)

            if i != 7:
                ax.legend(labels=['Managers', 'Staff'])
            else:
                ax.legend(labels=['Managers'])

            ax.bar_label(rects1)
            ax.bar_label(rects2)
            st.pyplot(fig)

        i += 1
        
# Region-IX : End        
        
# Region-X : Start

if menu == 'Region X: Northern Mindanao':
    region = 'Region X: Northern Mindanao'
    st.header(region)
    toggle = True

    st.sidebar.title('Actions')
    toggle = st.sidebar.button('SLERS Industries Inc.')

    region10_df = survey_df[survey_df["What region are you from?"] == region]

    firm_df = survey_df[survey_df["Name of Your Company:"] == 'SLERS Industries Inc.']

    if toggle:
        firm = 'SLERS Industries Inc.'
        st.subheader(firm)
        firm_df = survey_df[survey_df["Name of Your Company:"] == firm]
        st.write(firm_df)

    # Management / Staff
    firm_respondents_group = firm_df['Are you part of Management or Staff?']
    group_df = np.asarray(firm_respondents_group)
    group, group_counts = np.unique(group_df, return_counts=True)

    # Gender
    firm_respondents_sex = firm_df['What is your sex?']
    sex_df = np.asarray(firm_respondents_sex)
    gender, gender_counts = np.unique(sex_df, return_counts=True)

    # Age Group
    firm_respondents_age_group = firm_df['What age group do you belong to?']
    age_group_df = np.asarray(firm_respondents_age_group)
    age_group, age_group_counts = np.unique(age_group_df, return_counts=True)

    # Education
    firm_respondents_education = firm_df['What is your highest education attainment?']
    education_df = np.asarray(firm_respondents_education)
    education, education_counts = np.unique(education_df, return_counts=True)

    st.subheader('Demographics')

    row1_1, row1_2, row1_3, row1_4 = st.columns((1,1,1,1))
    with row1_1:
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

#     row2_1, row2_2= st.columns((2, 2))
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

    st.subheader('Survey Results')

    firm_managers = firm_df[firm_df["Are you part of Management or Staff?"] == "Management"]
    firm_staff = firm_df[firm_df["Are you part of Management or Staff?"] == "Staff"]

    np_firm_managers = np.asarray(firm_managers)
    np_firm_staff = np.asarray(firm_staff)

    managers_mean = np.mean(np_firm_managers[:,9:59], axis=0)

    # title
    objective_title = []
    objective_title.append("Objective 1: To  determine the employees' extent of understanding of the company's vision, mission, quality policy, purposes and directions")
    objective_title.append("Objective 2: To find out the employees’ perception of the company’s leadership")
    objective_title.append("Objective 3: To have an indication of the employee supervisor relationships in the company")
    objective_title.append("Objective 4: Evaluate  the pervading  conditions for  Total Quality Implementation")
    objective_title.append("Objective 5: Find out if strategic plans were prepared, evaluated and shared company-wide")
    objective_title.append("Objective 6: To find out the Company’s willingness to change towards a TQM direction")
    objective_title.append("Objective 7: Understand the management’s extent of support towards TQM")
    objective_title.append("Objective 8: To know the Management's TQM perspectives")
    objective_title.append("Objective 9: To know the Company’s extent of resiliency")

    # Labels
    label_objective = []
    label_objective.append(['Q6', 'Q12', 'Q20', 'Q37', 'Q38'])
    label_objective.append(['Q4', 'Q7', 'Q9', 'Q34', 'Q35'])
    label_objective.append(['Q2', 'Q3', 'Q10', 'Q22', 'Q23'])
    label_objective.append(['Q15', 'Q16', 'Q17', 'Q24', 'Q39'])
    label_objective.append(['Q1', 'Q10', 'Q31', 'Q32', 'Q40'])
    label_objective.append(['Q5', 'Q19', 'Q21', 'Q29', 'Q33'])
    label_objective.append(['Q13', 'Q14', 'Q18', 'Q28'])
    label_objective.append(['Q41', 'Q42', 'Q43', 'Q44', 'Q45', 'Q46', 'Q47', 'Q48', 'Q49', 'Q50'])
    label_objective.append(['Q8', 'Q26', 'Q27', 'Q30', 'Q36'])

    # Managers data
    firm_managers_obj = []
    firm_managers_obj.append(np.asarray([ managers_mean[5], managers_mean[11], managers_mean[19], managers_mean[36], managers_mean[37] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[3], managers_mean[6], managers_mean[8], managers_mean[33], managers_mean[34] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[1], managers_mean[2], managers_mean[9], managers_mean[21], managers_mean[22] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[14], managers_mean[15], managers_mean[16], managers_mean[23], managers_mean[38] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[0], managers_mean[9], managers_mean[30], managers_mean[31], managers_mean[39] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[4], managers_mean[18], managers_mean[20], managers_mean[28], managers_mean[32] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[12], managers_mean[13], managers_mean[1], managers_mean[27] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[40], managers_mean[41], managers_mean[42], managers_mean[43], managers_mean[44], managers_mean[45], managers_mean[46], managers_mean[47], managers_mean[48], managers_mean[49] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[7], managers_mean[25], managers_mean[26], managers_mean[29], managers_mean[35] ]))


    staff_mean = np.mean(np_firm_staff[:,59:99], axis=0)
    # Staff data
    firm_staff_obj = []
    firm_staff_obj.append(np.asarray([ staff_mean[5], staff_mean[11], staff_mean[19], staff_mean[36], staff_mean[37] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[2], staff_mean[6], staff_mean[8], staff_mean[33], staff_mean[34] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[1], staff_mean[2], staff_mean[9], staff_mean[21], staff_mean[22] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[14], staff_mean[15], staff_mean[16], staff_mean[23], staff_mean[38] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[0], staff_mean[9], staff_mean[30], staff_mean[31], staff_mean[39] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[4], staff_mean[18], staff_mean[20], staff_mean[28], staff_mean[32] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[12], staff_mean[13], staff_mean[1], staff_mean[27] ]))
    firm_staff_obj.append(['test'])
    firm_staff_obj.append(np.asarray([ staff_mean[7], staff_mean[25], staff_mean[26], staff_mean[29], staff_mean[35] ]))

    radar_df = pd.DataFrame({
        'group': ['Manager','Staff'],
        'Objective 1': [firm_managers_obj[0].mean(), firm_staff_obj[0].mean()],
        'Objective 2': [firm_managers_obj[1].mean(), firm_staff_obj[1].mean()],
        'Objective 3': [firm_managers_obj[2].mean(), firm_staff_obj[2].mean()],
        'Objective 4': [firm_managers_obj[3].mean(), firm_staff_obj[3].mean()],
        'Objective 5': [firm_managers_obj[4].mean(), firm_staff_obj[4].mean()],
        'Objective 6': [firm_managers_obj[5].mean(), firm_staff_obj[5].mean()],
        'Objective 7': [firm_managers_obj[6].mean(), firm_staff_obj[6].mean()],
        'Objective 9': [firm_managers_obj[8].mean(), firm_staff_obj[8].mean()]
        })

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


    firm_objective = []

    i = 0
    while i < len(objective_title):

        row1_1, row1_2, row1_3 = st.columns((1,3,1))

        with row1_2:
            firm_objective.append([ label_objective[i], firm_managers_obj[i], firm_staff_obj[i] ])

            X = np.arange(len(label_objective[i]))
            width = 0.5  # the width of the bars

            fig, ax = plt.subplots()
            rects1 = ax.bar(X - width/2, firm_objective[i][1], width, label='Managers')
            if i != 7:
                rects2 = ax.bar(X + width/2, firm_objective[i][2], width, label='Staff')

            fig = plt.figure(figsize=(14, 8))
            ax = fig.add_axes([0,0,1,1])

            ax.set_ylabel('Rating')
            ax.set_title(objective_title[i])
            ax.set_xticks(X, firm_objective[i][0])

            ax.bar(X + 0.00, firm_objective[i][1],  width = 0.25)
            if i != 7:
                ax.bar(X + 0.25, firm_objective[i][2],  width = 0.25)

            if i != 7:
                ax.legend(labels=['Managers', 'Staff'])
            else:
                ax.legend(labels=['Managers'])

            ax.bar_label(rects1)
            ax.bar_label(rects2)
            st.pyplot(fig)

        i += 1
        
# Region-X : End

# Region-XI : Start

if menu == 'Region XI: Davao Region':
    region = 'Region XI: Davao Region'
    st.header(region)
    toggle = True

    st.sidebar.title('Actions')
    toggle = st.sidebar.button('Malagos Food Inc.')
    toggle = st.sidebar.button('Woodworks Collections, Inc.')

    region10_df = survey_df[survey_df["What region are you from?"] == region]

    firm_df = survey_df[survey_df["Name of Your Company:"] == 'Malagos Food Inc.']

    if toggle:
        firm = 'Malagos Food Inc.'
        st.subheader(firm)
        firm_df = survey_df[survey_df["Name of Your Company:"] == firm]
        st.write(firm_df)
    else:
        firm = 'Woodworks Collections, Inc.'
        st.subheader(firm)
        firm_df = survey_df[survey_df["Name of Your Company:"] == firm]
        st.write(firm_df)
        
    # Management / Staff
    firm_respondents_group = firm_df['Are you part of Management or Staff?']
    group_df = np.asarray(firm_respondents_group)
    group, group_counts = np.unique(group_df, return_counts=True)

    # Gender
    firm_respondents_sex = firm_df['What is your sex?']
    sex_df = np.asarray(firm_respondents_sex)
    gender, gender_counts = np.unique(sex_df, return_counts=True)

    # Age Group
    firm_respondents_age_group = firm_df['What age group do you belong to?']
    age_group_df = np.asarray(firm_respondents_age_group)
    age_group, age_group_counts = np.unique(age_group_df, return_counts=True)

    # Education
    firm_respondents_education = firm_df['What is your highest education attainment?']
    education_df = np.asarray(firm_respondents_education)
    education, education_counts = np.unique(education_df, return_counts=True)

    st.subheader('Demographics')

    row1_1, row1_2, row1_3, row1_4 = st.columns((1,1,1,1))
    with row1_1:
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

#     row2_1, row2_2= st.columns((2, 2))
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

    st.subheader('Survey Results')

    firm_managers = firm_df[firm_df["Are you part of Management or Staff?"] == "Management"]
    firm_staff = firm_df[firm_df["Are you part of Management or Staff?"] == "Staff"]

    np_firm_managers = np.asarray(firm_managers)
    np_firm_staff = np.asarray(firm_staff)

    managers_mean = np.mean(np_firm_managers[:,9:59], axis=0)

    # title
    objective_title = []
    objective_title.append("Objective 1: To  determine the employees' extent of understanding of the company's vision, mission, quality policy, purposes and directions")
    objective_title.append("Objective 2: To find out the employees’ perception of the company’s leadership")
    objective_title.append("Objective 3: To have an indication of the employee supervisor relationships in the company")
    objective_title.append("Objective 4: Evaluate  the pervading  conditions for  Total Quality Implementation")
    objective_title.append("Objective 5: Find out if strategic plans were prepared, evaluated and shared company-wide")
    objective_title.append("Objective 6: To find out the Company’s willingness to change towards a TQM direction")
    objective_title.append("Objective 7: Understand the management’s extent of support towards TQM")
    objective_title.append("Objective 8: To know the Management's TQM perspectives")
    objective_title.append("Objective 9: To know the Company’s extent of resiliency")

    # Labels
    label_objective = []
    label_objective.append(['Q6', 'Q12', 'Q20', 'Q37', 'Q38'])
    label_objective.append(['Q4', 'Q7', 'Q9', 'Q34', 'Q35'])
    label_objective.append(['Q2', 'Q3', 'Q10', 'Q22', 'Q23'])
    label_objective.append(['Q15', 'Q16', 'Q17', 'Q24', 'Q39'])
    label_objective.append(['Q1', 'Q10', 'Q31', 'Q32', 'Q40'])
    label_objective.append(['Q5', 'Q19', 'Q21', 'Q29', 'Q33'])
    label_objective.append(['Q13', 'Q14', 'Q18', 'Q28'])
    label_objective.append(['Q41', 'Q42', 'Q43', 'Q44', 'Q45', 'Q46', 'Q47', 'Q48', 'Q49', 'Q50'])
    label_objective.append(['Q8', 'Q26', 'Q27', 'Q30', 'Q36'])

    # Managers data
    firm_managers_obj = []
    firm_managers_obj.append(np.asarray([ managers_mean[5], managers_mean[11], managers_mean[19], managers_mean[36], managers_mean[37] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[3], managers_mean[6], managers_mean[8], managers_mean[33], managers_mean[34] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[1], managers_mean[2], managers_mean[9], managers_mean[21], managers_mean[22] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[14], managers_mean[15], managers_mean[16], managers_mean[23], managers_mean[38] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[0], managers_mean[9], managers_mean[30], managers_mean[31], managers_mean[39] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[4], managers_mean[18], managers_mean[20], managers_mean[28], managers_mean[32] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[12], managers_mean[13], managers_mean[1], managers_mean[27] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[40], managers_mean[41], managers_mean[42], managers_mean[43], managers_mean[44], managers_mean[45], managers_mean[46], managers_mean[47], managers_mean[48], managers_mean[49] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[7], managers_mean[25], managers_mean[26], managers_mean[29], managers_mean[35] ]))


    staff_mean = np.mean(np_firm_staff[:,59:99], axis=0)
    # Staff data
    firm_staff_obj = []
    firm_staff_obj.append(np.asarray([ staff_mean[5], staff_mean[11], staff_mean[19], staff_mean[36], staff_mean[37] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[2], staff_mean[6], staff_mean[8], staff_mean[33], staff_mean[34] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[1], staff_mean[2], staff_mean[9], staff_mean[21], staff_mean[22] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[14], staff_mean[15], staff_mean[16], staff_mean[23], staff_mean[38] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[0], staff_mean[9], staff_mean[30], staff_mean[31], staff_mean[39] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[4], staff_mean[18], staff_mean[20], staff_mean[28], staff_mean[32] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[12], staff_mean[13], staff_mean[1], staff_mean[27] ]))
    firm_staff_obj.append(['test'])
    firm_staff_obj.append(np.asarray([ staff_mean[7], staff_mean[25], staff_mean[26], staff_mean[29], staff_mean[35] ]))

    radar_df = pd.DataFrame({
        'group': ['Manager','Staff'],
        'Objective 1': [firm_managers_obj[0].mean(), firm_staff_obj[0].mean()],
        'Objective 2': [firm_managers_obj[1].mean(), firm_staff_obj[1].mean()],
        'Objective 3': [firm_managers_obj[2].mean(), firm_staff_obj[2].mean()],
        'Objective 4': [firm_managers_obj[3].mean(), firm_staff_obj[3].mean()],
        'Objective 5': [firm_managers_obj[4].mean(), firm_staff_obj[4].mean()],
        'Objective 6': [firm_managers_obj[5].mean(), firm_staff_obj[5].mean()],
        'Objective 7': [firm_managers_obj[6].mean(), firm_staff_obj[6].mean()],
        'Objective 9': [firm_managers_obj[8].mean(), firm_staff_obj[8].mean()]
        })

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


    firm_objective = []

    i = 0
    while i < len(objective_title):

        row1_1, row1_2, row1_3 = st.columns((1,3,1))

        with row1_2:
            firm_objective.append([ label_objective[i], firm_managers_obj[i], firm_staff_obj[i] ])

            X = np.arange(len(label_objective[i]))
            width = 0.5  # the width of the bars

            fig, ax = plt.subplots()
            rects1 = ax.bar(X - width/2, firm_objective[i][1], width, label='Managers')
            if i != 7:
                rects2 = ax.bar(X + width/2, firm_objective[i][2], width, label='Staff')

            fig = plt.figure(figsize=(14, 8))
            ax = fig.add_axes([0,0,1,1])

            ax.set_ylabel('Rating')
            ax.set_title(objective_title[i])
            ax.set_xticks(X, firm_objective[i][0])

            ax.bar(X + 0.00, firm_objective[i][1],  width = 0.25)
            if i != 7:
                ax.bar(X + 0.25, firm_objective[i][2],  width = 0.25)

            if i != 7:
                ax.legend(labels=['Managers', 'Staff'])
            else:
                ax.legend(labels=['Managers'])

            ax.bar_label(rects1)
            ax.bar_label(rects2)
            st.pyplot(fig)

        i += 1
        
# Region-XI : End

# Region-XII : Start

if menu == 'Region XII: Soccsksargen':
    region = 'Region XII: Soccsksargen'
    st.header(region)
    toggle = True

    st.sidebar.title('Actions')
    toggle = st.sidebar.button('Kablon Farm Food Corporation')

    region12_df = survey_df[survey_df["What region are you from?"] == region]

    firm_df = survey_df[survey_df["Name of Your Company:"] == 'Kablon Farm Food Corporation']

    if toggle:
        firm = 'Kablon Farm Food Corporation'
        st.subheader(firm)
        firm_df = survey_df[survey_df["Name of Your Company:"] == firm]
        st.write(firm_df)
       
    # Management / Staff
    firm_respondents_group = firm_df['Are you part of Management or Staff?']
    group_df = np.asarray(firm_respondents_group)
    group, group_counts = np.unique(group_df, return_counts=True)

    # Gender
    firm_respondents_sex = firm_df['What is your sex?']
    sex_df = np.asarray(firm_respondents_sex)
    gender, gender_counts = np.unique(sex_df, return_counts=True)

    # Age Group
    firm_respondents_age_group = firm_df['What age group do you belong to?']
    age_group_df = np.asarray(firm_respondents_age_group)
    age_group, age_group_counts = np.unique(age_group_df, return_counts=True)

    # Education
    firm_respondents_education = firm_df['What is your highest education attainment?']
    education_df = np.asarray(firm_respondents_education)
    education, education_counts = np.unique(education_df, return_counts=True)

    st.subheader('Demographics')

    row1_1, row1_2, row1_3, row1_4 = st.columns((1,1,1,1))
    with row1_1:
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

#     row2_1, row2_2= st.columns((2, 2))
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

    st.subheader('Survey Results')

    firm_managers = firm_df[firm_df["Are you part of Management or Staff?"] == "Management"]
    firm_staff = firm_df[firm_df["Are you part of Management or Staff?"] == "Staff"]

    np_firm_managers = np.asarray(firm_managers)
    np_firm_staff = np.asarray(firm_staff)

    managers_mean = np.mean(np_firm_managers[:,9:59], axis=0)

    # title
    objective_title = []
    objective_title.append("Objective 1: To  determine the employees' extent of understanding of the company's vision, mission, quality policy, purposes and directions")
    objective_title.append("Objective 2: To find out the employees’ perception of the company’s leadership")
    objective_title.append("Objective 3: To have an indication of the employee supervisor relationships in the company")
    objective_title.append("Objective 4: Evaluate  the pervading  conditions for  Total Quality Implementation")
    objective_title.append("Objective 5: Find out if strategic plans were prepared, evaluated and shared company-wide")
    objective_title.append("Objective 6: To find out the Company’s willingness to change towards a TQM direction")
    objective_title.append("Objective 7: Understand the management’s extent of support towards TQM")
    objective_title.append("Objective 8: To know the Management's TQM perspectives")
    objective_title.append("Objective 9: To know the Company’s extent of resiliency")

    # Labels
    label_objective = []
    label_objective.append(['Q6', 'Q12', 'Q20', 'Q37', 'Q38'])
    label_objective.append(['Q4', 'Q7', 'Q9', 'Q34', 'Q35'])
    label_objective.append(['Q2', 'Q3', 'Q10', 'Q22', 'Q23'])
    label_objective.append(['Q15', 'Q16', 'Q17', 'Q24', 'Q39'])
    label_objective.append(['Q1', 'Q10', 'Q31', 'Q32', 'Q40'])
    label_objective.append(['Q5', 'Q19', 'Q21', 'Q29', 'Q33'])
    label_objective.append(['Q13', 'Q14', 'Q18', 'Q28'])
    label_objective.append(['Q41', 'Q42', 'Q43', 'Q44', 'Q45', 'Q46', 'Q47', 'Q48', 'Q49', 'Q50'])
    label_objective.append(['Q8', 'Q26', 'Q27', 'Q30', 'Q36'])

    # Managers data
    firm_managers_obj = []
    firm_managers_obj.append(np.asarray([ managers_mean[5], managers_mean[11], managers_mean[19], managers_mean[36], managers_mean[37] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[3], managers_mean[6], managers_mean[8], managers_mean[33], managers_mean[34] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[1], managers_mean[2], managers_mean[9], managers_mean[21], managers_mean[22] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[14], managers_mean[15], managers_mean[16], managers_mean[23], managers_mean[38] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[0], managers_mean[9], managers_mean[30], managers_mean[31], managers_mean[39] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[4], managers_mean[18], managers_mean[20], managers_mean[28], managers_mean[32] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[12], managers_mean[13], managers_mean[1], managers_mean[27] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[40], managers_mean[41], managers_mean[42], managers_mean[43], managers_mean[44], managers_mean[45], managers_mean[46], managers_mean[47], managers_mean[48], managers_mean[49] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[7], managers_mean[25], managers_mean[26], managers_mean[29], managers_mean[35] ]))


    staff_mean = np.mean(np_firm_staff[:,59:99], axis=0)
    # Staff data
    firm_staff_obj = []
    firm_staff_obj.append(np.asarray([ staff_mean[5], staff_mean[11], staff_mean[19], staff_mean[36], staff_mean[37] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[2], staff_mean[6], staff_mean[8], staff_mean[33], staff_mean[34] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[1], staff_mean[2], staff_mean[9], staff_mean[21], staff_mean[22] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[14], staff_mean[15], staff_mean[16], staff_mean[23], staff_mean[38] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[0], staff_mean[9], staff_mean[30], staff_mean[31], staff_mean[39] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[4], staff_mean[18], staff_mean[20], staff_mean[28], staff_mean[32] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[12], staff_mean[13], staff_mean[1], staff_mean[27] ]))
    firm_staff_obj.append(['test'])
    firm_staff_obj.append(np.asarray([ staff_mean[7], staff_mean[25], staff_mean[26], staff_mean[29], staff_mean[35] ]))

    radar_df = pd.DataFrame({
        'group': ['Manager','Staff'],
        'Objective 1': [firm_managers_obj[0].mean(), firm_staff_obj[0].mean()],
        'Objective 2': [firm_managers_obj[1].mean(), firm_staff_obj[1].mean()],
        'Objective 3': [firm_managers_obj[2].mean(), firm_staff_obj[2].mean()],
        'Objective 4': [firm_managers_obj[3].mean(), firm_staff_obj[3].mean()],
        'Objective 5': [firm_managers_obj[4].mean(), firm_staff_obj[4].mean()],
        'Objective 6': [firm_managers_obj[5].mean(), firm_staff_obj[5].mean()],
        'Objective 7': [firm_managers_obj[6].mean(), firm_staff_obj[6].mean()],
        'Objective 9': [firm_managers_obj[8].mean(), firm_staff_obj[8].mean()]
        })

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


    firm_objective = []

    i = 0
    while i < len(objective_title):

        row1_1, row1_2, row1_3 = st.columns((1,3,1))

        with row1_2:
            firm_objective.append([ label_objective[i], firm_managers_obj[i], firm_staff_obj[i] ])

            X = np.arange(len(label_objective[i]))
            width = 0.5  # the width of the bars

            fig, ax = plt.subplots()
            rects1 = ax.bar(X - width/2, firm_objective[i][1], width, label='Managers')
            if i != 7:
                rects2 = ax.bar(X + width/2, firm_objective[i][2], width, label='Staff')

            fig = plt.figure(figsize=(14, 8))
            ax = fig.add_axes([0,0,1,1])

            ax.set_ylabel('Rating')
            ax.set_title(objective_title[i])
            ax.set_xticks(X, firm_objective[i][0])

            ax.bar(X + 0.00, firm_objective[i][1],  width = 0.25)
            if i != 7:
                ax.bar(X + 0.25, firm_objective[i][2],  width = 0.25)

            if i != 7:
                ax.legend(labels=['Managers', 'Staff'])
            else:
                ax.legend(labels=['Managers'])

            ax.bar_label(rects1)
            ax.bar_label(rects2)
            st.pyplot(fig)

        i += 1
        
# Region-XII : End

# Region-XIII : Start

if menu == 'Region XIII: Caraga':
    region = 'Region XIII: Caraga'
    st.header(region)
    toggle = True

    st.sidebar.title('Actions')
    toggle = st.sidebar.button('MAFFISCO-MPC')

    region12_df = survey_df[survey_df["What region are you from?"] == region]

    firm_df = survey_df[survey_df["Name of Your Company:"] == 'MAFFISCO-MPC']
    firm_df
    if toggle:
        firm = 'MAFFISCO-MPC'
        st.subheader(firm)
        firm_df = survey_df[survey_df["Name of Your Company:"] == firm]
        st.write(firm_df)
       
    # Management / Staff
    firm_respondents_group = firm_df['Are you part of Management or Staff?']
    group_df = np.asarray(firm_respondents_group)
    group, group_counts = np.unique(group_df, return_counts=True)

    # Gender
    firm_respondents_sex = firm_df['What is your sex?']
    sex_df = np.asarray(firm_respondents_sex)
    gender, gender_counts = np.unique(sex_df, return_counts=True)

    # Age Group
    firm_respondents_age_group = firm_df['What age group do you belong to?']
    age_group_df = np.asarray(firm_respondents_age_group)
    age_group, age_group_counts = np.unique(age_group_df, return_counts=True)

    # Education
    firm_respondents_education = firm_df['What is your highest education attainment?']
    education_df = np.asarray(firm_respondents_education)
    education, education_counts = np.unique(education_df, return_counts=True)

    st.subheader('Demographics')

    row1_1, row1_2, row1_3, row1_4 = st.columns((1,1,1,1))
    with row1_1:
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

#     row2_1, row2_2= st.columns((2, 2))
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

    st.subheader('Survey Results')

    firm_managers = firm_df[firm_df["Are you part of Management or Staff?"] == "Management"]
    firm_staff = firm_df[firm_df["Are you part of Management or Staff?"] == "Staff"]

    np_firm_managers = np.asarray(firm_managers)
    np_firm_staff = np.asarray(firm_staff)

    managers_mean = np.mean(np_firm_managers[:,9:59], axis=0)

    # title
    objective_title = []
    objective_title.append("Objective 1: To  determine the employees' extent of understanding of the company's vision, mission, quality policy, purposes and directions")
    objective_title.append("Objective 2: To find out the employees’ perception of the company’s leadership")
    objective_title.append("Objective 3: To have an indication of the employee supervisor relationships in the company")
    objective_title.append("Objective 4: Evaluate  the pervading  conditions for  Total Quality Implementation")
    objective_title.append("Objective 5: Find out if strategic plans were prepared, evaluated and shared company-wide")
    objective_title.append("Objective 6: To find out the Company’s willingness to change towards a TQM direction")
    objective_title.append("Objective 7: Understand the management’s extent of support towards TQM")
    objective_title.append("Objective 8: To know the Management's TQM perspectives")
    objective_title.append("Objective 9: To know the Company’s extent of resiliency")

    # Labels
    label_objective = []
    label_objective.append(['Q6', 'Q12', 'Q20', 'Q37', 'Q38'])
    label_objective.append(['Q4', 'Q7', 'Q9', 'Q34', 'Q35'])
    label_objective.append(['Q2', 'Q3', 'Q10', 'Q22', 'Q23'])
    label_objective.append(['Q15', 'Q16', 'Q17', 'Q24', 'Q39'])
    label_objective.append(['Q1', 'Q10', 'Q31', 'Q32', 'Q40'])
    label_objective.append(['Q5', 'Q19', 'Q21', 'Q29', 'Q33'])
    label_objective.append(['Q13', 'Q14', 'Q18', 'Q28'])
    label_objective.append(['Q41', 'Q42', 'Q43', 'Q44', 'Q45', 'Q46', 'Q47', 'Q48', 'Q49', 'Q50'])
    label_objective.append(['Q8', 'Q26', 'Q27', 'Q30', 'Q36'])

    # Managers data
    firm_managers_obj = []
    firm_managers_obj.append(np.asarray([ managers_mean[5], managers_mean[11], managers_mean[19], managers_mean[36], managers_mean[37] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[3], managers_mean[6], managers_mean[8], managers_mean[33], managers_mean[34] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[1], managers_mean[2], managers_mean[9], managers_mean[21], managers_mean[22] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[14], managers_mean[15], managers_mean[16], managers_mean[23], managers_mean[38] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[0], managers_mean[9], managers_mean[30], managers_mean[31], managers_mean[39] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[4], managers_mean[18], managers_mean[20], managers_mean[28], managers_mean[32] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[12], managers_mean[13], managers_mean[1], managers_mean[27] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[40], managers_mean[41], managers_mean[42], managers_mean[43], managers_mean[44], managers_mean[45], managers_mean[46], managers_mean[47], managers_mean[48], managers_mean[49] ]))
    firm_managers_obj.append(np.asarray([ managers_mean[7], managers_mean[25], managers_mean[26], managers_mean[29], managers_mean[35] ]))


    staff_mean = np.mean(np_firm_staff[:,59:99], axis=0)
    # Staff data
    firm_staff_obj = []
    firm_staff_obj.append(np.asarray([ staff_mean[5], staff_mean[11], staff_mean[19], staff_mean[36], staff_mean[37] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[2], staff_mean[6], staff_mean[8], staff_mean[33], staff_mean[34] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[1], staff_mean[2], staff_mean[9], staff_mean[21], staff_mean[22] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[14], staff_mean[15], staff_mean[16], staff_mean[23], staff_mean[38] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[0], staff_mean[9], staff_mean[30], staff_mean[31], staff_mean[39] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[4], staff_mean[18], staff_mean[20], staff_mean[28], staff_mean[32] ]))
    firm_staff_obj.append(np.asarray([ staff_mean[12], staff_mean[13], staff_mean[1], staff_mean[27] ]))
    firm_staff_obj.append(['test'])
    firm_staff_obj.append(np.asarray([ staff_mean[7], staff_mean[25], staff_mean[26], staff_mean[29], staff_mean[35] ]))

    radar_df = pd.DataFrame({
        'group': ['Manager','Staff'],
        'Objective 1': [firm_managers_obj[0].mean(), firm_staff_obj[0].mean()],
        'Objective 2': [firm_managers_obj[1].mean(), firm_staff_obj[1].mean()],
        'Objective 3': [firm_managers_obj[2].mean(), firm_staff_obj[2].mean()],
        'Objective 4': [firm_managers_obj[3].mean(), firm_staff_obj[3].mean()],
        'Objective 5': [firm_managers_obj[4].mean(), firm_staff_obj[4].mean()],
        'Objective 6': [firm_managers_obj[5].mean(), firm_staff_obj[5].mean()],
        'Objective 7': [firm_managers_obj[6].mean(), firm_staff_obj[6].mean()],
        'Objective 9': [firm_managers_obj[8].mean(), firm_staff_obj[8].mean()]
        })

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


    firm_objective = []

    i = 0
    while i < len(objective_title):

        row1_1, row1_2, row1_3 = st.columns((1,3,1))

        with row1_2:
            firm_objective.append([ label_objective[i], firm_managers_obj[i], firm_staff_obj[i] ])

            X = np.arange(len(label_objective[i]))
            width = 0.5  # the width of the bars

            fig, ax = plt.subplots()
            rects1 = ax.bar(X - width/2, firm_objective[i][1], width, label='Managers')
            if i != 7:
                rects2 = ax.bar(X + width/2, firm_objective[i][2], width, label='Staff')

            fig = plt.figure(figsize=(14, 8))
            ax = fig.add_axes([0,0,1,1])

            ax.set_ylabel('Rating')
            ax.set_title(objective_title[i])
            ax.set_xticks(X, firm_objective[i][0])

            ax.bar(X + 0.00, firm_objective[i][1],  width = 0.25)
            if i != 7:
                ax.bar(X + 0.25, firm_objective[i][2],  width = 0.25)

            if i != 7:
                ax.legend(labels=['Managers', 'Staff'])
            else:
                ax.legend(labels=['Managers'])

            ax.bar_label(rects1)
            ax.bar_label(rects2)
            st.pyplot(fig)

        i += 1
        
# Region-XIII : End