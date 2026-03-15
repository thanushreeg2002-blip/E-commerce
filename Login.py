import streamlit as st
import pandas as pd

st.title("Product Login")

# Load CSV
try:
    df = pd.read_csv("products.csv")
except:
    st.error("products.csv file not found")
    st.stop()

# Login inputs
product_id = st.number_input("Enter Product ID", min_value=1, step=1)
title = st.text_input("Enter Product Title")

# Login button
if st.button("Login"):
    
    user = df[(df["id"] == product_id) & (df["title"] == title)]

    if not user.empty:
        st.success("Login Successful ✅")
        st.write("Product Details:")
        st.dataframe(user)
    else:
        st.error("Invalid Product ID or Title ❌")