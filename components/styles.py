# =========================================================
# FILE: components/styles.py
# =========================================================

import streamlit as st


# =========================================================
# LOAD CSS
# =========================================================

def load_css():

    # =====================================
    # PREVIOUS BASE STYLES
    # =====================================

    st.markdown(
        """
        <style>

        .stApp {

            background: #0B1426;

            color: white;
        }

        .dashboard-title {

            font-size: 42px;

            font-weight: bold;

            color: white;
        }

        .dashboard-subtitle {

            color: #94A3B8;

            margin-bottom: 25px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # =====================================
    # LOAD CUSTOM CSS FILE
    # =====================================

    with open(

        "assets/custom.css",

        encoding="utf-8"
    ) as css:

        st.markdown(

            f"""
            <style>
            {css.read()}
            </style>
            """,

            unsafe_allow_html=True
        )

    # =====================================
    # LOAD BOOTSTRAP ICONS
    # =====================================

    st.markdown(

        """
        <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
        """,

        unsafe_allow_html=True
    )