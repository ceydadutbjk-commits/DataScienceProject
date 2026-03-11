# Hautpdatei der Website 
'''
Simple Dash Dashboard for our DS Project
'''
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

