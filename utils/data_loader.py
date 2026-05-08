import pandas as pd
import streamlit as st


@st.cache_data
def load_data():

    # Load Excel Dataset
    df = pd.read_excel("data/mobile_data.xlsx")

    # =========================================
    # DATA CLEANING
    # =========================================

    # Remove Null Values
    df.dropna(inplace=True)

    # Remove Duplicates
    df.drop_duplicates(inplace=True)

    # Standardize Brand Names
    df["brand"] = df["brand"].str.title()

    # Convert Numeric Columns
    numeric_cols = [
        "price_usd",
        "ram_gb",
        "storage_gb",
        "camera_mp",
        "battery_mah",
        "display_size_inch",
        "charging_watt",
        "rating",
        "year",
        "weight_g"
    ]

    for col in numeric_cols:

        if col in df.columns:

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

    # Remove Remaining Null Values
    df.dropna(inplace=True)

    return df