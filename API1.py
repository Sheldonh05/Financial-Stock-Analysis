import requests
import pandas as pd
import streamlit as sl


BASE_URL = 'https://financialmodelingprep.com/api/v3'

sl.header('Financial Stock Analysis')
symbol = sl.sidebar.text_input('Ticker:',options=('AAPL','NVDA','MSFT'))

finData = sl.sidebar.selectbox('Data Type', options=('income-statement','balance-sheet-statement',
                                                     'cash-flow-statement','income-statement-growth','balance-sheet-growth-statement',
                                                     'rating','key-metrics','financial-growth'))

if finData == 'Historical Price smaller intervals':
    interval = sl.sidebar.selectbox('Interval',options=('1min','5min','15min','30min','1hr','4hr','Day'))
    finData ='historical-chart/'+interval

transpose = sl.sidebar.selectbox('Transpose',options=('Yes','No'))
URL = 'https://financialmodelingprep.com/api/v3/income-statement/AAPL?period=annual&apikey=XL3Lt5OdKAY7opPYbkn2nL4yymYnCJQg'
API_Key = 'XL3Lt5OdKAY7opPYbkn2nL4yymYnCJQg'

RESPONSE = requests.get(URL).json()

DATA = pd.DataFrame(RESPONSE).T

if transpose == 'Yes':
    DATA = pd.DataFrame(RESPONSE).T
else:
    DATA = pd.DataFrame(RESPONSE)
sl.write(DATA)

print(DATA)


