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
    plot_df["bubble_size"] = plot_df["residual_zscore"].abs() * 20
    plot_df = plot_df.dropna(subset=["datum", "residual", "residual_zscore", "significant_deviation"])
    plot_df["significant_label"] = plot_df["significant_deviation"].map({
        True: "Significant",
        False: "Not significant"
    })

    fig = px.scatter(
        plot_df,
        x="datum",
        y="residual",
        size="bubble_size",
        color="significant_label",
        hover_data=["residual_zscore", "deviation_direction"],
        title="Unusual Butter Price Deviations over Time",
        labels={
            "datum": "Date",
            "residual": "Residual (actual - predicted)",
            "significant_label": "Significant"
        }
    )

    fig.add_hline(y=0, line_dash="dash", line_color="gray")

    return fig