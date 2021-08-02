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

#Sorting teams in the sidebar   
sorted_by_team = sorted(playerstats.Tm.unique())
selected_teams = st.sidebar.multiselect('Teams', sorted_by_team, sorted_by_team)

#Sorting by position - sidebar
unique_position = ['RB', 'QB', 'WR', 'FB', 'TE']
selected_position = st.sidebar.multiselect('Position', unique_position, unique_position)

#Filtering the data
filtered_team_position = playerstats[(playerstats.Tm.isin(selected_teams)) & playerstats.Pos.isin(selected_position)]

st.header('Display Player Stats of Selected Team(s)')
st.write('Data Dimension: ' + str(filtered_team_position.shape[0]) + ' rows and ' + str(filtered_team_position.shape[1])+ ' columns.') 
st.dataframe(filtered_team_position)

#Download info as a CSV File
def filedownload(file):
    csv = file.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(filtered_team_position), unsafe_allow_html=True)

# Heatmap
if st.button('Intercorrelation Heatmap'):
    st.header('Intercorrelation Matrix Heatmap')
    filtered_team_position.to_csv('output.csv',index=False)
    df = pd.read_csv('output.csv')

    corr = df.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(7, 5))
        ax = sns.heatmap(corr, mask=mask, vmax=1, square=True)
    st.pyplot(f)