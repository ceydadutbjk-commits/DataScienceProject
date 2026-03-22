import pandas as pd
import plotly.express as px



rq6_df = pd.read_csv("data/rq6_data.csv")


rq6_df["date"] = pd.to_datetime(rq6_df["date"], errors="coerce")


def create_rq6_figure(view_type="sentiment"):
    """
    Creates an interactive visualization for Research Question 6.
    
    Parameters:
        view_type (str): The type of figure to create. Can be "prices" or "sentiment".
    
    Returns:
        fig (go.Figure): Interactive Plotly figure.
    """

    if view_type == "prices":
        # Load the prices dataframe
        price_df = rq6_df[rq6_df["type"] == "prices"].copy()

        # Create a line plot of the dairy and butter CPIs
        fig = px.line(
            price_df,
            x="date",
            y=["dairy_cpi", "butter_cpi"],
            title="Food Price trends in Germany (Dairy & Butter CPI)",
            labels={
                "date": "Date",
                "value": "Price index",
                "variable": "Series"
            }
        )

        # Adjust the figure height
        fig.update_layout(height=450)

        return fig

    # Load the sentiment dataframe
    sentiment_df = rq6_df[rq6_df["type"] == "sentiment"].copy()

    # Create a histogram of the sentiment scores
    fig = px.histogram(
        sentiment_df,
        x="sentiment",
        nbins=15,
        title="Distribution of media sentiment (food inflation news)",
        labels={
            "sentiment": "Sentiment score",
            "count": "Number of articles"
        }
    )

    # Adjust the figure height
    fig.update_layout(height=450)

    return fig
