import streamlit as st
import pandas as pd
import numpy as np
import time

# Initialize web app with simple table and comment
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

url = "data/heart_classification.csv"

names = ['age', 'sex', 'cp', 'chol', 'fbs']
heart_df = pd.read_csv(url)

# Create text and table in streamlit web app
st.write("This is my first streamlit web application. Here's a sample dataframe:")

st.write(heart_df)


# Line charts
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)

x = st.slider('x')
st.write(x, 'squared is', x * x)

st.text_input("Your name", key="name")
st.session_state.name

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20,3),
        columns = ['a', 'b', 'c']
        )
    
    chart_data

new_df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})    
    
option = st.selectbox(
    'Which number do you like best?',
    df['first column'])

'You selected: ', option

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted',
    ('Email', 'Home Phone', 'Mobile Phone')
)

add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

'Starting a long computation . . .'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
    
'. . . and now we\'re done!'


