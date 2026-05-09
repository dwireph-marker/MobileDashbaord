# =====================================================
# FILE: components/sidebar.py
# =====================================================

import streamlit as st


# =====================================================
# SIDEBAR FILTER FUNCTION
# =====================================================

def sidebar_filters(df):

    # =================================================
    # EMPTY DATABASE CHECK
    # =================================================

    if df.empty:

        st.sidebar.warning(
            "Database is empty. Add devices first."
        )

        return df, []

    # =================================================
    # SIDEBAR TITLE
    # =================================================

    st.sidebar.markdown(
        "## Dashboard Filters"
    )

    # =================================================
    # FILTER OPTIONS
    # =================================================

    available_filters = [

        "Brand",
        "Model",
        "Price",
        "RAM",
        "Storage",
        "Camera",
        "Battery",
        "Display Size",
        "Charging Watt",
        "5G Support",
        "Operating System",
        "Processor",
        "Weight",
        "Rating",
        "Release Month",
        "Year"
    ]

    # =================================================
    # FILTER SELECTION
    # =================================================

    selected_filters = st.sidebar.multiselect(
        "Select Filters",
        options=available_filters,
        default=[]
    )

    # =================================================
    # COPY DATAFRAME
    # =================================================

    filtered_df = df.copy()

    # =================================================
    # BRAND FILTER
    # =================================================

    if "Brand" in selected_filters:

        brand_filter = st.sidebar.multiselect(
            "Select Brand",
            options=sorted(df["brand"].dropna().unique()),
            default=[]
        )

        if brand_filter:

            filtered_df = filtered_df[
                filtered_df["brand"].isin(
                    brand_filter
                )
            ]

    # =================================================
    # MODEL FILTER
    # =================================================

    if "Model" in selected_filters:

        model_filter = st.sidebar.multiselect(
            "Select Model",
            options=sorted(
                filtered_df["model"]
                .dropna()
                .unique()
            ),
            default=[]
        )

        if model_filter:

            filtered_df = filtered_df[
                filtered_df["model"].isin(
                    model_filter
                )
            ]

    # =================================================
    # RAM FILTER
    # =================================================

    if "RAM" in selected_filters:

        ram_filter = st.sidebar.multiselect(
            "Select RAM (GB)",
            options=sorted(
                filtered_df["ram_gb"]
                .dropna()
                .unique()
            ),
            default=[]
        )

        if ram_filter:

            filtered_df = filtered_df[
                filtered_df["ram_gb"].isin(
                    ram_filter
                )
            ]

    # =================================================
    # STORAGE FILTER
    # =================================================

    if "Storage" in selected_filters:

        storage_filter = st.sidebar.multiselect(
            "Select Storage (GB)",
            options=sorted(
                filtered_df["storage_gb"]
                .dropna()
                .unique()
            ),
            default=[]
        )

        if storage_filter:

            filtered_df = filtered_df[
                filtered_df["storage_gb"].isin(
                    storage_filter
                )
            ]

    # =================================================
    # CAMERA FILTER
    # =================================================

    if "Camera" in selected_filters:

        camera_filter = st.sidebar.multiselect(
            "Select Camera MP",
            options=sorted(
                filtered_df["camera_mp"]
                .dropna()
                .unique()
            ),
            default=[]
        )

        if camera_filter:

            filtered_df = filtered_df[
                filtered_df["camera_mp"].isin(
                    camera_filter
                )
            ]

    # =================================================
    # BATTERY FILTER
    # =================================================

    if "Battery" in selected_filters:

        battery_filter = st.sidebar.multiselect(
            "Select Battery",
            options=sorted(
                filtered_df["battery_mah"]
                .dropna()
                .unique()
            ),
            default=[]
        )

        if battery_filter:

            filtered_df = filtered_df[
                filtered_df["battery_mah"].isin(
                    battery_filter
                )
            ]

    # =================================================
    # DISPLAY FILTER
    # =================================================

    if "Display Size" in selected_filters:

        display_filter = st.sidebar.multiselect(
            "Select Display Size",
            options=sorted(
                filtered_df["display_size_inch"]
                .dropna()
                .unique()
            ),
            default=[]
        )

        if display_filter:

            filtered_df = filtered_df[
                filtered_df[
                    "display_size_inch"
                ].isin(display_filter)
            ]

    # =================================================
    # PRICE FILTER
    # =================================================

    if "Price" in selected_filters:

        min_price = int(
            filtered_df["price_inr"].min()
        )

        max_price = int(
            filtered_df["price_inr"].max()
        )

        price_filter = st.sidebar.slider(
            "Select Price Range ($)",
            min_value=min_price,
            max_value=max_price,
            value=(min_price, max_price)
        )

        filtered_df = filtered_df[

            (
                filtered_df["price_inr"]
                >= price_filter[0]
            )

            &

            (
                filtered_df["price_inr"]
                <= price_filter[1]
            )
        ]

    # =================================================
    # EMPTY FILTERED DATA
    # =================================================

    if filtered_df.empty:

        st.sidebar.warning(
            "No matching data found."
        )

    # =================================================
    # RETURN DATA
    # =================================================

    return filtered_df, selected_filters