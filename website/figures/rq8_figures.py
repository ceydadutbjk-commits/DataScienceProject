import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

rq8_df = pd.read_csv("data/rq8_data.csv")


def create_rq8_figure(view_type="stacked"):
    """
    Create an interactive visualization for Research Question 8.

    Parameters:
        view_type (str): The type of figure to create. Can be "stacked" or "heatmap".

    Returns:
        fig (go.Figure): The created figure.
    """
    # Define a consistent order for platforms and narrative categories
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

    # Calculate the total number of texts per platform
    df["platform_total"] = df.groupby("platform")["count"].transform("sum")

    # Calculate the percentage share of each narrative within each platform
    df["percentage"] = (df["count"] / df["platform_total"]) * 100

    if view_type == "heatmap":
        # Create a matrix of percentage values for the heatmap
        heatmap_df = df.pivot(
            index="platform_label",
            columns="narrative",
            values="percentage"
        )

        # Reorder rows and columns so the heatmap follows a consistent structure
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
            title="Narrative Intensity across platforms"
        )

        # Customize the heatmap's layout
        fig.update_layout(height=450)

        return fig

    fig = go.Figure()

    # Iterate over all narratives and create a bar segment for each
    for narrative in narrative_order:
        narrative_df = df[df["narrative"] == narrative]

        if not narrative_df.empty:
            fig.add_trace(
                go.Bar(
                    x=narrative_df["platform_label"],
                    y=narrative_df["percentage"],
                    name=narrative,
                    customdata=narrative_df[["count", "platform_total"]],
                    hovertemplate=(
                        "Platform: %{x}<br>"
                        "Percentage: %{y:.1f}%<br>"
                        "Count: %{customdata[0]}<br>"
                        "Platform total: %{customdata[1]}<extra></extra>"
                    )
                )
            )

    # Customize the stacked bar chart's layout
    fig.update_layout(
        title="Narrative Distribution across Media platforms",
        barmode="stack",
        xaxis_title="Platform",
        yaxis_title="Percentage within platform",
        yaxis=dict(range=[0, 100]),
        legend_title="Narrative",
        height=450
    )

    return fig
