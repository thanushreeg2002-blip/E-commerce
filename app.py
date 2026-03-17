import streamlit as st

st.set_page_config(page_title="E-Commerce App")

st.title("🛒 Welcome to My E-Commerce Store")

st.write("Shop the best products online!")

col1, col2 = st.columns(2)

with col1:
    if st.button("Sign Up"):
        st.switch_page("pages/signUp.py")

with col2:
    if st.button("Sign In"):
        st.switch_page("pages/signIn.py")