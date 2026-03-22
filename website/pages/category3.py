from dash import html, dcc


def create_category3_page(section_style, graph_style):
    """
    This function creates a web page for Category 3 containing Research Questions 7, 8, and 9.
    """
    return html.Div([
        html.H2("Category 3"),
        html.P("Narratives, Emotion and Economic Stress"),

        # Research Question 7
        html.H3("Research Question 7"),
        html.P(
            "How does the volume of food-inflation-related media coverage "
            "change during periods of lower and higher inflation?"
        ),
        html.P(
            "This analysis falls under the category of Narratives, Emotion, and Economic Stress and examines how media coverage of food inflation changes at different inflation levels. The research question is whether there is more reporting on food inflation during periods of higher inflation than during periods of lower inflation. This is relevant because rising food prices are directly felt by many households and are often perceived as a burden. The media frequently pick up on such developments, thereby influencing public perception. By comparing inflation data with the number of media articles, the study examines whether higher inflation is associated with more coverage of food inflation."
        ),

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

        # Research Question 8
        html.H3("Research Question 8"),
        html.P(
            "Which narratives about food inflation appear most frequently across "
            "news articles, YouTube videos, and YouTube comments?"
        ),
        html.P(
            "This analysis falls under the category of “Narratives, Emotion, and Economic Stress” and examines which narratives about food inflation appear most frequently across various media. This is relevant because different media report differently: While news outlets tend to provide structured and economic explanations, YouTube-Videos and especially comments more strongly reflect personal opinions and emotions. By comparing the narratives across platforms, the study examines whether perceptions of food inflation differ depending on the medium or whether similar patterns emerge."
        ),

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

        # Research Question 9
        html.H3("Research Question 9"),
        html.P(
            "To what extent are increases in food prices associated with economic concerns "
            "expressed in online public discourse in Germany?"
        ),
        html.P(
            "This study examines how rising food prices in Germany, particularly the increase in butter prices, relate to public attention and expressions of economic concern online. "
            "By combining food price indices, Google search data, and YouTube comments, the analysis explores whether price spikes are mirrored by greater awareness and discussions about financial pressure."
            "Findings indicate that higher butter prices coincide with increased search activity and frequent mentions of terms like “teuer,” “Inflation,” and “Kosten.” "
            "This suggests that food price increases are perceived as part of a broader experience of economic strain."
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
