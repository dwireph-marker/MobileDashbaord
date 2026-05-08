# =========================================================
# FILE: app.py
# =========================================================

import streamlit as st

# =====================================
# IMPORT COMPONENTS
# =====================================

from utils.data_loader import load_data

from components.styles import load_css

from components.sidebar import sidebar_filters

from components.kpi_cards import show_kpis

from components.charts import show_charts

from components.insights import show_insights

from components.table_section import show_table


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Mobile Brand Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# LOAD CSS
# =========================================================

load_css()

# =========================================================
# LOAD DATA
# =========================================================

df = load_data()

# =========================================================
# SIDEBAR FILTERS
# =========================================================

filtered_df, selected_filters = sidebar_filters(df)

# =========================================================
# DASHBOARD HEADER
# =========================================================

st.markdown(
    """
    <div class="dashboard-title">
        Mobile Brand Dashboard
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="dashboard-subtitle">
        Professional analytics and insights for smartphone market performance
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# SHOW CONTENT ONLY IF FILTER SELECTED
# =========================================================

if len(selected_filters) > 0:

    # =====================================
    # KPI SECTION
    # =====================================

    show_kpis(filtered_df)

    # =====================================
    # CHART SECTION
    # =====================================

    show_charts(filtered_df)

    # =====================================
    # INSIGHTS SECTION
    # =====================================

    show_insights(filtered_df)

    # =====================================
    # TABLE SECTION
    # =====================================

    show_table(filtered_df)

else:

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.info(
        """
        Select at least one filter from the sidebar to display dashboard analytics.
        """
    )