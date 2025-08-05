import streamlit as st
import pandas as pd
import preprocessor,helper 

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')


df = preprocessor.preprocess(df,region_df)


st.sidebar.title("Olyampics Analysis")
user_menu = st.sidebar.radio(
    'Select an Option',
    ('Medal Tally','Overall Analysis','Country-Wise Analysis','Athlete wise Analysis')
)

if user_menu=='Medal Tally':
    st.sidebar.header("Medal Tally")
    years, country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select Year",years)
    selected_country = st.sidebar.selectbox("Select Country",country)


    medal_tally =helper.fetch_medal_tally(df,selected_year,selected_country)
    if selected_year == 'Overall' and selected_country =='Overall':
        st.title("Overall Tally")
    if selected_year != 'Overall' and selected_country =='Overall':
        st.title("Medal Tally in"+ str(selected_year)+ 'Olyampics')
    if selected_year == 'Overall' and selected_country !='Overall':
        st.title(selected_country + "Overall Performance")
    if selected_year != 'Overall' and selected_country !='Overall':
        st.title(selected_country + "Performance in " + str(selected_year) +"Olyampics")
    st.table(medal_tally)
