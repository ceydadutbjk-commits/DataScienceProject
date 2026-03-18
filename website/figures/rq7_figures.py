import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Daten laden
rq7_df = pd.read_csv("data/rq7_data.csv")

# Datumsformat
rq7_df["month"] = pd.to_datetime(rq7_df["month"])


def create_rq7_figure(view_type="scatter"):
    if view_type == "timeseries":
        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=rq7_df["month"],
                y=rq7_df["inflation_yoy"],
                mode="lines+markers",
                name="Inflation YoY",
                hovertemplate="Month: %{x}<br>Inflation YoY: %{y:.2f}%<extra></extra>"
            )
        )

        fig.add_trace(
            go.Scatter(
                x=rq7_df["month"],
                y=rq7_df["article_count"],
                mode="lines+markers",
                name="Article Count",
                yaxis="y2",
                hovertemplate="Month: %{x}<br>Articles: %{y}<extra></extra>"
            )
        )

        fig.update_layout(
            title="Interactive Time Series: Inflation and Media Coverage",
            xaxis_title="Month",
            yaxis=dict(title="Inflation YoY (%)"),
            yaxis2=dict(
                title="Number of Articles",
                overlaying="y",
                side="right"
            ),
            hovermode="x unified",
            height=450
        )

        return fig

    scatter_df = rq7_df.copy()
    scatter_df = scatter_df.dropna(subset=["inflation_yoy", "article_count", "inflation_regime", "month"])
    scatter_df["inflation_regime"] = scatter_df["inflation_regime"].astype(str)

    low_df = scatter_df[scatter_df["inflation_regime"] == "lower_inflation"]
    high_df = scatter_df[scatter_df["inflation_regime"] == "high_inflation"]

    fig = go.Figure()

    if not low_df.empty:
        fig.add_trace(
            go.Scatter(
                x=low_df["inflation_yoy"],
                y=low_df["article_count"],
                mode="markers",
                name="Low inflation",
                marker=dict(size=10),
                text=low_df["month"].astype(str),
                hovertemplate=(
                    "Month: %{text}<br>"
                    "Inflation YoY: %{x:.2f}%<br>"
                    "Articles: %{y}<extra></extra>"
                )
            )
        )

    if not high_df.empty:
        fig.add_trace(
            go.Scatter(
                x=high_df["inflation_yoy"],
                y=high_df["article_count"],
                mode="markers",
                name="High inflation",
                marker=dict(size=12),
                text=high_df["month"].astype(str),
                hovertemplate=(
                    "Month: %{text}<br>"
                    "Inflation YoY: %{x:.2f}%<br>"
                    "Articles: %{y}<extra></extra>"
                )
            )
        )

    fig.update_layout(
        title="Relationship between Inflation and Media Coverage",
        xaxis_title="Inflation (Year-over-Year %)",
        yaxis_title="Number of Articles",
        height=450
    )

    return fig