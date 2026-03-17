import streamlit as st
import pandas as pd
import os

st.title("User Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):

    # Check if users.csv exists
    if not os.path.exists("users.csv"):
        st.error("users.csv file not found. Please register first.")
        st.stop()

    # Read CSV
    df = pd.read_csv("users.csv")

    # Check if required columns exist
    required_columns = ["email", "password"]
    if not all(col in df.columns for col in required_columns):
        st.error("users.csv format is incorrect.")
        st.stop()

    # Clean data
    df["email"] = df["email"].astype(str).str.strip().str.lower()
    df["password"] = df["password"].astype(str).str.strip()

    email_input = email.strip().lower()
    password_input = password.strip()

    # Validate login
    user = df[(df["email"] == email_input) & (df["password"] == password_input)]

    if not user.empty:
        st.session_state["login"] = True
        st.success("Login Successful")
        st.switch_page("pages/products.py")
    else:
        st.error("Invalid Email or Password")