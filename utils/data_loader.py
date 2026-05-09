# =====================================================
# FILE: utils/data_loader.py
# =====================================================

import pandas as pd
import streamlit as st

from database.mongodb import get_all_devices


# =====================================================
# DEFAULT COLUMNS
# =====================================================

DEFAULT_COLUMNS = [

    "brand",
    "model",
    "price_inr",
    "ram_gb",
    "storage_gb",
    "camera_mp",
    "battery_mah",
    "display_size_inch",
    "charging_watt",
    "5g_support",
    "os",
    "processor",
    "weight_g",
    "rating",
    "release_month",
    "year"
]


# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_data():

    try:

        # =========================================
        # FETCH DATA FROM MONGODB
        # =========================================

        data = get_all_devices()

        # =========================================
        # EMPTY DATABASE
        # =========================================

        if not data:

            return pd.DataFrame(
                columns=DEFAULT_COLUMNS
            )

        # =========================================
        # CREATE DATAFRAME
        # =========================================

        df = pd.DataFrame(data)

        # =========================================
        # ENSURE ALL COLUMNS EXIST
        # =========================================

        for col in DEFAULT_COLUMNS:

            if col not in df.columns:

                df[col] = None

        # =========================================
        # REMOVE MONGODB _id
        # =========================================

        if "_id" in df.columns:

            df.drop(
                columns=["_id"],
                inplace=True
            )

        # =========================================
        # BRAND CLEANING
        # =========================================

        df["brand"] = (
            df["brand"]
            .astype(str)
            .str.title()
            .str.strip()
        )

        # =========================================
        # STRING COLUMNS
        # =========================================

        string_columns = [

            "brand",
            "model",
            "5g_support",
            "os",
            "processor",
            "release_month"
        ]

        for col in string_columns:

            df[col] = (
                df[col]
                .astype(str)
                .str.strip()
            )

        # =========================================
        # NUMERIC COLUMNS
        # =========================================

        numeric_columns = [

            "price_inr",
            "ram_gb",
            "storage_gb",
            "camera_mp",
            "battery_mah",
            "display_size_inch",
            "charging_watt",
            "weight_g",
            "rating",
            "year"
        ]

        for col in numeric_columns:

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

        # =========================================
        # RESET INDEX
        # =========================================

        df.reset_index(
            drop=True,
            inplace=True
        )

        return df

    except Exception as e:

        st.error(
            f"Database Error: {e}"
        )

        return pd.DataFrame(
            columns=DEFAULT_COLUMNS
        )