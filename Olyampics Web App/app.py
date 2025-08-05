import streamlit as st
import pandas as pd
import preprocessor 

df = preprocessor.preprocess()

st.sidebar.radio(
    'Select an Option',
    ('Medal Tally','Overall Analysis','Country-Wise Analysis','Athlete wise Analysis')
)

st.dataframe(df)