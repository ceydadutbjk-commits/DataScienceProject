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
        html.P("Asymmetric price transmission means that retail prices do not react in the same way when producer prices go up as when they go down. In the German dairy market, this is relevant because raw milk producer prices can be quite volatile, while households mainly notice the price of butter on the shelf. By comparing changes in raw milk producer prices with changes in retail butter prices, we can see how strongly cost shocks are passed on to consumers during phases of food inflation."),

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
        html.P("This question examines how the price relationship between butter and margarine changes during a period of elevated food inflation. The focus is on whether butter becomes relatively more expensive or cheaper than margarine over time and how strongly the prices of these two substitute products diverge or converge."),

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
        html.P("This question investigates abnormal movements of butter price through comparing actual prices against predicted price, for butter produced, based on expected producer price levels and normal seasonal patterns."
                "By observing months in which butter price behaves differently than expected, we can try to determine if these differences represent unusual dynamic conditions in butter market, including delayed price adjustments or temporary inefficiencies of the butter market." 
        
                ),

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
        html.P("This analysis is about the prices that move between the producers and consumers during a certain period with changing economic conditions. "
                "The analysis is about the reduction of VAT in 2020, which was temporary, and the high inflation period in 2021. "
                 "The idea is to see the effect of the retail prices (CPI), when the production prices (PPI) change, whether these changes are passed on the consumers, and the stability in this situation. "
                 ),

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
        html.P(
            "This question seeks to answer how the inflation rates of butter consumer prices (CPI) and dairy producer prices (PPI) change with time." 
            "The aim is to identify instances when consumer prices rise more rapidly than producer prices." 
            "These instances may signify opportunities for potential margin expansion, implying that retailers are raising prices more rapidly than justified by cost changes."
         ),

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