import pandas as pd
import plotly.graph_objects as go


rq5_df = pd.read_csv("data/rq5_data.csv")


rq5_df["date"] = pd.to_datetime(rq5_df["date"])


def create_rq5_figure(view_type="base"):
    """
    Create a visualization for Research Question 5.

    Parameters:
        view_type (str): The type of figure to create. Can be "base" or "highlight".

    Returns:
        fig (go.Figure): The created figure.
    """
    fig = go.Figure()

    # Add the dairy PPI inflation
    fig.add_trace(
        go.Scatter(
            x=rq5_df["date"],
            y=rq5_df["dairy_ppi_yoy_pct"],
            mode="lines",
            name="Dairy PPI inflation"
        )
    )

    # Add the butter CPI inflation
    fig.add_trace(
        go.Scatter(
            x=rq5_df["date"],
            y=rq5_df["butter_yoy_pct"],
            mode="lines",
            name="Butter CPI inflation",
            fill="tonexty"
        )
    )

    # Highlight the potential margin expansions
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

    # Add a horizontal line to indicate the 0% inflation rate
    fig.add_hline(y=0, line_dash="dash", line_color="gray")

    # Update the layout
    fig.update_layout(
        title="Inflation Gap between Butter CPI and Dairy PPI over Time",
        xaxis_title="Date",
        yaxis_title="Year-over-year inflation rate (%)",
        height=500
    )

    return fig
