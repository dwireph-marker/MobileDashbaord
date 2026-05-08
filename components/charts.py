import streamlit as st
import plotly.express as px
import pandas as pd

from utils.helpers import apply_chart_style


def show_charts(df):

    # =====================================================
    # BRAND VS PRICE
    # =====================================================

    brand_price = (
        df.groupby("brand")["price_usd"]
        .mean()
        .reset_index()
    )

    fig1 = px.bar(
        brand_price,
        x="brand",
        y="price_usd",
        title="Brand-wise Average Price",
        color_discrete_sequence=["#3B82F6"]
    )

    apply_chart_style(fig1)

    # =====================================================
    # RAM DISTRIBUTION
    # =====================================================

    ram_dist = (
        df["ram_gb"]
        .value_counts()
        .reset_index()
    )

    ram_dist.columns = ["RAM", "Count"]

    fig2 = px.pie(
        ram_dist,
        names="RAM",
        values="Count",
        hole=0.55,
        title="RAM Distribution",
        color_discrete_sequence=[
            "#3B82F6",
            "#4ADE80",
            "#A78BFA",
            "#FACC15"
        ]
    )

    apply_chart_style(fig2)

    # =====================================================
    # BATTERY ANALYSIS
    # =====================================================

    battery_brand = (
        df.groupby("brand")["battery_mah"]
        .mean()
        .reset_index()
    )

    fig3 = px.bar(
        battery_brand,
        x="brand",
        y="battery_mah",
        title="Battery Comparison by Brand",
        color_discrete_sequence=["#4ADE80"]
    )

    apply_chart_style(fig3)

    # =====================================================
    # STORAGE DISTRIBUTION
    # =====================================================

    storage_dist = (
        df["storage_gb"]
        .value_counts()
        .reset_index()
    )

    storage_dist.columns = ["Storage", "Count"]

    fig4 = px.pie(
        storage_dist,
        names="Storage",
        values="Count",
        hole=0.55,
        title="Storage Distribution",
        color_discrete_sequence=[
            "#3B82F6",
            "#4ADE80",
            "#FACC15"
        ]
    )

    apply_chart_style(fig4)

    # =====================================================
    # PRICE HISTOGRAM
    # =====================================================

    fig5 = px.histogram(
        df,
        x="price_usd",
        nbins=20,
        title="Price Range Analysis",
        color_discrete_sequence=["#FACC15"]
    )

    apply_chart_style(fig5)

    # =====================================================
    # WEIGHT ANALYSIS
    # =====================================================

    weight_brand = (
        df.groupby("brand")["weight_g"]
        .mean()
        .reset_index()
    )

    fig6 = px.bar(
        weight_brand,
        x="brand",
        y="weight_g",
        title="Average Weight by Brand",
        color_discrete_sequence=["#A78BFA"]
    )

    apply_chart_style(fig6)

    # =====================================================
    # CAMERA ANALYSIS
    # =====================================================

    camera_brand = (
        df.groupby("brand")["camera_mp"]
        .mean()
        .reset_index()
    )

    fig7 = px.bar(
        camera_brand,
        x="brand",
        y="camera_mp",
        title="Average Camera MP by Brand",
        color_discrete_sequence=["#06B6D4"]
    )

    apply_chart_style(fig7)

    # =====================================================
    # DISPLAY SIZE ANALYSIS
    # =====================================================

    display_brand = (
        df.groupby("brand")["display_size_inch"]
        .mean()
        .reset_index()
    )

    fig8 = px.bar(
        display_brand,
        x="brand",
        y="display_size_inch",
        title="Average Display Size",
        color_discrete_sequence=["#F97316"]
    )

    apply_chart_style(fig8)

    # =====================================================
    # CHARGING WATT ANALYSIS
    # =====================================================

    charging_brand = (
        df.groupby("brand")["charging_watt"]
        .mean()
        .reset_index()
    )

    fig9 = px.bar(
        charging_brand,
        x="brand",
        y="charging_watt",
        title="Charging Speed Comparison",
        color_discrete_sequence=["#10B981"]
    )

    apply_chart_style(fig9)

    # =====================================================
    # 5G SUPPORT ANALYSIS
    # =====================================================

    fiveg_dist = (
        df["5g_support"]
        .value_counts()
        .reset_index()
    )

    fiveg_dist.columns = ["5G", "Count"]

    fig10 = px.pie(
        fiveg_dist,
        names="5G",
        values="Count",
        hole=0.55,
        title="5G Support Distribution",
        color_discrete_sequence=[
            "#3B82F6",
            "#EF4444"
        ]
    )

    apply_chart_style(fig10)

    # =====================================================
    # OPERATING SYSTEM ANALYSIS
    # =====================================================

    os_dist = (
        df["os"]
        .value_counts()
        .reset_index()
    )

    os_dist.columns = ["OS", "Count"]

    fig11 = px.bar(
        os_dist,
        x="OS",
        y="Count",
        title="Operating System Distribution",
        color_discrete_sequence=["#8B5CF6"]
    )

    apply_chart_style(fig11)

    # =====================================================
    # PROCESSOR ANALYSIS
    # =====================================================

    processor_dist = (
        df["processor"]
        .value_counts()
        .reset_index()
        .head(10)
    )

    processor_dist.columns = ["Processor", "Count"]

    fig12 = px.bar(
        processor_dist,
        x="Processor",
        y="Count",
        title="Top Processors",
        color_discrete_sequence=["#14B8A6"]
    )

    apply_chart_style(fig12)

    # =====================================================
    # RATING DISTRIBUTION
    # =====================================================

    fig13 = px.histogram(
        df,
        x="rating",
        nbins=10,
        title="Rating Distribution",
        color_discrete_sequence=["#A855F7"]
    )

    apply_chart_style(fig13)

    # =====================================================
    # RELEASE MONTH ANALYSIS
    # =====================================================

    month_dist = (
        df["release_month"]
        .value_counts()
        .reset_index()
    )

    month_dist.columns = ["Month", "Count"]

    fig14 = px.bar(
        month_dist,
        x="Month",
        y="Count",
        title="Release Month Distribution",
        color_discrete_sequence=["#F43F5E"]
    )

    apply_chart_style(fig14)

    # =====================================================
    # YEAR ANALYSIS
    # =====================================================

    year_dist = (
        df["year"]
        .value_counts()
        .reset_index()
        .sort_values("year")
    )

    year_dist.columns = ["Year", "Count"]

    fig15 = px.line(
        year_dist,
        x="Year",
        y="Count",
        title="Smartphone Release Trend"
    )

    apply_chart_style(fig15)

    # =====================================================
    # DASHBOARD GRID LAYOUT
    # =====================================================

    charts = [
        fig1, fig2, fig3,
        fig4, fig5, fig6,
        fig7, fig8, fig9,
        fig10, fig11, fig12,
        fig13, fig14, fig15
    ]

    for i in range(0, len(charts), 3):

        cols = st.columns(3)

        for j in range(3):

            if i + j < len(charts):

                with cols[j]:

                    st.plotly_chart(
                        charts[i + j],
                        use_container_width=True
                    )