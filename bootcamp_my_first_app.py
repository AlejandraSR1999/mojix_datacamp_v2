import streamlit as st
import pandas as pd
import numpy as np
import plost
from PIL import Image

st.set_page_config(layout="wide")
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.write("STREAMLIT BLOGS")
st.write("""
# WHAT IS A DASHBOARD? 

""")

st.write("The dashboard is like the gauges in the cockpit of an airplane (although it should be a bit simpler!).\n it's a super-powerful tool for getting insights from data and centralizing the KPIs you need to know what's really going on with your business. \n In this article we are going to see what a dashboard is, why it is a good idea to implement it in your company and the main metrics to include according to your objectives")

st.write("""
# WHAT IS A DASHBOARD? 

""")

# Data
seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')

# Row A
a1, a2, a3 = st.columns(3)
a1.image(Image.open('streamlit-logo-secondary-colormark-darktext.png'))
a2.metric("Wind", "9 mph", "-8%")
a3.metric("Humidity", "86%", "4%")

# Row B
b1, b2, b3, b4 = st.columns(4)
b1.metric("Temperature", "70 °F", "1.2 °F")
b2.metric("Wind", "9 mph", "-8%")
b3.metric("Humidity", "86%", "4%")
b4.metric("Humidity", "86%", "4%")

# Row C
c1, c2 = st.columns((7,3))
with c1:
    st.markdown('### Heatmap')
    plost.time_hist(
    data=seattle_weather,
    date='date',
    x_unit='week',
    y_unit='day',
    color='temp_max',
    aggregate='median',
    legend=None)
with c2:
    st.markdown('### Bar chart')
    plost.donut_chart(
        data=stocks,
        theta='q2',
        color='company')