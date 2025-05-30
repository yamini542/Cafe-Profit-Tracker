import streamlit as st
import pandas as pd

st.set_page_config(page_title="Café Profit Tracker", page_icon="☕")

st.title("☕ Café Profit Tracker")
st.markdown("Upload your daily order Excel file to track cost, revenue, and profit.")

# File uploader
uploaded_file = st.file_uploader("📂 Upload your Excel file", type=["xlsx", "xls"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)

        st.subheader("📄 Uploaded Data")
        st.dataframe(df)

        # Ensure required columns exist
        required_cols = {"Date", "Item", "Quantity", "Cost Price", "Selling Price"}
        if not required_cols.issubset(df.columns):
            st.error(f"❌ Please include the following columns: {', '.join(required_cols)}")
        else:
            # Calculations
            df["Revenue"] = df["Quantity"] * df["Selling Price"]
            df["Cost"] = df["Quantity"] * df["Cost Price"]
            df["Profit"] = df["Revenue"] - df["Cost"]

            st.subheader("💰 Calculated Results")
            st.dataframe(df[["Date", "Item", "Quantity", "Revenue", "Cost", "Profit"]])

            # Summary
            summary = df.groupby("Date")[["Revenue", "Cost", "Profit"]].sum().reset_index()
            st.subheader("📊 Daily Summary")
            st.dataframe(summary)

            # Charts
            st.line_chart(summary.set_index("Date"))

    except Exception as e:
        st.error(f"⚠️ Error processing file: {e}")
else:
    st.info("Please upload an Excel file to begin.")
