import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Daten laden
rq1_df = pd.read_csv("data/rq1_data.csv")

# Datumsformat
rq1_df["month"] = pd.to_datetime(rq1_df["month"])


def create_rq1_figure(view_type="scatter"):

    if view_type == "dumbbell":
        ppi_increase = rq1_df[rq1_df["ppi_change"] > 0]
        ppi_decrease = rq1_df[rq1_df["ppi_change"] < 0]

        butter_reaction_increase = ppi_increase["butter_change"].mean()
        butter_reaction_decrease = ppi_decrease["butter_change"].mean()

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=[butter_reaction_increase, butter_reaction_decrease],
                y=[0, 0],
                mode="lines",
                line=dict(color="gray", width=3),
                showlegend=False
            )
        )

        fig.add_trace(
            go.Scatter(
                x=[butter_reaction_increase],
                y=[0],
                mode="markers+text",
                text=[round(butter_reaction_increase, 2)],
                textposition="top center",
                name="Producer price increase"
            )
        )

        fig.add_trace(
            go.Scatter(
                x=[butter_reaction_decrease],
                y=[0],
                mode="markers+text",
                text=[round(butter_reaction_decrease, 2)],
                textposition="top center",
                name="Producer price decrease"
            )
        )

        fig.update_layout(
            title="Average Butter Price Reaction to Producer Price Changes",
            xaxis_title="Average change in butter price",
            yaxis=dict(showticklabels=False),
            height=350
        )

        return fig

    fig = px.scatter(
        rq1_df,
        x="ppi_change",
        y="butter_change",
        color="ppi_direction",
        title="Quadrant View of Price Transmission between Producer and Retail Prices",
        labels={
            "ppi_change": "Change in Dairy Producer Price Index",
            "butter_change": "Change in Butter Consumer Price Index"
        }
    )

    fig.add_vline(x=0, line_dash="dash", line_color="gray")
    fig.add_hline(y=0, line_dash="dash", line_color="gray")

    fig.update_layout(height=450)

    return fig