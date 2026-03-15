import pandas as pd
import plotly.graph_objects as go

# Daten laden
rq5_df = pd.read_csv("data/rq5_data.csv")

# Datumsformat
rq5_df["date"] = pd.to_datetime(rq5_df["date"])


def create_rq5_figure(view_type="base"):
    fig = go.Figure()

    # Linie 1: Dairy PPI inflation
    fig.add_trace(
        go.Scatter(
            x=rq5_df["date"],
            y=rq5_df["dairy_ppi_yoy_pct"],
            mode="lines",
            name="Dairy PPI inflation"
        )
    )

    # Linie 2: Butter CPI inflation + Fläche dazwischen
    fig.add_trace(
        go.Scatter(
            x=rq5_df["date"],
            y=rq5_df["butter_yoy_pct"],
            mode="lines",
            name="Butter CPI inflation",
            fill="tonexty"
        )
    )

    # Optional: markiere Monate mit potenzieller margin expansion
    if view_type == "highlight":
        flagged_df = rq5_df[rq5_df["margin_expansion_flag"]]

        fig.add_trace(
            go.Scatter(
                x=flagged_df["date"],
                y=flagged_df["butter_yoy_pct"],
                mode="markers",
                name="Potential margin expansion"
            )
        )

    fig.add_hline(y=0, line_dash="dash", line_color="gray")

    fig.update_layout(
        title="Inflation Gap between Butter CPI and Dairy PPI over Time",
        xaxis_title="Date",
        yaxis_title="Year-over-year inflation rate (%)",
        height=500
    )

    return fig