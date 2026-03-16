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
        html.P("Context ."),

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
            "How are sudden spikes in grocery prices reflected in expressions of economic fear "
            "and perceived loss of control in online discussions?"
        ),
        html.P("Context text ."),
        html.Div(dcc.Graph(id='rq9_graph', figure={}), style=graph_style),
        html.P("Graph explanation .")
    ], style=section_style)