import streamlit as st
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import locale

# import plot_likert
from math import pi

import matplotlib.pyplot as plt, mpld3
# import numpy as np
from mpld3 import plugins
import streamlit.components.v1 as components
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

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
survey_df = pd.read_csv('data/ktp_climate_survey_2nd_cycle.csv').reset_index()
# survey_df
np_survey_df = np.asarray(survey_df)

managers = survey_df[survey_df["Are you part of Management or Staff?"] == "Management"]
staffs = survey_df[survey_df["Are you part of Management or Staff?"] == "Staff"]

regions_df = demo_respondents_group = survey_df['What region are you from?']
regions_df = np.asarray(regions_df)

regions, region_counts = np.unique(regions_df, return_counts=True)
# regions




t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

two_subplot_fig = plt.figure(figsize=(8,8))
plt.subplot(211)
plt.plot(t1, f(t1), color='tab:blue', marker=',')
plt.plot(t2, f(t2), color='black', marker='.')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), color='tab:orange', linestyle='--', marker='.')

# Define some CSS to control our custom labels
css = '''
table
{
  border-collapse: collapse;
}
th
{
  color: #ffffff;
  background-color: #000000;
}
td
{
  background-color: #cccccc;
}
table, th, td
{
  font-family:Arial, Helvetica, sans-serif;
  border: 1px solid black;
  text-align: right;
}
'''

for axes in two_subplot_fig.axes:
  for line in axes.get_lines():
    xy_data = line.get_xydata()
    labels = []
    for x,y in xy_data:
      html_label = f'<table border="1" class="dataframe"> <thead> <tr style="text-align: right;"> </thead> <tbody> <tr> <th>x</th> <td>{x}</td> </tr> <tr> <th>y</th> <td>{y}</td> </tr> </tbody> </table>'
      labels.append(html_label)
    tooltip = plugins.PointHTMLTooltip(line, labels, css=css)
    plugins.connect(two_subplot_fig, tooltip)

fig_html = mpld3.fig_to_html(two_subplot_fig)
components.html(fig_html, height=850, width=850)

# fig1, ax1 = plt.subplots(figsize=(8, 8))
# fig1.subplots_adjust(0.3,0,1,1)

# ax1.axis('equal')

# plt.pie(region_counts, labels = regions, autopct='%1.1f%%', shadow=False, startangle = 90)
# plt.legend(
#     loc='upper left',
#     prop={'size': 11},
#     bbox_to_anchor=(0.98, 1.05), # x,y coordinates
#     bbox_transform=fig1.transFigure
# )
# plt.title('Respondents by Region')
# plt.axis('equal')
# plt.show() 





housing_df = pd.read_csv(url)

st.sidebar.title('Survey Results')

menu = st.sidebar.radio('This web application features the following:', (
    'Demographics', 
    'Overall Results',
    'Housing Calculator',
))

if menu == 'Demographics':
    toggle = True
    
    fig1, ax1 = plt.subplots(figsize=(8, 8))
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
    plt.show() 
        
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