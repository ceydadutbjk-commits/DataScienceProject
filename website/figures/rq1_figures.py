# This module creates the interactive visualizations for Research Question 1.
# It provides two views:
# 1) a scatter plot of monthly producer vs. retail price changes
# 2) a dumbbell plot comparing average butter price reactions

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the prepared dataset for Research Question 1
rq1_df = pd.read_csv("data/rq1_data.csv")
# Convert the month column to datetime format for plotting
rq1_df["month"] = pd.to_datetime(rq1_df["month"])


def create_rq1_figure(view_type="scatter"):
    """
    Create the visualization for Research Question 1.

    Parameters:
        view_type (str): Either "scatter" or "dumbbell".

    Returns:
        plotly.graph_objects.Figure: Interactive Plotly figure.
    """

    if view_type == "dumbbell":
        ppi_increase = rq1_df[rq1_df["ppi_change"] > 0]
        ppi_decrease = rq1_df[rq1_df["ppi_change"] < 0]
        # Calculate the average butter price reaction in both cases
        butter_reaction_increase = ppi_increase["butter_change"].mean()
        butter_reaction_decrease = ppi_decrease["butter_change"].mean()

        fig = go.Figure()
        # Add a connecting line between both average values
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
    # Plot all months with increasing producer prices
    if not increase_df.empty:
        fig.add_trace(
            go.Scatter(
                x=increase_df["ppi_change"],
                y=increase_df["butter_change"],
                mode="markers",
                name="increase"
            )
        )
    # Plot all months with decreasing producer prices
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
    # Add reference lines at zero to divide the plot into quadrants
    fig.add_vline(x=0, line_dash="dash", line_color="gray")
    fig.add_hline(y=0, line_dash="dash", line_color="gray")

    fig.update_layout(height=450)

    return fig

# For RQ1, two different views are used.
# The scatter plot shows the monthly relationship between producer price changes
# and butter price changes.
# The dumbbell plot summarizes this information by comparing the average butter
# price reaction in periods of increasing and decreasing producer prices.