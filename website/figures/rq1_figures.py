import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Daten laden
rq1_df = pd.read_csv("data/rq1_data.csv")

# Datumsformat
rq1_df["month"] = pd.to_datetime(rq1_df["month"])

# Scatterplot udn Dumbbellplot
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

    scatter_df = rq1_df.copy()
    scatter_df = scatter_df.dropna(subset=["ppi_change", "butter_change", "ppi_direction"])
    scatter_df["ppi_direction"] = scatter_df["ppi_direction"].astype(str)

    increase_df = scatter_df[scatter_df["ppi_direction"] == "increase"]
    decrease_df = scatter_df[scatter_df["ppi_direction"] == "decrease"]

    fig = go.Figure()

    if not increase_df.empty:
        fig.add_trace(
            go.Scatter(
                x=increase_df["ppi_change"],
                y=increase_df["butter_change"],
                mode="markers",
                name="increase"
            )
        )

    if not decrease_df.empty:
        fig.add_trace(
            go.Scatter(
                x=decrease_df["ppi_change"],
                y=decrease_df["butter_change"],
                mode="markers",
                name="decrease"
            )
        )

    fig.update_layout(
        title="Quadrant View of Price Transmission between Producer and Retail Prices",
        xaxis_title="Change in Dairy Producer Price Index",
        yaxis_title="Change in Butter Consumer Price Index",
        height=450
    )

    fig.add_vline(x=0, line_dash="dash", line_color="gray")
    fig.add_hline(y=0, line_dash="dash", line_color="gray")

    fig.update_layout(height=450)

    return fig

# Für RQ1 haben wir zwei Sichtweisen genutzt.
# Der Scatter Plot zeigt die monatliche Beziehung zwischen Erzeugerpreisänderung und Butterpreisänderung. 
# Der Dumbbell Plot verdichtet diese Information und zeigt den
# durchschnittlichen Unterschied zwischen Monaten mit steigenden und fallenden Producer Prices.