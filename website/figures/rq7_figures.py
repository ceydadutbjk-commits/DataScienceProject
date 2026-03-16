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

    fig = px.scatter(
        rq7_df,
        x="inflation_yoy",
        y="article_count",
        color="inflation_regime",
        size="article_count",
        hover_data=["month"],
        title="Relationship between Inflation and Media Coverage"
    )

    fig.update_layout(
        xaxis_title="Inflation (Year-over-Year %)",
        yaxis_title="Number of Articles",
        height=450
    )

    return fig