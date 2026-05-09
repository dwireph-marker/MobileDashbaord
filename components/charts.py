import streamlit as st
import plotly.express as px
import pandas as pd
from utils.helpers import apply_chart_style

def show_charts(df):
    if df.empty:
        st.warning("No data available for the current selection.")
        return

    # 1. CHRONOLOGICAL SORTING
    # Ensure models are arranged by year (iPhone 11 -> 12 -> 13)
    df = df.sort_values("year")

    # 2. DATA CORRECTION
    # Your price_inr column already contains large numbers (e.g., 64900).
    # We map it directly to price_inr without multiplying by 83 to avoid inflation.
    if "price_inr" not in df.columns:
        df["price_inr"] = df["price_inr"]

    # Check if we are looking at a single brand or multiple
    is_single_brand = df["brand"].nunique() == 1
    current_brand = df["brand"].iloc[0] if is_single_brand else ""

    # Grouping logic (sort=False preserves our chronological 'year' sort)
    group_col = "model" if is_single_brand else "brand"
    title_suffix = f"for {current_brand}" if is_single_brand else "by Brand"

    # =====================================================
    # 1. PRICE ANALYSIS (Fixed Inflation & Sort)
    # =====================================================
    brand_price = df.groupby(group_col, sort=False)["price_inr"].mean().reset_index()
    
    fig1 = px.bar(
        brand_price, 
        x=group_col, 
        y="price_inr",
        title=f"Average Price {title_suffix} (₹)",
        color_discrete_sequence=["#3B82F6"],
        text_auto='.2s' # Formats labels as 65k, 1.2k etc.
    )
    
    # Apply Indian formatting to axes
    fig1.update_layout(
        yaxis_tickprefix='₹', 
        yaxis_tickformat=',',
        xaxis_title="Model Name" if is_single_brand else "Brand Name",
        yaxis_title="Price (INR)"
    )
    apply_chart_style(fig1)

    # =====================================================
    # 2. RAM DISTRIBUTION (Grouped for Clarity)
    # =====================================================
    ram_dist = df["ram_gb"].value_counts().reset_index()
    ram_dist.columns = ["RAM", "Count"]
    
    if len(ram_dist) > 6:
        top_ram = ram_dist.iloc[:5].copy()
        other_ram = pd.DataFrame([{"RAM": "Other", "Count": ram_dist.iloc[5:]["Count"].sum()}])
        ram_dist = pd.concat([top_ram, other_ram])

    fig2 = px.pie(
        ram_dist, names="RAM", values="Count",
        hole=0.55, title=f"RAM Distribution {title_suffix}",
        color_discrete_sequence=["#3B82F6", "#4ADE80", "#A78BFA", "#FACC15", "#FB7185", "#94A3B8"]
    )
    fig2.update_traces(textposition='inside', textinfo='percent+label')
    apply_chart_style(fig2)

    # =====================================================
    # 3. BATTERY ANALYSIS
    # =====================================================
    battery_data = df.groupby(group_col, sort=False)["battery_mah"].mean().reset_index()
    fig3 = px.bar(
        battery_data, x=group_col, y="battery_mah",
        title=f"Battery Comparison {title_suffix}",
        color_discrete_sequence=["#4ADE80"], text_auto=True
    )
    apply_chart_style(fig3)

    # =====================================================
    # 4. STORAGE DISTRIBUTION
    # =====================================================
    storage_dist = df["storage_gb"].value_counts().reset_index()
    storage_dist.columns = ["Storage", "Count"]
    
    if len(storage_dist) > 5:
        top_s = storage_dist.iloc[:4].copy()
        other_s = pd.DataFrame([{"Storage": "Other", "Count": storage_dist.iloc[4:]["Count"].sum()}])
        storage_dist = pd.concat([top_s, other_s])

    fig4 = px.pie(
        storage_dist, names="Storage", values="Count",
        hole=0.55, title=f"Storage Distribution {title_suffix}",
        color_discrete_sequence=["#3B82F6", "#4ADE80", "#FACC15", "#94A3B8"]
    )
    fig4.update_traces(textposition='inside', textinfo='percent')
    apply_chart_style(fig4)

    # =====================================================
    # 5. PRICE RANGE
    # =====================================================
    fig5 = px.histogram(
        df, x="price_inr", nbins=15,
        title=f"Price Spread {title_suffix} (₹)",
        color_discrete_sequence=["#FACC15"]
    )
    fig5.update_layout(xaxis_tickprefix='₹', xaxis_tickformat=',')
    apply_chart_style(fig5)

    # =====================================================
    # 6. CAMERA QUALITY
    # =====================================================
    camera_data = df.groupby(group_col, sort=False)["camera_mp"].mean().reset_index()
    fig6 = px.bar(
        camera_data, x=group_col, y="camera_mp",
        title=f"Camera Specs {title_suffix}",
        color_discrete_sequence=["#06B6D4"]
    )
    apply_chart_style(fig6)

    # =====================================================
    # 7. 5G SUPPORT
    # =====================================================
    fiveg_dist = df["5g_support"].value_counts().reset_index()
    fiveg_dist.columns = ["5G", "Count"]
    fig7 = px.pie(
        fiveg_dist, names="5G", values="Count", hole=0.55,
        title=f"5G Readiness {title_suffix}",
        color_discrete_sequence=["#3B82F6", "#EF4444"]
    )
    apply_chart_style(fig7)

    # =====================================================
    # 8. PROCESSOR TOP LIST
    # =====================================================
    proc_dist = df["processor"].value_counts().reset_index().head(10)
    proc_dist.columns = ["Processor", "Count"]
    fig8 = px.bar(
        proc_dist, x="Count", y="Processor", orientation='h',
        title=f"Top Processors {title_suffix}",
        color_discrete_sequence=["#14B8A6"]
    )
    fig8.update_layout(yaxis={'categoryorder':'total ascending'})
    apply_chart_style(fig8)

    # =====================================================
    # 9. RELEASE TREND
    # =====================================================
    year_dist = df.groupby("year").size().reset_index(name="Count")
    year_dist["year"] = year_dist["year"].astype(str)
    fig9 = px.line(
        year_dist, x="year", y="Count", markers=True,
        title=f"Release Trend {title_suffix}",
        color_discrete_sequence=["#F43F5E"]
    )
    apply_chart_style(fig9)

    # =====================================================
    # DASHBOARD GRID LAYOUT (3x3)
    # =====================================================
    all_charts = [fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8, fig9]
    
    for i in range(0, len(all_charts), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(all_charts):
                with cols[j]:
                    st.plotly_chart(all_charts[i + j], use_container_width=True)