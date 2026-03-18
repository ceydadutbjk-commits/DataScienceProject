# Hauptprogramm, Stelle an der alle Einzelteile der Seite zusammengefasst werden


import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output # wird benutzt, um die Seite zu aktualisieren Callback

# Aufteilen der Seite in verschiedene Komponenten
# importieren der Komponenten

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
from figures.rq7_figures import create_rq7_figure
from figures.rq8_figures import create_rq8_figure
from figures.rq6_figures import create_rq6_figure
from figures.rq9_figures import create_rq9_figure

app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server 
app.layout = html.Div([ # gesamtes Layout des Dash Dashboards

    dcc.Location(id='url', refresh=False), # URL verwaltung

    html.Div([
    html.H1(
        "From Butter Prices to Public Emotions",
        style={
            "textAlign": "center",
            "fontSize": "48px",
            "fontWeight": "700",
            "marginBottom": "10px",
            "color": "#111827"
        }
    ),

    html.P(
        "Interactive insights into food inflation, public perception, and media discourse in Germany.",
        style={
            "textAlign": "center",
            "fontSize": "18px",
            "color": "#374151",
            "marginBottom": "25px"
        }
    )
], style={
    "padding": "30px 20px 10px 20px"
}),

    create_navbar(link_style, menu_style),

    html.Div(id='page_content') # Inhaltsblöcke

], style={
    'maxWidth': '1100px',
    'margin': '0 auto',
    'padding': '20px',
    'fontFamily': 'Arial, sans-serif',
    'background': 'linear-gradient(to bottom, #eef2f7, #e5e7eb)'
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

# jede research question hat einen eigenen callback
# wird aufgerufen, wenn sich etwas im dropdown ändert
# jede rsq hat einen eigenen dropdown, figure und interpretation

@app.callback(
    Output("rq2_graph_dynamic", "figure"),
    Output("rq2_interpretation", "children"),
    Input("rq2_view", "value")
)
def update_rq2_graph(selected_view):

    fig = create_rq2_figure(selected_view)

    if selected_view == "prices":

        interpretation = html.P(
            " In the absolute price chart, the y‑axis shows the price ratio of butter to margarine, while the x‑axis displays the months from early 2020 to late 2023. The ratio starts clearly above the reference value of 1, which suggests that butter is consistently priced higher than margarine at the beginning of the period. Over the course of 2022, the line rises noticeably and reaches a pronounced peak, indicating a phase in which butter prices increase more than margarine prices. From early 2023 onward, the ratio drops sharply below the reference line and remains there for several months, so margarine appears temporarily more expensive than butter, before the ratio moves slightly back toward 1 near the end of the observed period."
        )

    else:

        interpretation = html.P(
            "In the price rario chart, the y‑axis reports price indices for butter and margarine (base year 2015 = 100), and the x‑axis again covers the months from 2020 to 2023. Both index series trend upward over time, indicating an overall rise in prices for both products. The blue area for butter lies above the red area for margarine for a long stretch and shows a particularly strong increase from 2021 to the end of 2022, which suggests comparatively stronger price growth for butter in that phase. From early 2023, the butter index moves closer to the margarine index and even falls below it at times, indicating that the relative price dynamics between the two products reverse or become more aligned in this later period."
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
            "The quadrant scatter shows monthly changes in raw milk producer prices on the x-axis and monthly changes in the butter consumer price index on the y-axis. Many points are located to the right of zero and often above zero, which means that rising producer prices frequently coincide with rising butter prices. On the left side, there are also months where both producer and butter prices fall, but this pattern is less clustered and more scattered. In some months, butter prices move more strongly than producer prices, suggesting that the reaction is not perfectly proportional. Overall, the plot indicates a positive link between producer and retail prices, with some signs of asymmetry, but it should be read as a pattern rather than a final statistical proof."
        )

    else:

        interpretation = html.P(
            "The average reaction plot summarizes how butter prices behave in months with producer price increases compared to months with producer price decreases. In the data shown, producer price increases are associated with an average butter price change of around +2.63 index points, while producer price decreases go along with an average change of about −3.71 index points. This means that butter prices respond in both directions and, in this sample, fall on average even more strongly when producer prices decrease than they rise when producer prices increase. The result therefore does not fit the simple story that “prices rise faster than they fall”, but instead points to a noticeable, two-sided pass-through of producer price movements to retail butter prices."
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

# dynamisches beispiel
# Hier wird nicht zwischen zwei Plottypen gewechselt, sondern zwischen drei Metriken:
# index_gap
# butter_cpi
# dairy_ppi

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

@app.callback(
    Output("rq7_graph_dynamic", "figure"),
    Output("rq7_interpretation", "children"),
    Input("rq7_view", "value")
)
def update_rq7_graph(selected_view):

    fig = create_rq7_figure(selected_view)

    if selected_view == "scatter":

        interpretation = html.P(
            "The scatter plot shows the relationship between the inflation rate on the x-axis and the number of media articles per month on the y-axis. "
            "Points with higher inflation tend to be associated with higher article counts, suggesting that periods of stronger inflation are often accompanied by greater media attention. "
            "At lower inflation levels, the number of articles varies more strongly and is in several cases clearly lower. "
            "Although the pattern is not perfectly linear, the chart overall indicates a positive relationship between inflation and media coverage."
        )

    else:

        interpretation = html.P(
            "The time series compares the development of inflation and media coverage over time. "
            "Both series follow similar broader movements, which suggests a connection between higher inflation and increased reporting. "
            "At the same time, the graph shows that media attention does not always react immediately: in some months, article counts continue to rise even when inflation declines. "
            "This indicates that the relationship is positive overall, but not equally strong or synchronous in every month."
        )

    return fig, interpretation

@app.callback(
    Output("rq8_graph_dynamic", "figure"),
    Output("rq8_interpretation", "children"),
    Input("rq8_view", "value")
)
def update_rq8_graph(selected_view):

    fig = create_rq8_figure(selected_view)

    if selected_view == "stacked":

        interpretation = html.P(
           "The stacked bar chart shows how different narratives about food inflation are distributed across news articles, YouTube videos, and YouTube comments."
           "In the news, “monetary causes” clearly dominate, suggesting that traditional media primarily attribute inflation to economic factors. By comparison, other narratives play a significantly smaller role. "
           "In YouTube videos, the distribution is more balanced, as several narratives each account for a relevant share. This shows that different explanatory approaches coexist there, rather than a single dominant narrative taking center stage."
           "In YouTube comments, “other” dominates by a wide margin. This suggests that users more frequently use nonspecific or emotional explanations rather than referring to clear economic causes."
           "Overall, the diagram shows that the narratives differ significantly depending on the platform, with a shift from structured, economic explanations in the news to more diverse and less clear interpretations on social media. "

        )

    else:

        interpretation = html.P(
            "The heatmap shows the prevalence of different narratives about food inflation across news articles, YouTube videos, and YouTube comments, with darker colors representing higher proportions. "
            "In the news, “monetary causes” clearly dominates, suggesting that traditional media primarily attribute inflation to economic factors such as monetary policy. Other narratives appear significantly less frequently. "
            "In YouTube videos, the distribution is more balanced, as several narratives such as monetary causes, other, and energy/tax costs appear with similar frequency. This shows that multiple explanations are used simultaneously there."
            "In YouTube comments, “other” dominates by a wide margin. This suggests that comments are less structured and more heavily influenced by subjective or emotional assessments. "
            "Overall, the heatmap shows a clear shift from structured economic explanations in the news toward more diverse and less clear interpretations on social media. "
        )

    return fig, interpretation

@app.callback(
    Output("rq6_graph_dynamic", "figure"),
    Output("rq6_interpretation", "children"),
    Input("rq6_view", "value")
)
def update_rq6_graph(selected_view):

    fig = create_rq6_figure(selected_view)

    if selected_view == "prices":
        interpretation = html.P(
            "The price trend view shows the development of dairy and butter prices over time. Butter prices rise more strongly, which illustrates the broader food inflation context."
        )
    else:
        interpretation = html.P(
            "The sentiment distribution shows that recent news coverage on food inflation is predominantly negative, indicating a critical media tone."
        )

    return fig, interpretation

@app.callback(
    Output("rq9_graph_dynamic", "figure"),
    Output("rq9_interpretation", "children"),
    Input("rq9_view", "value")
)
def update_rq9_graph(selected_view):

    fig = create_rq9_figure(selected_view)

    if selected_view == "price_indices":
        interpretation = html.P(
            "The chart shows the development of consumer price indices for butter, dairy products, and margarine in Germany. "
            "All three series increase over time, with particularly strong price growth during the later inflation period. "
            "This provides the basis for identifying food price spikes and comparing them with public reactions."
        )

    elif selected_view == "price_vs_search":
        interpretation = html.P(
            "This visualization compares normalized butter prices with Google search interest. "
            "Periods of rising butter prices tend to coincide with higher search activity, suggesting that food price increases "
            "are associated with stronger public attention and information-seeking behavior."
        )

    else:
        interpretation = html.P(
            "The distribution of fear scores shows that a notable share of YouTube comments contains at least one term related "
            "to economic concern. This suggests that online discussions about food inflation are often linked to affordability, "
            "financial pressure, and broader economic stress."
        )

    return fig, interpretation

if __name__ == '__main__': # Wenn du diese Datei direkt startest, soll die App laufen.

    app.run(debug=True) # startet lokale Server