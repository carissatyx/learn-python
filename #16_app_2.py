import streamlit as st
import pandas as pd
import numpy as np

st.header("Food")
st.write("Hello World")
x = st.text_input("Favourite_Movie?")

st.write(f"You like {x}")
is_clicked = st.button("Click me")

df = pd.read_csv('cni.csv')
st.write(df)

chart_data = pd.DataFrame(
    np.random.randn(20,4),
    columns=['a','b','c','d']
)

st.bar_chart(chart_data)
st.line_chart(chart_data)

st.link_button("Profile", url="/profile")