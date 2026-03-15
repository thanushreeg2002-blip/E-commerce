import streamlit as st
import pandas as pd
import os

st.title("Product Registration")

# Input fields
product_id = st.number_input("Product ID", min_value=1, step=1)
title = st.text_input("Product Title")
description = st.text_area("Description")
category = st.text_input("Category")
price = st.number_input("Price", min_value=0.0)
discount = st.number_input("Discount Percentage", min_value=0.0)

# CSV file name
file_name = "products.csv"

# Register button
if st.button("Register Product"):
    
    new_data = {
        "id": product_id,
        "title": title,
        "description": description,
        "category": category,
        "price": price,
        "discountPercentage": discount
    }

    df = pd.DataFrame([new_data])

    if os.path.exists(file_name):
        df.to_csv(file_name, mode='a', header=False, index=False)
    else:
        df.to_csv(file_name, index=False)

    st.success("Product registered successfully!")

# Show existing products
if os.path.exists(file_name):
    st.subheader("Product List")
    data = pd.read_csv(file_name)
    st.dataframe(data)