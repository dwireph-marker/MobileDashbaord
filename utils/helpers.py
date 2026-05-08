import plotly.graph_objects as go


# =========================================
# FORMAT CURRENCY
# =========================================
def format_currency(value):

    return f"${value:,.0f}"


# =========================================
# FORMAT BATTERY
# =========================================
def format_battery(value):

    return f"{value} mAh"


# =========================================
# FORMAT RAM
# =========================================
def format_ram(value):

    return f"{value:.1f} GB"


# =========================================
# FORMAT WEIGHT
# =========================================
def format_weight(value):

    return f"{value:.0f} g"


# =========================================
# SAFE MODE
# =========================================
def safe_mode(series, default="N/A"):

    if not series.mode().empty:
        return series.mode()[0]

    return default


# =========================================
# SAFE IDXMAX
# =========================================
def safe_idxmax(series, default="N/A"):

    if not series.empty:
        return series.idxmax()

    return default


# =========================================
# APPLY CHART STYLE
# =========================================
def apply_chart_style(fig, height=360):

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font_color="white",

        title_font_size=20,

        height=height,

        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        )
    )

    return fig