#Import Libraries

import streamlit as st 
import pandas as pd
import base64
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title('S&P 500')

st.markdown("""
This app retrieves the list of the **S&P 500** (from Widipedia) and its cooresponding **stock closing price** (year-to-date).
* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn
* **Data Source:** [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies).
""")

st.sidebar.header('User Input Features')

#Scraping Wikipedia for the data
@st.cache
def load_data():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    html = pd.read_html(url, header = 0)
    data = html[0]
    return data 

data = load_data()


