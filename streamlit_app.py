import streamlit as st

st.title("Simple Input UI")

# Text input
name = st.text_input("Enter your name:")

# Number input
age = st.number_input("Enter your age:", min_value=0, max_value=120)

# Dropdown
gender = st.selectbox("Select gender:", ["Male", "Female", "Other"])

# Checkbox
agree = st.checkbox("I agree to the terms and conditions")

# Button action
if st.button("Submit"):
    if agree:
        st.success(f"Hello {name}! You are {age} years old and identified as {gender}.")
    else:
        st.warning("Please agree to the terms to continue.")
