import streamlit as st
import pandas as pd

st.set_page_config(page_title="ShopMate", layout="wide")

# Load product data
df = pd.read_csv("products.csv")

st.title("🛒 ShopMate")

# Sidebar filters
st.sidebar.header("Filters")

category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + list(df["category"].dropna().unique())
)

price_range = st.sidebar.slider(
    "Select Price Range",
    float(df["price"].min()),
    float(df["price"].max()),
    (float(df["price"].min()), float(df["price"].max()))
)

# Filter products
filtered_df = df.copy()

if category != "All":
    filtered_df = filtered_df[filtered_df["category"] == category]

filtered_df = filtered_df[
    (filtered_df["price"] >= price_range[0]) &
    (filtered_df["price"] <= price_range[1])
]

# Display products
cols = st.columns(3)

for index, row in filtered_df.iterrows():

    col = cols[index % 3]

    with col:

        if "thumbnail" in row:
            st.image(row["thumbnail"], width=200)

        st.subheader(row["title"])

        st.write(f"Category: {row['category']}")

        if "brand" in row:
            st.write(f"Brand: {row['brand']}")

        if "rating" in row:
            st.write(f"⭐ Rating: {row['rating']}")

        st.write(f"💰 Price: ${row['price']}")

        if "stock" in row:
            st.write(f"Stock: {row['stock']}")

        if "availabilityStatus" in row and row["availabilityStatus"] == "Low Stock":
            st.warning("Low Stock!")

        if st.button("Add to Cart", key=row["id"]):
            st.success(f"{row['title']} added to cart!")