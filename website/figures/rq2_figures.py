import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


rq2_df = pd.read_csv("data/rq2_data.csv")


rq2_df["month"] = pd.to_datetime(rq2_df["month"])


rq2_df["price_ratio"] = rq2_df["butter_cpi"] / rq2_df["margarine_cpi"]


def create_rq2_figure(view_type="prices"):
    """
    Create a Plotly figure based on the Research Question 2 data.

    Parameters:
    view_type (str): The type of figure to create. Can be "ratio" or "prices".

    Returns:
    fig (go.Figure): The created figure.

    """

    # Ratio view: shows how butter prices evolve relative to margarine prices
    if view_type == "ratio":
        fig = px.line(
            rq2_df,
            x="month",
            y="price_ratio",
            title="Relative Price Ratio: Butter vs Margarine"
        )

        fig.add_hline(
            y=1,
            line_dash="dash",
            line_color="gray"
        )

        fig.update_layout(
            xaxis_title="Month",
            yaxis_title="Price Ratio (Butter / Margarine)"
        )

        return fig

    # Default view: compares the absolute CPI development of butter and margarine.
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=rq2_df["month"],
            y=rq2_df["butter_cpi"],
            mode="lines",
            name="Butter CPI",
            fill="tozeroy"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=rq2_df["month"],
            y=rq2_df["margarine_cpi"],
            mode="lines",
            name="Margarine CPI",
            fill="tozeroy"
        )
    )

    fig.update_layout(
        title="Butter and Margarine Price Dynamics during Food Inflation",
        xaxis_title="Month",
        yaxis_title="Price Index (2015 = 100)"
    )

    return fig

