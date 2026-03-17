import streamlit as st
import pandas as pd

st.title("Products")

if "login" not in st.session_state:
    st.warning("Please login first")
    st.stop()

df = pd.read_csv("products.csv")

st.dataframe(df)