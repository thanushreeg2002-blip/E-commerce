import streamlit as st
import pandas as pd
import os

st.title("User Registration")

name = st.text_input("Name")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Register"):

    new_user = {
        "name": name,
        "email": email,
        "password": password
    }

    df = pd.DataFrame([new_user])

    if os.path.exists("users.csv"):
        df.to_csv("users.csv", mode="a", header=False, index=False)
    else:
        df.to_csv("users.csv", index=False)

    st.success("Registration Successful! Please Login")