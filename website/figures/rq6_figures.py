import pandas as pd
import plotly.express as px


# Daten laden
rq6_df = pd.read_csv("data/rq6_data.csv")

# Datumsformat
rq6_df["date"] = pd.to_datetime(rq6_df["date"], errors="coerce")


def create_rq6_figure(view_type="sentiment"):

    if view_type == "prices":
        price_df = rq6_df[rq6_df["type"] == "prices"].copy()

        fig = px.line(
            price_df,
            x="date",
            y=["dairy_cpi", "butter_cpi"],
            title="Food Price Trends in Germany (Dairy & Butter CPI)",
            labels={
                "date": "Date",
                "value": "Price index",
                "variable": "Series"
            }
        )

        fig.update_layout(height=450)

        return fig

    sentiment_df = rq6_df[rq6_df["type"] == "sentiment"].copy()

    fig = px.histogram(
        sentiment_df,
        x="sentiment",
        nbins=15,
        title="Distribution of Media Sentiment (Food Inflation News)",
        labels={
            "sentiment": "Sentiment score",
            "count": "Number of articles"
        }
    )

    fig.update_layout(height=450)

    return fig