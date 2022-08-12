import streamlit as st
import yfinance as yf
import pandas as pd 

st.write("MAKE YOUR FIRST SIMPLE FINANCE APP ON STREAMLIT")
st.write("""
# Financial App 

""")


st.write("First we will use Amazon Stocks for the example")

stock = 'AMZN'

# Get stock data
get_stock_data = yf.Ticker(stock)

# Set the time line of your data
ticket_df = get_stock_data.history(period='1d', start='2021-1-02', end='2021-12-12')

# Show your data in line chart
st.line_chart(ticket_df.Close)
st.line_chart(ticket_df.Volume)