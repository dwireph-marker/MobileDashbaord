import streamlit as st
import pandas as pd

# =====================================================
# STYLING
# =====================================================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

    [data-testid="stHorizontalBlock"] {
        gap: 32px !important;
    }

    .kpi-row-spacer {
        margin-top: 32px !important;
    }

    .kpi-card {
        background: #0f172a; 
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 24px;
        padding: 24px;
        height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: transform 0.3s ease;
    }

    .kpi-header {
        display: flex;
        align-items: center;
        gap: 16px;
    }

    .kpi-icon {
        width: 48px;
        height: 48px;
        border-radius: 14px;
        background: #3b82f6;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
    }

    .kpi-icon i {
        color: white;
        font-size: 22px;
    }

    .kpi-title {
        font-size: 0.9rem;
        font-weight: 600;
        color: #94a3b8;
    }

    .kpi-value {
        font-size: 2.5rem;
        font-weight: 800;
        color: #ffffff;
        letter-spacing: -1px;
        line-height: 1;
    }
    </style>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    """,
    unsafe_allow_html=True
)

# =====================================================
# HELPERS
# =====================================================
def format_inr(number):
    s = str(int(number))
    if len(s) <= 3: return "₹" + s
    last_three, others = s[-3:], s[:-3]
    res = ""
    while len(others) > 2:
        res = "," + others[-2:] + res
        others = others[:-2]
    return "₹" + others + res + "," + last_three

def kpi_card(title, value, icon):
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-header">
                <div class="kpi-icon"><i class="{icon}"></i></div>
                <div class="kpi-title">{title}</div>
            </div>
            <div class="kpi-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# =====================================================
# MAIN FUNCTION (This MUST be named show_kpis)
# =====================================================
def show_kpis(df):
    total_brands, total_models = 0, 0
    avg_price_inr, max_battery, avg_ram, avg_weight = "₹0", "0mAh", "0GB", "0g"

    if not df.empty:
        total_brands = df["brand"].nunique()
        total_models = len(df)
        
        # Using raw price from your data (No 83x multiplication)
        avg_price_inr = format_inr(df["price_inr"].mean()) if pd.notnull(df["price_inr"].mean()) else "₹0"
        max_battery = f"{int(df['battery_mah'].max())}mAh" if pd.notnull(df['battery_mah'].max()) else "0mAh"
        avg_ram = f"{round(df['ram_gb'].mean(), 1)}GB" if pd.notnull(df['ram_gb'].mean()) else "0GB"
        w_col = "weight_g" if "weight_g" in df.columns else "weight"
        avg_weight = f"{round(df[w_col].mean())}g" if w_col in df.columns and pd.notnull(df[w_col].mean()) else "0g"

    data = [
        ("Brands", total_brands, "bi bi-tag-fill"),
        ("Models", total_models, "bi bi-phone-vibrate-fill"),
        ("Avg Price", avg_price_inr, "bi bi-currency-rupee"),
        ("Battery", max_battery, "bi bi-lightning-fill"),
        ("Avg RAM", avg_ram, "bi bi-cpu-fill"),
        ("Weight", avg_weight, "bi bi-bag-fill")
    ]


    # Row 1
    cols1 = st.columns(3)
    for i in range(3):
        with cols1[i]:
            kpi_card(data[i][0], data[i][1], data[i][2])

    # Row 2 with Top Margin Spacer
    st.markdown('<div class="kpi-row-spacer"></div>', unsafe_allow_html=True)
    cols2 = st.columns(3)
    for i in range(3):
        with cols2[i]:
            kpi_card(data[i+3][0], data[i+3][1], data[i+3][2])