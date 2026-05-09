# =====================================================
# FILE: components/admin_panel.py
# =====================================================

import streamlit as st

from components.admin.add_device import (
    show_add_device
)

from components.admin.edit_device import (
    show_edit_device
)

from components.admin.delete_device import (
    show_delete_device
)

# =====================================================
# ADMIN PANEL
# =====================================================

def show_admin_panel(df):

    st.markdown(
        "## Device Management"
    )

    if df.empty:

        st.info(
            "Database is empty. Add your first device."
        )

    # =================================================
    # TABS
    # =================================================

    tab1, tab2, tab3 = st.tabs([

        "Add Device",

        "Edit Device",

        "Delete Device"
    ])

    # =================================================
    # ADD DEVICE TAB
    # =================================================

    with tab1:

        show_add_device(df)

    # =================================================
    # EDIT DEVICE TAB
    # =================================================

    with tab2:

        show_edit_device(df)

    # =================================================
    # DELETE DEVICE TAB
    # =================================================

    with tab3:

        show_delete_device(df)