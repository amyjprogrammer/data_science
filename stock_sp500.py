#Import Libraries

from pandas.core.indexes import period
import streamlit as st 
import pandas as pd
import base64
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

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
data

#Different sectors for the S&P 500 companies
different_sector = data['GICS Sector'].unique()
different_sector

group_sector = data.groupby('GICS Sector')
g = group_sector.describe()
g

health_sector = group_sector.get_group('Health Care')
health_sector

#Download stock prices
#checkout https://pypi.org/project/yfinance/ (for more info on usng yfinance)
stock_data = yf.download(
    tickers = list(data.Symbol),
    period = 'ytd',
    interval = '1d',
    group_by = 'ticker',
    auto_adjust = True, #default is False
    prepost = True, #default is False
    threads = True, #default is True
    proxy = None #default is None
)

#stock data for Abbott Laboratories for this year
info = stock_data['ABT']
info

#adding Date in a Column to use for Matplotlib
abt = pd.DataFrame(stock_data['ABT'].Close)
abt['Date'] = abt.index
abt

def price_plot(symbol):
    data = pd.DataFrame(stock_data[symbol].Close)
    data['Date'] = data.index
    plt.fill_between(data.Date, data.Close, color='skyblue', alpha=0.3)
    plt.plot(data.Date, data.Close, color='skyblue', alpha=0.8)
    plt.xticks(rotation=90)
    plt.xlabel('Date')
    plt.ylabel("Closing Price")
    return st.pyplot()

graph = price_plot('ABT')
graph
