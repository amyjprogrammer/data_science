#Import Libraries

from pandas.core.indexes import period
import streamlit as st 
import pandas as pd
import base64
import matplotlib.pyplot as plt
import yfinance as yf

st.title('S&P 500')

st.markdown("""
This app retrieves the list of the **S&P 500** (from Widipedia) and its cooresponding **stock closing price** (year-to-date).
* **Python libraries:** base64, pandas, streamlit, matplotlib, yfinance
* **Data Source:** [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies).
""")

st.sidebar.header('User Input Features')

#Scraping Wikipedia for the data
@st.cache #used so the system doesn't need to redownload everytime
def load_data():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    html = pd.read_html(url, header = 0)
    data = html[0]
    return data 

data = load_data()
sector = data.groupby('GICS Sector')
#data (used for testing)

#Different sectors for the S&P 500 companies- Sidebar
different_sector = sorted(data['GICS Sector'].unique())
sector_sidebar = st.sidebar.multiselect('Sectors', different_sector, different_sector)
#different_sector (used for testing)

#Filtering the data from what is entered in the sidebar
data_selected_sector = data[(data['GICS Sector'].isin(sector_sidebar))]

#Display header and data
st.header('Display Companies in Selected Sector')
st.write('Data Dimension: ' + str(data_selected_sector.shape[0]) + ' rows and ' + str(data_selected_sector.shape[1]) + 'columns.')
st.dataframe(data_selected_sector)

#Downloading the S&P500 data as an CSV file
def filedownload(file):
    csv = file.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="SP500.csv">Download CSV File</a>'
    return href 

st.markdown(filedownload(data_selected_sector), unsafe_allow_html=True)

#Download stock prices
#checkout https://pypi.org/project/yfinance/ (for more info on usng yfinance)
stock_data = yf.download(
    tickers = list(data_selected_sector[:10].Symbol), #only looking at 10, because it loads slow
    period = 'ytd',
    interval = '1d',
    group_by = 'ticker',
    auto_adjust = True, #default is False
    prepost = True, #default is False
    threads = True, #default is True
    proxy = None #default is None
)

#Plot Closing Price
def price_plot(symbol):
    data = pd.DataFrame(stock_data[symbol].Close)
    data['Date'] = data.index
    plt.fill_between(data.Date, data.Close, color='skyblue', alpha=0.3)
    plt.plot(data.Date, data.Close, color='skyblue', alpha=0.8)
    plt.xticks(rotation=90)
    plt.title(symbol, fontweight='bold')
    plt.xlabel('Date')
    plt.ylabel("Closing Price")
    return st.pyplot()

num_company = st.sidebar.slider('Number of Companies', 1, 5)

if st.button('Show Plots'):
    st.header('Stock Closing Price')
    for i in list(data_selected_sector.Symbol)[:num_company]:
        price_plot(i)

st.set_option('deprecation.showPyplotGlobalUse', False)