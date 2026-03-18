import pandas as pd
import plotly.express as px

# Daten laden
rq8_df = pd.read_csv("data/rq8_data.csv")


def create_rq8_figure(view_type="stacked"):
    # Lesbarere Plattformnamen
    platform_labels = {
        "news": "News",
        "youtube_videos": "YouTube Videos",
        "youtube_comments": "YouTube Comments"
    }

    df = rq8_df.copy()
    df["platform_label"] = df["platform"].map(platform_labels)

    platform_order = ["News", "YouTube Videos", "YouTube Comments"]
    narrative_order = [
        "corporate_greed",
        "political_failure",
        "monetary_causes",
        "energy_tax_costs",
        "other"
    ]

    # Prozentanteile je Plattform berechnen
    df["platform_total"] = df.groupby("platform")["count"].transform("sum")
    df["percentage"] = (df["count"] / df["platform_total"]) * 100

    if view_type == "heatmap":
        heatmap_df = df.pivot(
            index="platform_label",
            columns="narrative",
            values="percentage"
        )

        heatmap_df = heatmap_df.reindex(
            index=platform_order,
            columns=narrative_order
        )

        fig = px.imshow(
            heatmap_df,
            text_auto=".1f",
            aspect="auto",
            color_continuous_scale="Blues",
            labels={
                "x": "Narrative",
                "y": "Platform",
                "color": "Percentage"
            },
            title="Narrative Intensity across Platforms"
        )

        fig.update_layout(height=450)

        return fig

    fig = px.bar(
        df,
        x="platform_label",
        y="percentage",
        color="narrative",
        category_orders={
            "platform_label": platform_order,
            "narrative": narrative_order
        },
        hover_data=["count", "platform_total"],
        title="Narrative Distribution across Media Platforms"
    )

    fig.update_layout(
        barmode="stack",
        xaxis_title="Platform",
        yaxis_title="Percentage within platform",
        yaxis=dict(range=[0, 100]),
        legend_title="Narrative",
        height=450
    )
    return fig