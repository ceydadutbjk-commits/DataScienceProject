import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Daten laden
rq3_df = pd.read_csv("data/rq3_data.csv")

# Datumsformat
rq3_df["datum"] = pd.to_datetime(rq3_df["datum"])


def create_rq3_figure(view_type="bubble"):

    if view_type == "heatmap":
        heatmap_df = (
            rq3_df.assign(
                year=rq3_df["datum"].dt.year,
                month=rq3_df["datum"].dt.month
            )
            .pivot(index="year", columns="month", values="residual_zscore")
            .reindex(columns=range(1, 13))
        )

        fig = px.imshow(
            heatmap_df,
            labels=dict(x="Month", y="Year", color="Residual z-score"),
            x=heatmap_df.columns,
            y=heatmap_df.index,
            title="Residual z-scores by Year and Month",
            aspect="auto"
        )

        return fig

    plot_df = rq3_df.copy()
    plot_df = plot_df.dropna(subset=["datum", "residual", "residual_zscore", "significant_deviation"])
    plot_df["bubble_size"] = plot_df["residual_zscore"].abs() * 20
    plot_df["significant_deviation"] = plot_df["significant_deviation"].astype(bool)

    significant_df = plot_df[plot_df["significant_deviation"] == True]
    not_significant_df = plot_df[plot_df["significant_deviation"] == False]

    fig = go.Figure()

    if not not_significant_df.empty:
        fig.add_trace(
            go.Scatter(
                x=not_significant_df["datum"],
                y=not_significant_df["residual"],
                mode="markers",
                name="Not significant",
                marker=dict(size=not_significant_df["bubble_size"]),
                text=not_significant_df["deviation_direction"],
                customdata=not_significant_df[["residual_zscore"]],
                hovertemplate=(
                    "Date: %{x}<br>"
                    "Residual: %{y}<br>"
                    "Residual z-score: %{customdata[0]:.2f}<br>"
                    "Direction: %{text}<extra></extra>"
                )
            )
        )

    if not significant_df.empty:
        fig.add_trace(
            go.Scatter(
                x=significant_df["datum"],
                y=significant_df["residual"],
                mode="markers",
                name="Significant",
                marker=dict(size=significant_df["bubble_size"]),
                text=significant_df["deviation_direction"],
                customdata=significant_df[["residual_zscore"]],
                hovertemplate=(
                    "Date: %{x}<br>"
                    "Residual: %{y}<br>"
                    "Residual z-score: %{customdata[0]:.2f}<br>"
                    "Direction: %{text}<extra></extra>"
                )
            )
        )

    fig.add_hline(y=0, line_dash="dash", line_color="gray")

    fig.update_layout(
        title="Unusual Butter Price Deviations over Time",
        xaxis_title="Date",
        yaxis_title="Residual (actual - predicted)"
    )

    return fig