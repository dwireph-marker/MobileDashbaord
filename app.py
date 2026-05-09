
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

from components.admin_panel import show_admin_panel


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
# NAVBAR
# =========================================================

st.markdown(
    """
    <style>
    .navbar {
        background: linear-gradient(90deg, #0F172A, #111827);
        padding: 18px;
        border-radius: 15px;
        margin-bottom: 25px;
        border: 1px solid rgba(255,255,255,0.08);
    }

    .navbar-title {
        color: white;
        font-size: 32px;
        font-weight: 700;
    }

    .navbar-subtitle {
        color: #94A3B8;
        font-size: 15px;
        margin-top: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =====================================================
# DASHBOARD HEADER
# =====================================================

# =====================================================
# DASHBOARD HEADER
# =====================================================

# =========================================================
# DASHBOARD HEADER
# =========================================================

st.markdown(
    """
    <div class="dashboard-title">
        Mobile Brand Dashboard
    </div>

    <div class="dashboard-subtitle">
        Professional analytics and device management platform
    </div>
    """,
    unsafe_allow_html=True
)
# =========================================================
# NAVIGATION MENU
# =========================================================

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Add Device",
        "All Devices"
    ]
)

# =========================================================
# DASHBOARD PAGE
# =========================================================

if menu == "Dashboard":

    # =====================================
    # SIDEBAR FILTERS
    # =====================================

    filtered_df, selected_filters = sidebar_filters(df)

    # =====================================
    # SHOW DASHBOARD ONLY IF FILTER SELECTED
    # =====================================

    if len(selected_filters) > 0:

        # KPI SECTION
        show_kpis(filtered_df)

        st.markdown("<br>", unsafe_allow_html=True)

        # CHART SECTION
        show_charts(filtered_df)

        st.markdown("<br>", unsafe_allow_html=True)

        # INSIGHTS SECTION
        show_insights(filtered_df)

        st.markdown("<br>", unsafe_allow_html=True)

        # TABLE SECTION
        show_table(filtered_df)

    else:

        st.info(
            "Select filters from the sidebar to display analytics."
        )

# =========================================================
# ADD DEVICE PAGE
# =========================================================

elif menu == "Add Device":

    st.markdown("## Add New Mobile Device")

    show_admin_panel(df)

# =========================================================
# ALL DEVICES PAGE
# =========================================================

elif menu == "All Devices":

    st.markdown("## All Mobile Devices")

    # =====================================
    # SEARCH BAR
    # =====================================

    search = st.text_input(
        "Search Device"
    )

    all_devices_df = df.copy()

    if search:

        search = str(search)

        all_devices_df = all_devices_df[

            (
                all_devices_df["brand"]
                .astype(str)
                .str.contains(search, case=False, na=False)
            )

            |

            (
                all_devices_df["model"]
                .astype(str)
                .str.contains(search, case=False, na=False)
            )

            |

            (
                all_devices_df["processor"]
                .astype(str)
                .str.contains(search, case=False, na=False)
            )

            |

            (
                all_devices_df["os"]
                .astype(str)
                .str.contains(search, case=False, na=False)
            )
        ]

    # =====================================
    # DEVICE COUNT
    # =====================================

    st.markdown(
        f"### Total Devices: {len(all_devices_df)}"
    )

    # =====================================
    # SHOW DATAFRAME
    # =====================================

    st.dataframe(
        all_devices_df,
        use_container_width=True,
        height=600
    )

    # =====================================
    # DOWNLOAD BUTTON
    # =====================================

    csv = all_devices_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download Device Data",
        data=csv,
        file_name="all_mobile_devices.csv",
        mime="text/csv"
    )


