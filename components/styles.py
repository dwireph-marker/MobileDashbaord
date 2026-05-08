import streamlit as st


def load_css():

    st.markdown("""
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
    """, unsafe_allow_html=True)