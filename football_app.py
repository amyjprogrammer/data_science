#Import Libraries

import streamlit as st 
import pandas as pd
import base64
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title('NFL Football Stats Explorer')

st.markdown("""
This app performs simple webscraping of NFL players stats data.
* **Python libraries:** base64, pandas, streamlit
* **Data Source:** [pro-football-reference.com](https://www.pro-football-reference.com/).
""")

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1990,2021))))

#Web scraping of stats
@st.cache
def load_data(year):
    url = "https://www.pro-football-reference.com/years/" + str(year) + "/rushing.htm"
    html = pd.read_html(url, header = 1)
    df = html[0]
    playerstats = df.drop(['Rk'], axis = 1)
    return playerstats
playerstats = load_data(selected_year)

playerstats