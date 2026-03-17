# Navigationsleiste der Webseite
from dash import html


def create_navbar(link_style, menu_style):
    return html.Div([
        html.A("Home", href="/", style=link_style),
        html.A("Data & Sources", href="/data", style=link_style),
        html.A("Category 1", href="/category1", style=link_style),
        html.A("Category 2", href="/category2", style=link_style),
        html.A("Category 3", href="/category3", style=link_style),
        html.A("Imprint", href="/imprint", style=link_style)
    ], style=menu_style)