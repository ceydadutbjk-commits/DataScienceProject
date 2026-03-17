from dash import html


def create_home_page(section_style, card_style=None):
    if card_style is None:
        card_style = {
            "backgroundColor": "white",
            "padding": "20px",
            "borderRadius": "12px",
            "boxShadow": "0px 2px 8px rgba(0,0,0,0.08)",
            "marginBottom": "20px"
        }

    return html.Div([

        html.Div([
            html.H2(
                "Home",
                style={
                    "marginBottom": "10px",
                    "color": "#111827"
                }
            ),
            html.P(
                "This website presents an interactive Data Science project on food inflation in Germany. Visitors can explore multiple research questions through dynamic visualizations that connect price developments with media discourse, narratives, and public reactions.",
                style={
                    "fontSize": "17px",
                    "lineHeight": "1.6",
                    "color": "#374151"
                }
            )
        ], style=card_style),

        html.Div([
            html.H3(
                "Short Introduction",
                style={
                    "marginBottom": "10px",
                    "color": "#1f2937"
                }
            ),
            html.P(
                "This project investigates the relationship between rising food prices in Germany, public sentiment, and media coverage. It integrates economic indicators with textual data from news articles and online platforms, focusing on price developments for butter, margarine, and other dairy products.",
                style={
                    "fontSize": "16px",
                    "lineHeight": "1.7",
                    "color": "#374151"
                }
            ),
            html.P(
                "The analysis is structured around several research questions that explore how society responds to increasing food costs. Interactive and dynamic visualizations allow users to explore patterns, relationships, and trends across multiple data sources and analytical perspectives.",
                style={
                    "fontSize": "16px",
                    "lineHeight": "1.7",
                    "color": "#374151"
                }
            )
        ], style=card_style),

        html.Div([
            html.H3(
                "Project Relevance",
                style={
                    "marginBottom": "10px",
                    "color": "#1f2937"
                }
            ),
            html.P(
                "Food price inflation is a significant economic and social issue that directly affects household spending and perceptions of economic stability. Beyond measurable price changes, these developments are also reflected in media reporting and public discourse.",
                style={
                    "fontSize": "16px",
                    "lineHeight": "1.7",
                    "color": "#374151"
                }
            ),
            html.P(
                "Analyzing these dimensions together provides a more comprehensive understanding of how economic conditions and societal responses interact. By combining quantitative and qualitative data, the project demonstrates how data-driven approaches can uncover patterns in both price dynamics and collective reactions.",
                style={
                    "fontSize": "16px",
                    "lineHeight": "1.7",
                    "color": "#374151"
                }
            )
        ], style=card_style)

    ], style=section_style)