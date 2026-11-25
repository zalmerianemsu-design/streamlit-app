import streamlit as st
import pandas as pd
import numpy as np

st.header("ZEDRIC D. ALMERIA")

st.title("My First Streamlit App")
st.write("Built following the DataCamp Streamlit tutorial.")

df = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])

st.subheader("Data Table")
st.dataframe(df)

st.subheader("Line Chart")
st.line_chart(df)

st.subheader("Bar Chart")
st.bar_chart(df)

st.subheader("Interactive Widgets")
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")

n = st.slider("Pick a number of rows to show", 1, 20, 5)
st.table(df.head(n))
