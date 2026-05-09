# =====================================================
# FILE: components/admin/edit_device.py
# =====================================================

import streamlit as st

from database.mongodb import (
    update_device
)

# =====================================================
# EDIT DEVICE
# =====================================================

def show_edit_device(df):

    st.subheader(
        "Edit Existing Device"
    )

    if not df.empty:

        # =========================================
        # BRAND LIST
        # =========================================

        brand_list = sorted(
            df["brand"]
            .dropna()
            .unique()
        )

        # =========================================
        # SELECT BRAND
        # =========================================

        selected_brand = st.selectbox(

            "Select Brand",

            options=["Select Brand"] + brand_list,

            index=0,

            key="edit_brand"
        )

        # =========================================
        # WAIT FOR BRAND
        # =========================================

        if selected_brand == "Select Brand":

            st.info(
                "Please select a brand."
            )

        else:

            # =====================================
            # FILTER DATA BY BRAND
            # =====================================

            brand_filtered_df = df[

                df["brand"] == selected_brand
            ]

            # =====================================
            # MODEL LIST
            # =====================================

            model_list = sorted(

                brand_filtered_df[
                    "model"
                ]
                .dropna()
                .unique()
            )

            # =====================================
            # SELECT MODEL
            # =====================================

            selected_model = st.selectbox(

                "Select Model",

                options=["Select Model"] + model_list,

                index=0,

                key="edit_model"
            )

            # =====================================
            # WAIT FOR MODEL
            # =====================================

            if selected_model == "Select Model":

                st.info(
                    "Please select a model."
                )

            else:

                # =================================
                # GET SELECTED DEVICE
                # =================================

                selected_device_df = brand_filtered_df[

                    brand_filtered_df["model"]
                    == selected_model
                ]

                # =================================
                # SAFETY CHECK
                # =================================

                if selected_device_df.empty:

                    st.error(
                        "Device data not found."
                    )

                else:

                    selected_data = (
                        selected_device_df
                        .iloc[0]
                    )

                    # =============================
                    # UPDATE FORM
                    # =============================

                    with st.form(
                        "edit_device_form"
                    ):

                        col1, col2 = st.columns(2)

                        # =========================
                        # COLUMN 1
                        # =========================

                        with col1:

                            updated_brand = st.text_input(
                                "Brand",
                                value=str(
                                    selected_data["brand"]
                                )
                            )

                            updated_model = st.text_input(
                                "Model",
                                value=str(
                                    selected_data["model"]
                                )
                            )

                            updated_price = st.number_input(
                                "Price USD",
                                value=float(
                                    selected_data[
                                        "price_inr"
                                    ]
                                )
                            )

                            updated_ram = st.number_input(
                                "RAM GB",
                                value=float(
                                    selected_data[
                                        "ram_gb"
                                    ]
                                )
                            )

                            updated_storage = st.number_input(
                                "Storage GB",
                                value=float(
                                    selected_data[
                                        "storage_gb"
                                    ]
                                )
                            )

                            updated_camera = st.number_input(
                                "Camera MP",
                                value=float(
                                    selected_data[
                                        "camera_mp"
                                    ]
                                )
                            )

                            updated_battery = st.number_input(
                                "Battery mAh",
                                value=float(
                                    selected_data[
                                        "battery_mah"
                                    ]
                                )
                            )

                            updated_display = st.number_input(
                                "Display Size",
                                value=float(
                                    selected_data[
                                        "display_size_inch"
                                    ]
                                )
                            )

                        # =========================
                        # COLUMN 2
                        # =========================

                        with col2:

                            updated_charging = st.number_input(
                                "Charging Watt",
                                value=float(
                                    selected_data[
                                        "charging_watt"
                                    ]
                                )
                            )

                            updated_5g = st.selectbox(

                                "5G Support",

                                ["Yes", "No"],

                                index=0
                                if selected_data[
                                    "5g_support"
                                ] == "Yes"
                                else 1
                            )

                            updated_os = st.text_input(
                                "Operating System",
                                value=str(
                                    selected_data["os"]
                                )
                            )

                            updated_processor = st.text_input(
                                "Processor",
                                value=str(
                                    selected_data[
                                        "processor"
                                    ]
                                )
                            )

                            updated_weight = st.number_input(
                                "Weight (g)",
                                value=float(
                                    selected_data[
                                        "weight_g"
                                    ]
                                )
                            )

                            updated_rating = st.number_input(
                                "Rating",
                                min_value=0.0,
                                max_value=5.0,
                                value=float(
                                    selected_data[
                                        "rating"
                                    ]
                                )
                            )

                            updated_month = st.text_input(
                                "Release Month",
                                value=str(
                                    selected_data[
                                        "release_month"
                                    ]
                                )
                            )

                            updated_year = st.number_input(
                                "Year",
                                value=int(
                                    selected_data[
                                        "year"
                                    ]
                                )
                            )

                        # =========================
                        # UPDATE BUTTON
                        # =========================

                        update_btn = (
                            st.form_submit_button(
                                "Update Device"
                            )
                        )

                        # =========================
                        # UPDATE LOGIC
                        # =========================

                        if update_btn:

                            updated_data = {

                                "brand": updated_brand,

                                "model": updated_model,

                                "price_inr": updated_price,

                                "ram_gb": updated_ram,

                                "storage_gb": updated_storage,

                                "camera_mp": updated_camera,

                                "battery_mah": updated_battery,

                                "display_size_inch": updated_display,

                                "charging_watt": updated_charging,

                                "5g_support": updated_5g,

                                "os": updated_os,

                                "processor": updated_processor,

                                "weight_g": updated_weight,

                                "rating": updated_rating,

                                "release_month": updated_month,

                                "year": updated_year
                            }

                            updated = update_device(

                                selected_model,

                                updated_data
                            )

                            # =====================
                            # SUCCESS
                            # =====================

                            if updated:

                                st.success(
                                    f"""
                                    Device Updated Successfully

                                    Brand:
                                    {updated_brand}

                                    Model:
                                    {updated_model}
                                    """
                                )

                                st.toast(
                                    f"{updated_model} updated",
                                    icon="✅"
                                )

                                st.cache_data.clear()

                                st.rerun()

                            else:

                                st.warning(
                                    "No changes made."
                                )