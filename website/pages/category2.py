from dash import html, dcc


def create_category2_page(section_style, graph_style):
    return html.Div([
        html.H2("Category 2"),
        html.P("Regional Inequality and Public Sentiment"),

        html.H3("Research Question 6"),
        html.P(
            "How does the sentiment and emotional intensity of online discussions "
            "about food price inflation differ between higher-income and lower-income "
            "German federal states between 2020 and 2024?"
        ),
        html.P("Context text ."),
        html.Div(dcc.Graph(id='rq6_graph', figure={}), style=graph_style),
        html.P("Graph explanation .")
    ], style=section_style)