import streamlit as st

from utils.helpers import (
    safe_mode,
    safe_idxmax,
    format_currency
)


def show_insights(df):

    highest_priced_brand = safe_idxmax(
        df.groupby("brand")["price_usd"].mean()
    )

    most_common_ram = safe_mode(
        df["ram_gb"]
    )

    most_common_storage = safe_mode(
        df["storage_gb"]
    )

    most_common_battery = safe_mode(
        df["battery_mah"]
    )

    avg_price = df["price_usd"].mean()

    avg_weight = df["weight_g"].mean()

    st.markdown(
        "## Business Insights"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            f"""
Highest priced brand: {highest_priced_brand}

Average smartphone price: {format_currency(avg_price)}

Average smartphone weight: {avg_weight:.0f} g
"""
        )

    with col2:

        st.info(
            f"""
Most common RAM: {most_common_ram} GB

Most common storage: {most_common_storage} GB

Most common battery: {most_common_battery} mAh
"""
        )