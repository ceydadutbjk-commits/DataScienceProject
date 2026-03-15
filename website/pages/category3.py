from dash import html, dcc


def create_category3_page(section_style, graph_style):
    return html.Div([
        html.H2("Category 3"),
        html.P("Narratives, Emotion and Economic Stress"),

        html.H3("Research Question 7"),
        html.P(
            "How do emotional intensity, persistence and polarization differ "
            "between periods dominated by food inflation and those dominated by energy inflation?"
        ),
        html.P("Context text ."),
        html.Div(dcc.Graph(id='rq7_graph', figure={}), style=graph_style),
        html.P("Graph explanation ."),

        html.H3("Research Question 8"),
        html.P(
            "How do specific narrative attributions – such as corporate greed or political failure – "
            "amplify emotional intensity during periods of food price inflation, and how do these "
            "narratives shape collective perceptions of economic stress?"
        ),
        html.P("Context text ."),
        html.Div(dcc.Graph(id='rq8_graph', figure={}), style=graph_style),
        html.P("Graph explanation ."),

        html.H3("Research Question 9"),
        html.P(
            "How are sudden spikes in grocery prices reflected in expressions of economic fear "
            "and perceived loss of control in online discussions?"
        ),
        html.P("Context text ."),
        html.Div(dcc.Graph(id='rq9_graph', figure={}), style=graph_style),
        html.P("Graph explanation .")
    ], style=section_style)