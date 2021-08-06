#Importing Libraries
import streamlit as st 
from PIL import Image
import pandas as pd
import base64
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import json
import time

#Full width of the screen
st.set_page_config(layout="wide")

#image at the top showing CryptoCurrency
image = Image.open('cryptocurrency.jpg')
st.image(image, width=500)

st.title('Crypto Price App')

st.markdown("""
This app retrieves cryptocurrency prices for the top 100 cryptocurrency from the **CoinMarketCap!**            
""")

#sidebar
st.sidebar.header('Input Options')

#About section
expander_bar = st.beta_expander('About')
expander_bar.markdown("""
* **Python libraries:** base64, pandas, streamlit, matplotlib, Beautiful Soup, requests, json, time 
* **Data source:** [CoinMarketCap](http://coinmarket.com)
* **Credit:** Web scraper adapted from the Medium article *[Web Scraping Crypto Prices With Python](https://towardsdatascience.com/web-scraping-crypto-prices-with-python-41072ea5b5bf)* written by [Bryan Feng](https://medium.com/@bryanf).                   
""")

#Having three Columns
col1 = st.sidebar
col2, col3 = st.beta_columns((2,1))

#Column 1- sidebar
col1.header('Input Options')

#sidebar- currency price unit
currency_price = col1.selectbox('Select currency for price', 'USD', 'BTC', 'ETH')
