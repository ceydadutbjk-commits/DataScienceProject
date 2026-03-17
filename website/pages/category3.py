from dash import html, dcc


def create_category3_page(section_style, graph_style):
    return html.Div([
        html.H2("Category 3"),
        html.P("Narratives, Emotion and Economic Stress"),

        html.H3("Research Question 7"),
        html.P(
            "How does the volume of food-inflation-related media coverage "
            "change during periods of lower and higher inflation?"
        ),
        html.P(" This analysis falls under the category of Narratives, Emotion, and Economic Stress and examines how media coverage of food inflation changes at different inflation levels. The research question is whether there is more reporting on food inflation during periods of higher inflation than during periods of lower inflation. This is relevant because rising food prices are directly felt by many households and are often perceived as a burden. The media frequently pick up on such developments, thereby influencing public perception. By comparing inflation data with the number of media articles, the study examines whether higher inflation is associated with more coverage of food inflation."),

        dcc.Dropdown(
            id="rq7_view",
            options=[
                {"label": "Scatter plot", "value": "scatter"},
                {"label": "Time series", "value": "timeseries"}
            ],
            value="scatter",
            clearable=False,
            style={"marginBottom": "15px"}
        ),

        html.Div(dcc.Graph(id="rq7_graph_dynamic"), style=graph_style),

        html.Div(
            id="rq7_interpretation",
            style={"marginTop": "15px"}
        ),

        html.H3("Research Question 8"),
        html.P(
            "Which narratives about food inflation appear most frequently across "
            "news articles, YouTube videos, and YouTube comments?"
        ),
        html.P("Context ."),

        dcc.Dropdown(
            id="rq8_view",
            options=[
                {"label": "Stacked bar chart", "value": "stacked"},
                {"label": "Heatmap", "value": "heatmap"}
            ],
            value="stacked",
            clearable=False,
            style={"marginBottom": "15px"}
        ),

        html.Div(dcc.Graph(id="rq8_graph_dynamic"), style=graph_style),

        html.Div(
            id="rq8_interpretation",
            style={"marginTop": "15px"}
        ),

        html.H3("Research Question 9"),
        html.P(
            "To what extent are increases in food prices associated with economic concerns "
            "expressed in online public discourse in Germany?"
        ),
        html.P(
            "This analysis combines food price indices, Google search interest, and YouTube comments "
            "to examine whether food price spikes are linked to public attention and economic concern."
        ),

        dcc.Dropdown(
            id="rq9_view",
            options=[
                {"label": "Price increases", "value": "price_indices"},
                {"label": "Public attention", "value": "price_vs_search"},
                {"label": "Economic concern", "value": "economic_concern"}
            ],
            value="price_indices",
            clearable=False,
            style={"marginBottom": "15px"}
        ),

        html.Div(dcc.Graph(id="rq9_graph_dynamic"), style=graph_style),

        html.Div(
            id="rq9_interpretation",
            style={"marginTop": "15px"}
        )
    ], style=section_style)