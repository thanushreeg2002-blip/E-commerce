import streamlit as st
import pandas as pd

st.set_page_config(page_title="E-Commerce Store", layout="wide")

# Load data

df = pd.read_csv("products.csv")

st.title("🛒Sunday Bazaar")

# Sidebar filters

st.sidebar.header("Filters")

category = st.sidebar.selectbox(
"Select Category",
["All"] + list(df["category"].unique())
)

price_range = st.sidebar.slider(
"Select Price Range",
float(df["price"].min()),
float(df["price"].max()),
(float(df["price"].min()), float(df["price"].max()))
)

filtered_df = df.copy()

if category != "All":
    filtered_df = filtered_df[filtered_df["category"] == category]

    filtered_df = filtered_df[
    (filtered_df["price"] >= price_range[0]) &
    (filtered_df["price"] <= price_range[1])
    ]

# Show products

cols = st.columns(3)

for index, row in filtered_df.iterrows():


    col = cols[index % 3]

    with col:

        st.image(row["thumbnail"], width=200)

        st.subheader(row["title"])

        st.write(f"Category: {row['category']}")
        st.write(f"Brand: {row['brand']}")

        st.write(f"⭐ Rating: {row['rating']}")

        st.write(f"💰 Price: ${row['price']}")

        st.write(f"Stock: {row['stock']}")

        if row["availabilityStatus"] == "Low Stock":
            st.warning("Low Stock!")

        if st.button("Add to Cart", key=row["id"]):

            st.success(f"{row['title']} added to cart!")

