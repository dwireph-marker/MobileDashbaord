import streamlit as st
import pandas as pd
from utils.helpers import (
    safe_mode,
    safe_idxmax
)

def format_inr(number):
    """Helper to format numbers in Indian Rupee style with commas"""
    s = str(int(number))
    if len(s) <= 3:
        return "₹" + s
    last_three = s[-3:]
    others = s[:-3]
    res = ""
    while len(others) > 2:
        res = "," + others[-2:] + res
        others = others[:-2]
    return "₹" + others + res + "," + last_three

def show_insights(df):
    if df.empty:
        st.warning("No data available for insights.")
        return

    highest_priced_brand = safe_idxmax(
        df.groupby("brand")["price_inr"].mean()
    )

    most_common_ram = safe_mode(df["ram_gb"])
    most_common_storage = safe_mode(df["storage_gb"])
    most_common_battery = safe_mode(df["battery_mah"])

    avg_price = df["price_inr"].mean()
    
    # Check for weight column variation
    w_col = "weight_g" if "weight_g" in df.columns else "weight"
    avg_weight = df[w_col].mean() if w_col in df.columns else 0

    st.markdown("## Business Insights")

    col1, col2 = st.columns(2)

    with col1:
        st.info(
            f"""
**Highest priced brand:** {highest_priced_brand}

**Average smartphone price:** {format_inr(avg_price)}

**Average smartphone weight:** {avg_weight:.0f} g
"""
        )

    with col2:
        st.info(
            f"""
**Most common RAM:** {most_common_ram} GB

**Most common storage:** {most_common_storage} GB

**Most common battery:** {most_common_battery} mAh
"""
        )