# =====================================================
# FILE: components/admin/helpers.py
# =====================================================

def get_unique_options(df, column, fallback=None):

    if fallback is None:

        fallback = []

    if df.empty:

        return fallback

    return sorted(
        df[column]
        .dropna()
        .unique()
    )