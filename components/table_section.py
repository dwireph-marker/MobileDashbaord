import streamlit as st


def show_table(df):

    st.markdown("## Filtered Dataset")

    st.dataframe(
        df,
        use_container_width=True
    )

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download Filtered Data",
        data=csv,
        file_name="filtered_mobile_data.csv",
        mime="text/csv"
    )