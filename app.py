import streamlit as st
import pandas as pd

# Load the Excel file
data = pd.read_excel("cafe_orders_data.xlsx")

# Display data
st.title("☕ Café Profit Tracker")
st.dataframe(data)

# Calculate total revenue and profit
data["Revenue"] = data["Quantity"] * data["Selling Price"]
data["Cost"] = data["Quantity"] * data["Cost Price"]
data["Profit"] = data["Revenue"] - data["Cost"]

# Weekly summary
daily = data.groupby("Date")[["Revenue", "Cost", "Profit"]].sum().reset_index()
st.subheader("📅 This Week Sales")
st.dataframe(daily)

# Optional: show charts
st.line_chart(daily.set_index("Date")[["Revenue", "Cost", "Profit"]])
