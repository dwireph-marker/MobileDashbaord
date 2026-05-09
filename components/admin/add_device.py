# =====================================================
# FILE: components/admin/add_device.py
# =====================================================

import streamlit as st

from database.mongodb import (
    add_device
)

# =====================================================
# ADD DEVICE
# =====================================================

def show_add_device(df):

    st.subheader(
        "Add New Device"
    )

    # =============================================
    # EXISTING VALUES FOR DROPDOWNS
    # =============================================

    brand_options = sorted(
        df["brand"].dropna().unique()
    ) if not df.empty else []

    ram_options = sorted(
        df["ram_gb"].dropna().unique()
    ) if not df.empty else [4, 6, 8, 12, 16]

    storage_options = sorted(
        df["storage_gb"].dropna().unique()
    ) if not df.empty else [64, 128, 256, 512]

    processor_options = sorted(
        df["processor"].dropna().unique()
    ) if not df.empty else [

        "Snapdragon",

        "MediaTek",

        "Apple Bionic",

        "Exynos"
    ]

    os_options = sorted(
        df["os"].dropna().unique()
    ) if not df.empty else [

        "Android",

        "iOS"
    ]

    # =============================================
    # DEFAULT BRANDS
    # =============================================

    default_brands = [

        "Samsung",
        "Apple",
        "Xiaomi",
        "Realme",
        "OnePlus",
        "Oppo",
        "Vivo",
        "Motorola",
        "Google",
        "Nokia",
        "Infinix",
        "Tecno",
        "iQOO",
        "Poco",
        "Nothing",
        "Asus",
        "Sony",
        "Huawei"
    ]

    # =============================================
    # COMBINED BRAND LIST
    # =============================================

    all_brand_options = sorted(

        list(

            set(

                default_brands +

                list(brand_options)
            )
        )
    )

    # =============================================
    # BRAND SELECTOR
    # =============================================

    selected_brand = st.selectbox(

        "Select Brand",

        options=["Select Brand"] + all_brand_options + ["Custom Brand"],

        index=0,

        key="brand_dropdown"
    )

    # =============================================
    # CUSTOM BRAND INPUT
    # =============================================

    custom_brand = ""

    if selected_brand == "Custom Brand":

        custom_brand = st.text_input(
            "Enter Custom Brand",
            key="custom_brand_input"
        )

    # =============================================
    # FINAL BRAND VALUE
    # =============================================

    if selected_brand == "Custom Brand":

        brand = custom_brand

    else:

        brand = selected_brand

    # =============================================
    # MONTH OPTIONS
    # =============================================

    month_options = [

        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    # =============================================
    # YEAR OPTIONS
    # =============================================

    year_options = list(
        range(2020, 2031)
    )

    # =============================================
    # FORM
    # =============================================

    with st.form(
        "add_device_form"
    ):

        col1, col2 = st.columns(2)

        # =========================================
        # COLUMN 1
        # =========================================

        with col1:

            model = st.text_input(
                "Model"
            )

            price = st.number_input(
                "Price USD",
                min_value=0.0
            )

            ram = st.selectbox(

                "RAM GB",

                options=["Select RAM"] + list(ram_options),

                index=0
            )

            storage = st.selectbox(

                "Storage GB",

                options=["Select Storage"] + list(storage_options),

                index=0
            )

            camera = st.number_input(
                "Camera MP",
                min_value=0.0
            )

            battery = st.number_input(
                "Battery mAh",
                min_value=0.0
            )

            display = st.number_input(
                "Display Size",
                min_value=0.0
            )

        # =========================================
        # COLUMN 2
        # =========================================

        with col2:

            charging = st.number_input(
                "Charging Watt",
                min_value=0.0
            )

            support_5g = st.selectbox(
                "5G Support",
                ["Yes", "No"]
            )

            # =====================================
            # OPERATING SYSTEM
            # =====================================

            os_name = st.selectbox(

                "Operating System",

                options=["Select OS"] + list(os_options),

                index=0
            )

            # =====================================
            # PROCESSOR
            # =====================================

            processor = st.selectbox(

                "Processor",

                options=["Select Processor"] + list(processor_options),

                index=0
            )

            weight = st.number_input(
                "Weight (g)",
                min_value=0.0
            )

            rating = st.number_input(
                "Rating",
                min_value=0.0,
                max_value=5.0
            )

            release_month = st.selectbox(

                "Release Month",

                options=["Select Month"] + month_options,

                index=0
            )

            year = st.selectbox(

                "Year",

                options=["Select Year"] + year_options,

                index=0
            )

        # =========================================
        # SUBMIT BUTTON
        # =========================================

        submit = st.form_submit_button(
            "Add Device"
        )

        # =========================================
        # ADD DEVICE LOGIC
        # =========================================

        if submit:

            # =====================================
            # VALIDATION
            # =====================================

            if brand.strip() == "" or model.strip() == "":

                st.error(
                    "Brand and Model are required."
                )

            # =====================================
            # DROPDOWN VALIDATION
            # =====================================

            elif selected_brand == "Select Brand":

                st.error(
                    "Please select a brand."
                )

            elif ram == "Select RAM":

                st.error(
                    "Please select RAM."
                )

            elif storage == "Select Storage":

                st.error(
                    "Please select storage."
                )

            elif os_name == "Select OS":

                st.error(
                    "Please select operating system."
                )

            elif processor == "Select Processor":

                st.error(
                    "Please select processor."
                )

            elif release_month == "Select Month":

                st.error(
                    "Please select release month."
                )

            elif year == "Select Year":

                st.error(
                    "Please select year."
                )

            else:

                # =====================================
                # MODEL DUPLICATE CHECK
                # =====================================

                model_clean = (
                    model.strip().lower()
                )

                duplicate_exists = False

                if not df.empty:

                    duplicate_check = df[

                        (
                            df["model"]
                            .astype(str)
                            .str.strip()
                            .str.lower()
                            ==
                            model_clean
                        )
                    ]

                    if not duplicate_check.empty:

                        duplicate_exists = True

                # =====================================
                # DUPLICATE FOUND
                # =====================================

                if duplicate_exists:

                    st.error(
                        f"""
                        Model Already Exists

                        Model:
                        {model}
                        """
                    )

                else:

                    # =================================
                    # DEVICE DATA
                    # =================================

                    device_data = {

                        "brand": brand.strip(),

                        "model": model.strip(),

                        "price_inr": price,

                        "ram_gb": ram,

                        "storage_gb": storage,

                        "camera_mp": camera,

                        "battery_mah": battery,

                        "display_size_inch": display,

                        "charging_watt": charging,

                        "5g_support": support_5g,

                        "os": os_name.strip(),

                        "processor": processor.strip(),

                        "weight_g": weight,

                        "rating": rating,

                        "release_month": release_month.strip(),

                        "year": year
                    }

                    # =================================
                    # INSERT DEVICE
                    # =================================

                    inserted_id = add_device(
                        device_data
                    )

                    # =================================
                    # INSERT SUCCESS
                    # =================================

                    if inserted_id:

                        st.success(
                            f"""
                            Device Successfully Added

                            Brand: {brand}
                            Model: {model}

                            MongoDB ID:
                            {inserted_id}
                            """
                        )

                        st.balloons()

                        st.toast(
                            f"{model} added successfully",
                            icon="✅"
                        )

                        st.cache_data.clear()

                        st.rerun()

                    else:

                        st.error(
                            "Failed to add device to database."
                        )