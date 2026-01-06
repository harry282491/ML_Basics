import streamlit as st
# Input values
a = st.number_input("Enter value for a ")
b = st.number_input("Enter value for b")
c = st.text_input("Enter value for c (string)")
# Addition
result = a + b
# Streamlit app
st.title("Addition App")
st.write(c)
st.write(f"The sum of {a}, {b} is: {result}")