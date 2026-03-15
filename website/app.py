import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# Aufteilen der Seite in verschiedene Komponenten
from components.navbar import create_navbar
from pages.imprint import create_imprint_page
from pages.category1 import create_category1_page
from pages.category2 import create_category2_page 
from pages.category3 import create_category3_page
from pages.home import create_home_page
from pages.data_page import create_data_page
from components.styles import section_style, graph_style, menu_style, link_style
from figures.rq1_figures import create_rq1_figure
from figures.rq2_figures import create_rq2_figure
from figures.rq3_figures import create_rq3_figure
from figures.rq4_figures import create_rq4_figure
from figures.rq5_figures import create_rq5_figure

app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.layout = html.Div([ # gesamtes Layout des Dash Dashboards

    dcc.Location(id='url', refresh=False), # URL verwaltung

    html.H1("From Butter Prices to Public Emotions", style={'textAlign': 'center'}),

    html.P(
    "A Data Science project on food inflation, retail price dynamics, and emotional online reactions in Germany.",
    style={'textAlign': 'center', 'marginBottom': '20px'}
    ),

    create_navbar(link_style, menu_style),

    html.Div(id='page_content') # Inhaltsblöcke

], style={
    'maxWidth': '1100px',
    'margin': '0 auto',
    'padding': '20px',
    'fontFamily': 'Arial, sans-serif',
    'backgroundColor': '#eef2f7'
})


@app.callback( # mehrseitigiger Callback für die Navigation
# Wenn sich etwas ändert, wird automatisch eine Funktion ausgeführt.
# URL wird gelesen, passende Seite wird ausgewählt, Inhalt wird angezeigt
    Output('page_content', 'children'), # Das Ergebnis der Funktion wird in den Bereich page_content geschrieben.
    Input('url', 'pathname') # reagieren auf den aktuellen Pfad der URL
)

def display_page(pathname): # Funktion, die die Seite anzeigt

    if pathname == '/':
        return create_home_page(section_style)

    elif pathname == '/data':
        return create_data_page(section_style)

    elif pathname == '/category1':
        return create_category1_page(
            section_style,
            graph_style
        )

    elif pathname == '/category2':
        return create_category2_page(section_style, graph_style)

    elif pathname == '/category3':
        return create_category3_page(section_style, graph_style)

    elif pathname == '/imprint':
        return create_imprint_page(section_style)

    else:
        return html.Div([
            html.H2("Page not found"),
            html.P("This page does not exist.")
        ], style=section_style)

@app.callback(
    Output("rq2_graph_dynamic", "figure"),
    Output("rq2_interpretation", "children"),
    Input("rq2_view", "value")
)
def update_rq2_graph(selected_view):

    fig = create_rq2_figure(selected_view)

    if selected_view == "prices":

        interpretation = html.P(
            " interpretation"
        )

    else:

        interpretation = html.P(
            "interpretation"
        )

    return fig, interpretation

@app.callback(
    Output("rq1_graph_dynamic", "figure"),
    Output("rq1_interpretation", "children"),
    Input("rq1_view", "value")
)
def update_rq1_graph(selected_view):

    fig = create_rq1_figure(selected_view)

    if selected_view == "scatter":

        interpretation = html.P(
            "interpretation"
        )

    else:

        interpretation = html.P(
            "interpretation"
        )

    return fig, interpretation

@app.callback(
    Output("rq3_graph_dynamic", "figure"),
    Output("rq3_interpretation", "children"),
    Input("rq3_view", "value")
)
def update_rq3_graph(selected_view):

    fig = create_rq3_figure(selected_view)

    if selected_view == "bubble":
        interpretation = html.P(
            "The bubble plot...."
        )
    else:
        interpretation = html.P(
            "The heatmap shows....."
        )

    return fig, interpretation

@app.callback(
    Output("rq4_graph_dynamic", "figure"),
    Output("rq4_interpretation", "children"),
    Input("rq4_metric", "value")
)
def update_rq4_graph(selected_metric):
    fig = create_rq4_figure(selected_metric)

    if selected_metric == "butter_cpi":
        interpretation = html.P(
            "Butter prices dropped marginally while the government lowered value-added tax, yet costs climbed sharply throughout the following year. This indicates the brief tax adjustment barely influenced the market compared to the subsequent spike in consumer prices."
        )
    elif selected_metric == "dairy_ppi":
        interpretation = html.P(
            "Dairy producer prices fluctuated slightly during the VAT period before climbing noticeably throughout 2021. These figures establish the cost basis for analyzing shifts in retail pricing."
        )
    else:
        interpretation = html.P(
            "The gap between consumer and producer prices shrank while the value-added tax decreased. This movement points to businesses passing part of the savings to their customers. In 2021, the difference grew again because rising inflation outweighed the previous tax reduction."
        )

    return fig, interpretation

@app.callback(
    Output("rq5_graph_dynamic", "figure"),
    Output("rq5_interpretation", "children"),
    Input("rq5_view", "value")
)
def update_rq5_graph(selected_view):

    fig = create_rq5_figure(selected_view)

    interpretation = html.P(
        "interpretation"
    )

    return fig, interpretation

if __name__ == '__main__': # Wenn du diese Datei direkt startest, soll die App laufen.

    app.run(debug=True) # startet lokale Server