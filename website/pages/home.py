from dash import html


def create_home_page(section_style):
    return html.Div([
        html.H2("Home"),
        html.P("Short introduction"),
        html.P("Project relevance")
    ], style=section_style)

    