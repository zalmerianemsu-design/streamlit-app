import streamlit as st
import pandas as pd
import numpy as np

st.header("ZEDRIC D. ALMERIA")

st.title("My First Streamlit App")
st.write("Built following the DataCamp Streamlit tutorial.")

# --- About me: photo + details ---
st.subheader("About Me")
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.image("photo1.jpg", caption="Zedric D. Almeria", width=250)

with col2:
    st.write("**Full name:** Zedric D. Almeria")
    st.write("**Course / Section:** BSME2B")
    st.write("**School:** North Eastern Mindanao State University")
    st.write("**Hobbies:** gaming, music, poems")
    st.write("**Goal:** My dream and goal is to finish my studies and fulfill my mom's dream of going to Disneyland.")

# --- My own data ---
st.subheader("My Weekly Study Hours")
my_data = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Hours": [2, 3, 1, 4, 2, 5, 3],
})
st.dataframe(my_data)
st.bar_chart(my_data.set_index("Day"))

# --- Random sample data from the tutorial ---
df = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])

st.subheader("Sample Data Table")
st.dataframe(df)

st.subheader("Line Chart")
st.line_chart(df)

# --- Calculator ---
st.subheader("ZEDRIC'S CALCULATOR")

num1 = st.number_input("First Number")
num2 = st.number_input("Second Number")

operation = st.selectbox("Operation", ["Multiply", "Divide", "Add", "Subtraction"])

if st.button("Calculate"):
    if operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        result = num1 / num2 if num2 != 0 else None
    elif operation == "Add":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2

    if result is None:
        st.error("You can't divide by zero.")
    else:
        st.write("HERE'S THE RESULT:", result)