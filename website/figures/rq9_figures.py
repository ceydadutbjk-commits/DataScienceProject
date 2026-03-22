import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

rq9_df = pd.read_csv("data/rq9_data.csv")


def create_rq9_figure(view_type="price_indices"):
    """
    Create an interactive visualization for Research Question 9.

    Parameters:
        view_type (str): The type of figure to create. Can be "price_indices", "price_vs_search", or "economic_concern".

    Returns:
        fig (go.Figure): The created figure.
    """
    df = rq9_df.copy()

    if view_type == "price_indices":
        # Load the price index dataframe
        price_df = df[df["type"] == "price_indices"].copy()

        # Convert the date column to datetime format
        price_df["date"] = pd.to_datetime(price_df["date"])

        # Melt the dataframe to create a long format for plotting
        price_long = price_df.melt(
            id_vars="date",
            value_vars=["butter_price", "dairy_price", "margarine_price"],
            var_name="product",
            value_name="price_index"
        )

        # Replace the product names with more descriptive labels
        price_long["product"] = price_long["product"].replace({
            "butter_price": "Butter",
            "dairy_price": "Dairy",
            "margarine_price": "Margarine"
        })

        # Drop any rows with missing values
        price_long = price_long.dropna(subset=["date", "price_index", "product"])

        # Split the dataframe by product
        butter_df = price_long[price_long["product"] == "Butter"]
        dairy_df = price_long[price_long["product"] == "Dairy"]
        margarine_df = price_long[price_long["product"] == "Margarine"]

        fig = go.Figure()

        # Add the butter price index to the figure
        if not butter_df.empty:
            fig.add_trace(
                go.Scatter(
                    x=butter_df["date"],
                    y=butter_df["price_index"],
                    mode="lines",
                    name="Butter"
                )
            )

        # Add the dairy price index to the figure
        if not dairy_df.empty:
            fig.add_trace(
                go.Scatter(
                    x=dairy_df["date"],
                    y=dairy_df["price_index"],
                    mode="lines",
                    name="Dairy"
                )
            )

        # Add the margarine price index to the figure
        if not margarine_df.empty:
            fig.add_trace(
                go.Scatter(
                    x=margarine_df["date"],
                    y=margarine_df["price_index"],
                    mode="lines",
                    name="Margarine"
                )
            )

        # Update the figure layout
        fig.update_layout(
            title="Consumer price indices for selected food products in Germany",
            xaxis_title="Year",
            yaxis_title="Price index",
            height=450,
            legend_title="Product"
        )

        return fig

    elif view_type == "price_vs_search":
        # Load the price vs. search dataframe
        search_df = df[df["type"] == "price_vs_search"].copy()

        # Convert the year_month column to datetime format
        search_df["year_month"] = pd.to_datetime(search_df["year_month"])

        # Convert the butter price and search interest columns to numeric values
        search_df["butter_price"] = pd.to_numeric(search_df["butter_price"], errors="coerce")
        search_df["butter_search_interest"] = pd.to_numeric(search_df["butter_search_interest"], errors="coerce")

        # Normalize the butter price and search interest values
        search_df["butter_price_norm"] = search_df["butter_price"] / search_df["butter_price"].max()
        search_df["search_interest_norm"] = (
            search_df["butter_search_interest"] / search_df["butter_search_interest"].max()
        )

        # Melt the dataframe to create a long format for plotting
        plot_df = search_df.melt(
            id_vars="year_month",
            value_vars=["butter_price_norm", "search_interest_norm"],
            var_name="series",
            value_name="normalized_value"
        )

        # Replace the series names with more descriptive labels
        plot_df["series"] = plot_df["series"].replace({
            "butter_price_norm": "Butter price (normalized)",
            "search_interest_norm": "Google search interest"
        })

        # Drop any rows with missing values
        plot_df = plot_df.dropna(subset=["year_month", "normalized_value", "series"])

        # Split the dataframe by series
        price_series_df = plot_df[plot_df["series"] == "Butter price (normalized)"]
        search_series_df = plot_df[plot_df["series"] == "Google search interest"]

        fig = go.Figure()

        # Add the butter price series to the figure
        if not price_series_df.empty:
            fig.add_trace(
                go.Scatter(
                    x=price_series_df["year_month"],
                    y=price_series_df["normalized_value"],
                    mode="lines",
                    name="Butter price (normalized)"
                )
            )

        # Add the search interest series to the figure
        if not search_series_df.empty:
            fig.add_trace(
                go.Scatter(
                    x=search_series_df["year_month"],
                    y=search_series_df["normalized_value"],
                    mode="lines",
                    name="Google search interest"
                )
            )

        # Update the figure layout
        fig.update_layout(
            title="Butter price vs. Google search interest",
            xaxis_title="Year-Month",
            yaxis_title="Normalized value",
            height=450,
            legend_title="Series"
        )

        return fig

    else:
        # Load the economic concern dataframe
        concern_df = df[df["type"] == "economic_concern"].copy()

        # Convert the fear score and count columns to numeric values
        concern_df["fear_score"] = pd.to_numeric(concern_df["fear_score"], errors="coerce")
        concern_df["count"] = pd.to_numeric(concern_df["count"], errors="coerce")

        # Create a bar chart of the economic concern distribution
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

        # Update the figure layout
        fig.update_layout(
            height=450
        )

        return fig
