from dash import html, dcc


def create_category2_page(section_style, graph_style):
    return html.Div([
        html.H2("Category 2"),
        html.P("Regional Inequality and Public Sentiment"),

        html.H3("Research Question 6"),
        html.P(
            "How is media sentiment toward food price inflation reflected in recent news coverage in Germany, and how does it relate to food price developments?"
        ),
        html.P("Context ."),

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