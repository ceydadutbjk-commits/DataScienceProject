'''Hier liegen RQ1 bis RQ5.

Jede Research Question hat:
	•	Überschrift
	•	Fragestellung
	•	Kontexttext
	•	Dropdown
	•	Graph
	•	Interpretation
'''

from dash import html, dcc


def create_category1_page(section_style, graph_style):    return html.Div([
        html.H2("Category 1"),
        html.P("Price Dynamics, Inflation and Retail Behaviour in Germany"),

        html.H3("Research Question 1"),
        html.P(
            "What patterns of asymmetric price transmission can be observed "
            "between rawmilk producer prices and retail butter prices in Germany?"
        ),
        html.P("Context ."),

        dcc.Dropdown(
            id="rq1_view",
            options=[
                {"label": "Quadrant scatter", "value": "scatter"},
                {"label": "Average reaction", "value": "dumbbell"}
            ],
            value="scatter",
            clearable=False,
            style={"marginBottom": "15px"}
        ),
html.Div(dcc.Graph(id="rq1_graph_dynamic"), style=graph_style),

html.Div(
    id="rq1_interpretation",
    style={"marginTop": "15px"}
),

        html.H3("Research Question 2"),
        html.P(
            "How do the relative price dynamics between butter and margarine "
            "evolve during periods of elevated food inflation?"
        ),
        html.P("Context"),

        dcc.Dropdown(
            id="rq2_view",
            options=[
                {"label": "Absolute prices", "value": "prices"},
                {"label": "Price ratio", "value": "ratio"}
            ],
            value="prices",
            clearable=False,
            style={"marginBottom": "15px"}
        ),

        html.Div(dcc.Graph(id="rq2_graph_dynamic"), style=graph_style),
        html.P("Graph"),

        html.Div(
            id="rq2_interpretation",
            style={"marginTop": "15px"}
        ),

        html.H3("Research Question 3"),
        html.P(
            "Which months between 2020 and 2024 exhibit statistically significant "
            "deviations in retail butter prices that cannot be explained by "
            "underlying dairy commodity trends or normal seasonal price patterns?"
        ),
        html.P("Context ."),

        dcc.Dropdown(
            id="rq3_view",
            options=[
                {"label": "Bubble plot", "value": "bubble"},
                {"label": "Heatmap", "value": "heatmap"}
            ],
            value="bubble",
            clearable=False,
            style={"marginBottom": "15px"}
        ),

        html.Div(dcc.Graph(id="rq3_graph_dynamic"), style=graph_style),

        html.Div(
            id="rq3_interpretation",
            style={"marginTop": "15px"}
        ),

        html.H3("Research Question 4"),
        html.P(
            "How did the temporary VAT reduction in Germany (July–December 2020) "
            "affect the price-setting behaviour of retailers, and to what extent "
            "was this effect offset by the inflation surge in 2021?"
        ),
        html.P("Context ."),

        dcc.Dropdown(
            id="rq4_metric",
            options=[
                {"label": "CPI–PPI gap", "value": "index_gap"},
                {"label": "Butter CPI", "value": "butter_cpi"},
                {"label": "Dairy PPI", "value": "dairy_ppi"},
            ],
            value="index_gap",
            clearable=False,
            style={"marginBottom": "15px"}
        ),

        html.Div(dcc.Graph(id="rq4_graph_dynamic"), style=graph_style),

        html.Div(
            id="rq4_interpretation",
            style={"marginTop": "15px"}
        ),

        html.H3("Research Question 5"),
        html.P(
            "To what extent can comparisons between the dairy Producer Price Index "
            "(PPI) and the Consumer Price Index (CPI) reveal periods of excessive "
            "margin expansion, where retail prices increased significantly faster "
            "than production costs?"
        ),
        html.P("Context ."),

        dcc.Dropdown(
            id="rq5_view",
            options=[
                {"label": "Base view", "value": "base"},
                {"label": "Highlight margin expansion", "value": "highlight"}
            ],
            value="base",
            clearable=False,
            style={"marginBottom": "15px"}
        ),

        html.Div(dcc.Graph(id="rq5_graph_dynamic"), style=graph_style),

        html.Div(
            id="rq5_interpretation",
            style={"marginTop": "15px"}
        ),
    ], style=section_style)