#import library yg dibutuhkan

import streamlit as st

from web_function import load_data

import home, predict, visualise

Tabs = {
    "Home" : home,
    "Prediction" : predict,
    "Visualitation" : visualise
}

#membuat sidebar
st.sidebar.title("Navigasi")

#membuat radio option
page = st.sidebar.radio("Pages", list(Tabs.keys()))

#load dataset
df, x, y = load_data()

#kondisi call app function
if page in ["Prediction", "Visualitation"]:
    Tabs[page].app(x,y)
else:
    Tabs[page].app()