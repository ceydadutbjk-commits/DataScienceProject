'''
# Schritt 1: 
# Erstellen eines Simple Dash Dashboard for our DS Project

import dash # Dash Bibliothek in unser Programm holen
from dash import html # HTML Elemente in unser Programm holen

# Erstellen des Dash Dashboards (App/Webiste)
app = dash.Dash(__name__)
server = app.server # damit Render die App im Internet startet

# Erstellen des Layouts
app.layout = html.Div([
    html.H1("Welcome to our Data Science Project Website"), # große Überschrift
    html.P("first simple version of our website.") # normaler Text darunter
])
# Starten der Website
if __name__ == '__main__':
    app.run(debug=True) # lokale Server starten

'''
'''
Sample Dash Dashboard for DS Project
'''

import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

rq1_df = pd.read_csv("data/rq1_data.csv")
rq2_df = pd.read_csv("data/rq2_data.csv")

rq1_df["month"] = pd.to_datetime(rq1_df["month"])
rq2_df["month"] = pd.to_datetime(rq2_df["month"])


app = dash.Dash(__name__) # Dash App erstellen
server = app.server # damit Render die App im Internet startet


 # Style der einzelnen Abschnitte
section_style = { # großen Inhaltsblöcke
    'backgroundColor': '#D1EEEE', # türkis/blau
    'padding': '20px', # Abstand innerhalb der Inhaltsblöcke
    'marginBottom': '30px', # Abstand unterhalb der Inhaltsblöcke
    'borderRadius': '10px', # Rundung der Ecken
    'boxShadow': '0px 2px 6px rgba(0,0,0,0.1)' # Schatten
}

graph_style = {
    'backgroundColor': 'white',
    'padding': '10px',
    'borderRadius': '8px',
    'marginTop': '10px',
    'marginBottom': '10px'
}

menu_style = { # Style der Navigationsleiste
    'textAlign': 'center',
    'marginBottom': '50px',
    'padding': '15px',
    'backgroundColor': '#dfe7f2',
    'borderRadius': '10px'
}

link_style = { # Style der Links in der Navigationsleiste
    'margin': '0 10px', # Abstand zwischen den Links und rechts 
    'textDecoration': 'none', # keine Unterstreichung
    'color': '#1f4e79', # blau
    'fontWeight': 'bold' # fett
}


app.layout = html.Div([ # gesamtes Layout des Dash Dashboards

    dcc.Location(id='url', refresh=False), # URL

    html.H1("From Butter Prices to Public Emotions", style={'textAlign': 'center'}),

    html.P(
    "A Data Science project on food inflation, retail price dynamics, and emotional online reactions in Germany.",
    style={'textAlign': 'center', 'marginBottom': '20px'}
    ),

    html.Div([ # Navigationsleiste
        html.A("Home", href="/", style=link_style),
        html.A("Data & Sources", href="/data", style=link_style),
        html.A("Category 1", href="/category1", style=link_style),
        html.A("Category 2", href="/category2", style=link_style),
        html.A("Category 3", href="/category3", style=link_style),
        html.A("Imprint", href="/imprint", style=link_style)
    ], style=menu_style),

    html.Div(id='page_content') # Inhaltsblöcke

], style={
    'maxWidth': '1100px',
    'margin': '0 auto',
    'padding': '20px',
    'fontFamily': 'Arial, sans-serif',
    'backgroundColor': '#eef2f7'
})


@app.callback( # mehrseitigiger Callback
# Wenn sich etwas ändert, wird automatisch eine Funktion ausgeführt.
    Output('page_content', 'children'), # Das Ergebnis der Funktion wird in den Bereich page_content geschrieben.
    Input('url', 'pathname') # reagieren auf den aktuellen Pfad der URL
)

def display_page(pathname): # Funktion, die die Seite anzeigt

    if pathname == '/':
        return html.Div([
            html.H2("Home"),
            html.P("Short introduction"),
            html.P("Project relevance")
        ], style=section_style)

    elif pathname == '/data':
        return html.Div([
            html.H2("Data & Sources"),
            html.P("Data source description ."),
            html.P("Variable and preparation description .")
        ], style=section_style)

    elif pathname == '/category1':
        return html.Div([
            html.H2("Category 1"),
            html.P("Price Dynamics, Inflation and Retail Behaviour in Germany"),

            html.H3("Research Question 1"),
            html.P("What patterns of asymmetric price transmission can be observed between rawmilk producer prices and retail butter prices in Germany?"),
            html.P("Context text ."),
            html.Div(dcc.Graph(id='rq1_graph', figure={}), style=graph_style),
            html.P("Graph explanation."),

            html.H3("Research Question 2"),
            html.P("How do the relative price dynamics between butter and margarine evolve during periods of elevated food inflation?"),
            html.P("Context text"),
            html.Div(dcc.Graph(id='rq2_graph', figure={}), style=graph_style),
            html.P("Graph explanation"),

            html.H3("Research Question 3"),
            html.P("Which months between 2020 and 2024 exhibit statistically significant deviations in retail butter prices that cannot be explained by underlying dairy commodity trends or normal seasonal price patterns?"),
            html.P("Context text ."),
            html.Div(dcc.Graph(id='rq3_graph', figure={}), style=graph_style),
            html.P("Graph explanation ."),

            html.H3("Research Question 4"),
            html.P("How did the temporary VAT reduction in Germany (July–December 2020) affect the price-setting behaviour of retailers, and to what extent was this eOect oOset by the inflation surge in 2021?"),
            html.P("Context text ."),
            html.Div(dcc.Graph(id='rq4_graph', figure={}), style=graph_style),
            html.P("Graph explanation ."),

            html.H3("Research Question 5"),
            html.P("To what extent can comparisons between the dairy Producer Price Index (PPI) and the Consumer Price Index (CPI) reveal periods of excessive margin expansion, where retail prices increased significantly faster than production costs?"),
            html.P("Context text ."),
            html.Div(dcc.Graph(id='rq5_graph', figure={}), style=graph_style),
            html.P("Graph explanation .")
        ], style=section_style)

    elif pathname == '/category2':
        return html.Div([
            html.H2("Category 2"),
            html.P("Regional Inequality and Public Sentiment"),

            html.H3("Research Question 6"),
            html.P("How does the sentiment and emotional intensity of online discussions about food price inflation diOer between higher-income and lower-income German federal states between 2020 and 2024?"),
            html.P("Context text ."),
            html.Div(dcc.Graph(id='rq6_graph', figure={}), style=graph_style),
            html.P("Graph explanation .")
        ], style=section_style)

    elif pathname == '/category3':
        return html.Div([
            html.H2("Category 3"),
            html.P("Narratives, Emotion and Economic Stress"),

            html.H3("Research Question 7"),
            html.P("How do emotional intensity, persistence and polarization differ between periods dominated by food inflation and those dominated by energy inflation?"),
            html.P("Context text ."),
            html.Div(dcc.Graph(id='rq7_graph', figure={}), style=graph_style),
            html.P("Graph explanation ."),

            html.H3("Research Question 8"),
            html.P("How do specific narrative attributions – such as corporate greed or political failure – amplify emotional intensity during periods of food price inflation, and how do these narratives shape collective perceptions of economic stress?"),
            html.P("Context text ."),
            html.Div(dcc.Graph(id='rq8_graph', figure={}), style=graph_style),
            html.P("Graph explanation ."),

            html.H3("Research Question 9"),
            html.P("How are sudden spikes in grocery prices reflected in expressions of economic fear and perceived loss of control in online discussions?"),
            html.P("Context text ."),
            html.Div(dcc.Graph(id='rq9_graph', figure={}), style=graph_style),
            html.P("Graph explanation .")
        ], style=section_style)

    elif pathname == '/imprint':
        return html.Div([
            html.H2("Imprint"),

            html.P("Kiel University (Christian-Albrechts-Universität zu Kiel)"),
            html.P("Christian-Albrechts-Platz 4"),
            html.P("24118 Kiel, Germany"),

            html.Br(),

            html.P("General Contact:"),
            html.P("Phone: +49 (0431) 880-00"),
            html.P("Email: mail@uni-kiel.de"),
            html.P("Website: www.uni-kiel.de"),

            html.Br(),

            html.P("Legal Representation:"),
            html.P("Kiel University (CAU) is a public law corporation (Körperschaft des öffentlichen Rechts)."),
            html.P("It is legally represented by the Executive Board (Präsidium)."),

            html.Br(),

            html.P("Competent Supervisory Authority:"),
            html.P("Ministry of General and Vocational Education, Science, Research and Culture of the State of Schleswig-Holstein (MBWFK)"),
            html.P("Brunswiker Straße 16-22"),
            html.P("24105 Kiel, Germany"),

            html.Br(),

            html.P("VAT Identification Number:"),
            html.P("Pursuant to Section 27 a of the German Value Added Tax Act: DE 811317279")
        ], style=section_style)

    else:
        return html.Div([
            html.H2("Page not found"),
            html.P("This page does not exist.")
        ], style=section_style)


if __name__ == '__main__': # Wenn du diese Datei direkt startest, soll die App laufen.

    app.run(debug=True) # startet lokale Server