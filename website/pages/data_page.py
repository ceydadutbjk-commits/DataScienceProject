from dash import html


def create_data_page(section_style):
    return html.Div([
        html.H2("Data & Sources"),
        html.P("Data source description ."),
        html.P("Variable and preparation description .")
    ], style=section_style)