from dash import html


def create_data_page(section_style):
    card_style = {
        "background": "linear-gradient(145deg, #ffffff, #f3f4f6)",
        "padding": "24px",
        "borderRadius": "16px",
        "boxShadow": "0px 6px 20px rgba(0,0,0,0.08)",
        "marginBottom": "24px",
        "border": "1px solid #e5e7eb",
        "transition": "transform 0.2s ease, box-shadow 0.2s ease"
}

    source_grid_style = {
        "display": "grid",
        "gridTemplateColumns": "repeat(auto-fit, minmax(250px, 1fr))",
        "gap": "28px",
        "marginBottom": "20px"
    }

    return html.Div([

        # Intro Card
        html.Div([
            html.H2(
                "Data & Sources",
                style={
                    "marginBottom": "10px",
                    "color": "#111827",
                    "fontWeight": "700",
                    "fontSize": "30px"
                }
            ),
            html.P(
                "Our project integrates multiple data types to examine food inflation in Germany from both an economic and societal perspective. By combining structured economic indicators with unstructured media and online data, we connect price dynamics with public narratives and emotional reactions across digital platforms.",
                style={"fontSize": "16px", "lineHeight": "1.7", "color": "#374151"}
            )
            ], style={**card_style, "borderLeft": "5px solid #6366f1"}),

        # Source Cards
        html.Div([

            html.Div([
                html.H3(
                    "Official Price Indices",
                    style={
                        "marginBottom": "10px",
                        "color": "#1f2937",
                        "fontWeight": "600",
                        "fontSize": "20px"
                    }
                ),
                html.P(
                    "Sources: Eurostat, Destatis",
                    style={"fontWeight": "bold", "marginBottom": "10px", "color": "#1f2937"}
                ),
                html.P(
                    "Provide structured time-series data on Consumer Price Indices (CPI) and Producer Price Indices (PPI). These datasets record price changes for food categories such as butter, margarine, and dairy, forming the economic foundation of our analysis.",
                    style={
                        "fontSize": "15px",
                        "lineHeight": "1.9",
                        "color": "#374151",
                        "fontWeight": "400"
                    }
                )
            ], style={**card_style, "borderLeft": "5px solid #6366f1"}),

            html.Div([
                html.H3(
                    "Media & News Data",
                    style={
                        "marginBottom": "10px",
                        "color": "#1f2937",
                        "fontWeight": "600",
                        "fontSize": "20px"
                    }
                ),
                html.P(
                    "Sources: GDELT, News Archives",
                    style={"fontWeight": "bold", "marginBottom": "10px", "color": "#1f2937"}
                ),
                html.P(
                    "Contain large-scale textual data capturing media coverage of food inflation in Germany and beyond. They allow the analysis of article frequency, geographic focus, and framing patterns in public discourse.",
                    style={"fontSize": "15px", "lineHeight": "1.7", "color": "#374151"}
                )
            ], style={**card_style, "borderLeft": "5px solid #3b82f6"}),

            html.Div([
                html.H3(
                    "Public & Online Data",
                    style={
                        "marginBottom": "10px",
                        "color": "#1f2937",
                        "fontWeight": "600",
                        "fontSize": "20px"
                    }
                ),
                html.P(
                    "Sources: Google Trends, YouTube",
                    style={"fontWeight": "bold", "marginBottom": "10px", "color": "#1f2937"}
                ),
                html.P(
                    "Reflect public awareness and online response through search behavior and user interactions. Google Trends indicates shifts in public attention, while YouTube comments provide insight into sentiment and narrative framing.",
                    style={"fontSize": "15px", "lineHeight": "1.7", "color": "#374151"}
                )
            ], style={**card_style, "borderLeft": "5px solid #6366f1"})

        ], style=source_grid_style),

        # Variables & Preparation Card
        html.Div([
            html.H3(
                "Variables & Preparation",
                style={"marginBottom": "10px", "color": "#1f2937"}
            ),

            html.P(
                "Key Variables",
                style={"fontWeight": "bold", "marginBottom": "10px", "color": "#1f2937"}
            ),

            html.Ul([
                html.Li("Economic: CPI, PPI, inflation gaps, relative price ratios"),
                html.Li("Media & Discourse: article counts, sentiment polarity, narrative categories"),
                html.Li("Public Interest: search volumes, topic-related keyword indicators"),
            ], style={"fontSize": "15px", "lineHeight": "1.8", "color": "#374151"}),

            html.P(
                "Preparation Steps",
                style={
                    "fontWeight": "bold",
                    "marginTop": "15px",
                    "marginBottom": "10px",
                    "color": "#1f2937"
                }
            ),

            html.Ul([
                html.Li("Cleaning and harmonizing data formats"),
                html.Li("Aggregating daily or irregular data to monthly level"),
                html.Li("Filtering datasets for Germany and food-related terms"),
                html.Li("Merging sources via time keys for cross-source exploration"),
                html.Li("Creating derived indicators and applying basic text classification for sentiment and narrative detection"),
            ], style={"fontSize": "15px", "lineHeight": "1.8", "color": "#374151"})

        ], style={**card_style, "borderLeft": "5px solid #6366f1"}),

    ], style=section_style)