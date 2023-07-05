import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# simple stock price app
shown are stock Closing prices of GOOGLE and Volume
""")

tickersymbol = 'GOOGL'

tickerData1 = yf.Ticker(tickersymbol)
tickerDF = tickerData1.history(period='1mo')

print(tickerDF.Close) # try out and see if it works properly

# we then see the result on streamlit 
# you should run the following command python -m streamlit app.py

st.write("""
## Closing price
""")
st.line_chart(tickerDF.Close)

st.write("""
## Trading Volume 
""")
st.line_chart(tickerDF.Volume)

