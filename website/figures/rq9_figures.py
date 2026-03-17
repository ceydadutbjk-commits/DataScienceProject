import pandas as pd
import plotly.express as px

# Daten laden
rq9_df = pd.read_csv("data/rq9_data.csv")


def create_rq9_figure(view_type="price_indices"):
    df = rq9_df.copy()

    if view_type == "price_indices":
        price_df = df[df["type"] == "price_indices"].copy()
        price_df["date"] = pd.to_datetime(price_df["date"])

        price_long = price_df.melt(
            id_vars="date",
            value_vars=["butter_price", "dairy_price", "margarine_price"],
            var_name="product",
            value_name="price_index"
        )

        price_long["product"] = price_long["product"].replace({
            "butter_price": "Butter",
            "dairy_price": "Dairy",
            "margarine_price": "Margarine"
        })

        fig = px.line(
            price_long,
            x="date",
            y="price_index",
            color="product",
            title="Consumer price indices for selected food products in Germany",
            labels={
                "date": "Year",
                "price_index": "Price index",
                "product": "Product"
            }
        )

        fig.update_layout(
            height=450,
            legend_title="Product"
        )

        return fig

    elif view_type == "price_vs_search":
        search_df = df[df["type"] == "price_vs_search"].copy()

        search_df["year_month"] = pd.to_datetime(search_df["year_month"])
        search_df["butter_price"] = pd.to_numeric(search_df["butter_price"], errors="coerce")
        search_df["butter_search_interest"] = pd.to_numeric(search_df["butter_search_interest"], errors="coerce")

        # Normalisieren für bessere Vergleichbarkeit
        search_df["butter_price_norm"] = search_df["butter_price"] / search_df["butter_price"].max()
        search_df["search_interest_norm"] = (
            search_df["butter_search_interest"] / search_df["butter_search_interest"].max()
        )

        plot_df = search_df.melt(
            id_vars="year_month",
            value_vars=["butter_price_norm", "search_interest_norm"],
            var_name="series",
            value_name="normalized_value"
        )

        plot_df["series"] = plot_df["series"].replace({
            "butter_price_norm": "Butter price (normalized)",
            "search_interest_norm": "Google search interest"
        })

        fig = px.line(
            plot_df,
            x="year_month",
            y="normalized_value",
            color="series",
            title="Butter price vs. Google search interest",
            labels={
                "year_month": "Year-Month",
                "normalized_value": "Normalized value",
                "series": "Series"
            }
        )

        fig.update_layout(
            height=450,
            legend_title="Series"
        )

        return fig

    else:
        concern_df = df[df["type"] == "economic_concern"].copy()

        concern_df["fear_score"] = pd.to_numeric(concern_df["fear_score"], errors="coerce")
        concern_df["count"] = pd.to_numeric(concern_df["count"], errors="coerce")

        fig = px.bar(
            concern_df,
            x="fear_score",
            y="count",
            title="Distribution of economic concern in YouTube comments",
            labels={
                "fear_score": "Number of concern-related terms in a comment",
                "count": "Number of comments"
            }
        )

        fig.update_layout(
            height=450
        )

        return fig