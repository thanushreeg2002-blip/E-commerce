import streamlit as st

st.title("💳 Payment - ShopMate")

if "total" not in st.session_state:
    st.warning("No order found")
    st.stop()

st.subheader(f"Total Amount: ${st.session_state['total']}")

# User details
name = st.text_input("Full Name")
address = st.text_area("Delivery Address")

payment_method = st.radio(
    "Select Payment Method",
    ["Credit Card", "Debit Card", "Cash on Delivery"]
)

if payment_method in ["Credit Card", "Debit Card"]:
    card_number = st.text_input("Card Number")
    cvv = st.text_input("CVV", type="password")

if st.button("Pay Now"):

    if name == "" or address == "":
        st.error("Please fill all details")
    else:
        st.success("✅ Payment Successful!")
        st.balloons()

        # Clear cart after payment
        st.session_state["cart"] = []

        st.write("🎉 Your order has been placed successfully!")