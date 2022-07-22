import streamlit as st
import pandas as pd
import numpy as np

st.session_state.name = ""
show = False

st.title("Web Application Concepts")

url = "data/heart_classification.csv"

# names = ['age', 'sex', 'cp', 'chol', 'fbs']
heart_df = pd.read_csv(url)

st.sidebar.title('About')
# st.sidebar.info('This web application features the following:')

menu = st.sidebar.radio('This web application features the following:', (
    'The dataframe', 
#     'sidebar that toggles show/hide dataframe',
    'Charts',
    'Caching',
    'Custom Themes'
))

if menu == 'The dataframe':
    #st.write(heart_df[['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs']])
    toggle = true
    st.sidebar.title('Actions')
    show = st.sidebar.button('Show/Hide DataFrame')
    
    if toggle:
        st.write(heart_df[['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs']])
    else:
        
        st.write(heart_df)
    
if menu == 'Charts':
    line_chart_data = pd.DataFrame(
        np.random.randn(100, 3),
        columns = ['Col A', 'Col B', 'Col C']
    )
    
    area_chart_data = pd.DataFrame(
        np.random.randn(100, 4),
        columns = ['Col A', 'Col B', 'Col C', 'Col D']
    )
    
    bar_chart_data = pd.DataFrame(
        np.random.randn(100, 2),
        columns = ['Col A', 'Col B']
    )
    
    st.line_chart(line_chart_data)
    st.area_chart(area_chart_data)
    st.bar_chart(bar_chart_data)
    
    st.sidebar.title('Actions')
    
if menu == 'Caching':
    data = ''
    @st.cache
    def load_data(url):
        # Fetch data from URL here, and then clean it up.
        url = "data/breast_cancer_data_classification.csv"

        #names = ['age', 'sex', 'cp', 'chol', 'fbs']
        data = pd.read_csv(url)

        return data
    
    st.write(data)
    
    st.sidebar.title('Actions')
    
if menu == 'Custom Themes':
    st.sidebar.title('Parameters')
# st.sidebar.text_input("Your name", key="name")
# show = st.sidebar.button('Show/Hide DataFrame')