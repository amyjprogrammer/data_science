import yfinance as yf 
import streamlit as st 
import pandas as pd 

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and *volume* of Google!

""")

#Using Article below to get stock information
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

#define the ticker symbol
tickerSymbol = 'GOOGL'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical data prices from May 31, 2010- May 31, 2020
tickerDF = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
#Open  High  Low  Close   Volume   Dividends      Stock Splits

st.write("""
### Closing Price
""")
st.line_chart(tickerDF.Close)

st.write("""
### Volume 
""")
st.line_chart(tickerDF.Volume)
