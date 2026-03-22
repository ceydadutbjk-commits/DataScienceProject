from dash import html, dcc


def create_category2_page(section_style, graph_style):
    """
    Create the content for the category 2 page.

    This page contains the content for the category 2 page, which includes the research question 6.

    Parameters
    ----------
    section_style : dict
        The style for the section div.
    graph_style : dict
        The style for the graph div.

    Returns
    -------
    html.Div
        The content for the category 2 page.
    """
    return html.Div([
        html.H2("Category 2"),
        html.P("Regional Inequality and Public Sentiment"),

        html.H3("Research Question 6"),
        html.P(
            "How is media sentiment toward food price inflation reflected in recent news coverage in Germany, and how does it relate to food price developments?"
        ),
        html.P(
            "This study investigates how media sentiment toward food price inflation is reflected in German news coverage and how it relates to actual price developments. By combining consumer price index (CPI) data with sentiment analysis of news articles, the analysis explores how rising food prices are discussed and framed in the public sphere."
                "The CPI data shows that dairy products—especially butter—experienced noticeable price increases during the observed period. The sentiment analysis of news coverage further reveals that reporting on inflation and food prices was, on average, slightly negative, indicating public unease and critical perspectives on rising living costs."
                "Because the datasets cover different time periods, these results should not be viewed as direct causal evidence or month-to-month correlations. Rather, they suggest that both food price inflation and critical media coverage form central parts of the broader societal discourse on economic pressure and affordability in Germany."
        ),

        dcc.Dropdown(
            id="rq6_view",
            options=[
                {"label": "Sentiment distribution", "value": "sentiment"},
                {"label": "Price trends", "value": "prices"}
            ],
            value="sentiment",
            clearable=False,
            style={"marginBottom": "15px"}
        ),

        html.Div(dcc.Graph(id="rq6_graph_dynamic"), style=graph_style),

        html.Div(
            id="rq6_interpretation",
            style={"marginTop": "15px"}
        )
    ], style=section_style)
