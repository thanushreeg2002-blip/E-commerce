import streamlit as st
import pandas as pd

st.title("User Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):

    df = pd.read_csv("users.csv")

    user = df[(df["email"] == email) & (df["password"] == password)]

    if not user.empty:
        st.session_state["login"] = True
        st.success("Login Successful")
        st.switch_page("pages/products.py")
    else:
        st.error("Invalid Email or Password")