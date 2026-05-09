# =====================================================
# FILE: components/admin/delete_device.py
# =====================================================

import streamlit as st

from database.mongodb import (
    delete_device
)

# =====================================================
# DELETE DEVICE
# =====================================================

def show_delete_device(df):

    st.subheader(
        "Delete Device"
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

        delete_brand = st.selectbox(

            "Select Brand",

            options=["Select Brand"] + brand_list,

            index=0,

            key="delete_brand"
        )

        # =========================================
        # WAIT FOR BRAND
        # =========================================

        if delete_brand == "Select Brand":

            st.info(
                "Please select a brand."
            )

        else:

            # =====================================
            # FILTER DATA BY BRAND
            # =====================================

            delete_brand_df = df[

                df["brand"] == delete_brand
            ]

            # =====================================
            # MODEL LIST
            # =====================================

            delete_model_list = sorted(

                delete_brand_df[
                    "model"
                ]
                .dropna()
                .unique()
            )

            # =====================================
            # SELECT MODEL
            # =====================================

            delete_model = st.selectbox(

                "Select Model",

                options=["Select Model"] + delete_model_list,

                index=0,

                key="delete_model"
            )

            # =====================================
            # WAIT FOR MODEL
            # =====================================

            if delete_model == "Select Model":

                st.info(
                    "Please select a model."
                )

            else:

                # =================================
                # GET DEVICE DATA
                # =================================

                selected_delete_df = delete_brand_df[

                    delete_brand_df["model"]
                    == delete_model
                ]

                # =================================
                # SAFETY CHECK
                # =================================

                if selected_delete_df.empty:

                    st.error(
                        "Device data not found."
                    )

                else:

                    selected_delete_data = (
                        selected_delete_df
                        .iloc[0]
                    )

                    # =================================
                    # DEVICE PREVIEW
                    # =================================

                    st.warning(
                        f"""
                        You are about to delete:

                        Brand:
                        {selected_delete_data["brand"]}

                        Model:
                        {selected_delete_data["model"]}

                        Processor:
                        {selected_delete_data["processor"]}

                        RAM:
                        {selected_delete_data["ram_gb"]} GB

                        Storage:
                        {selected_delete_data["storage_gb"]} GB
                        """
                    )

                    # =================================
                    # DELETE BUTTON
                    # =================================

                    delete_btn = st.button(
                        "Delete Device",
                        type="primary"
                    )

                    # =================================
                    # DELETE LOGIC
                    # =================================

                    if delete_btn:

                        deleted = delete_device(
                            delete_model
                        )

                        # =============================
                        # SUCCESS
                        # =============================

                        if deleted:

                            st.cache_data.clear()

                            st.success(
                                f"""
                                Device Deleted Successfully

                                Brand:
                                {delete_brand}

                                Model:
                                {delete_model}
                                """
                            )

                            st.toast(
                                f"{delete_model} deleted",
                                icon="🗑️"
                            )

                            st.rerun()

                        else:

                            st.error(
                                "Failed to delete device."
                            )