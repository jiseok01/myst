import streamlit as st
import pandas as pd
import numpy as np

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

st.title("this is the app title")

df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y'])
st.line_chart(df)

df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],
columns=['lat', 'lon']
st.map(df)
