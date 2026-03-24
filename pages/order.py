import streamlit as st
import pandas as pd

st.title("🛒 Your Cart - ShopMate")

if "cart" not in st.session_state or len(st.session_state["cart"]) == 0:
    st.warning("Your cart is empty")
    st.stop()

cart_df = pd.DataFrame(st.session_state["cart"])

st.subheader("Selected Products")
st.dataframe(cart_df[["title", "price"]])

# Total Price
total_price = cart_df["price"].sum()
st.subheader(f"Total Price: ${total_price}")

# Remove item option
remove_index = st.number_input("Enter index to remove item", min_value=0, step=1)

if st.button("Remove Item"):
    if remove_index < len(st.session_state["cart"]):
        st.session_state["cart"].pop(remove_index)
        st.success("Item removed")
        st.rerun()

# Proceed to payment
if st.button("Proceed to Payment 💳"):
    st.session_state["total"] = total_price
    st.switch_page("pages/payment.py")