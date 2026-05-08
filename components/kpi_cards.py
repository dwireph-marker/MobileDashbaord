import streamlit as st

from utils.helpers import (
    format_currency,
    format_battery,
    format_ram,
    format_weight
)


def show_kpis(df):

    total_brands = df["brand"].nunique()

    total_models = df["model"].nunique()

    avg_price = df["price_usd"].mean()

    highest_battery = df["battery_mah"].max()

    avg_ram = df["ram_gb"].mean()

    avg_weight = df["weight_g"].mean()

    k1, k2, k3, k4, k5, k6 = st.columns(6)

    with k1:
        st.metric(
            "Total Brands",
            total_brands
        )

    with k2:
        st.metric(
            "Total Models",
            total_models
        )

    with k3:
        st.metric(
            "Average Price",
            format_currency(avg_price)
        )

    with k4:
        st.metric(
            "Highest Battery",
            format_battery(highest_battery)
        )

    with k5:
        st.metric(
            "Average RAM",
            format_ram(avg_ram)
        )

    with k6:
        st.metric(
            "Average Weight",
            format_weight(avg_weight)
        )