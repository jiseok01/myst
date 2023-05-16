import streamlit as st
import pandas as pd
import numpy as np

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

st.title("this is the app title")

dp = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y'])
st.line_chart(df)
