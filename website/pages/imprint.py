from dash import html


def create_imprint_page(section_style):
    """
    Create the Imprint page of the website.

    Parameters
    ----------
    section_style : dict
        Styling dictionary for the section containing the imprint.

    Returns
    -------
    html.Div
        The Imprint page as a Dash HTML Div object.
    """
    return html.Div([
        html.H2("Imprint"),

        html.P("This website was created as part of the university course:"),
        html.P("Data Science Project (inf-DSProj-01a)"),

        html.Br(),

        html.P("Institution:"),
        html.P("Database Systems and Data Mining"),
        html.P("Christian-Albrechts-Universität zu Kiel"),

        html.Br(),

        html.P("Course Instructors:"),
        html.P("Prof. Dr. Peer Kröger"),
        html.P("Mirjam Bayer, M.Sc."),
        html.P("Dr. Ruekiye Altin"),
        html.P("Dr. Claudius Zelenka"),
        html.P("Sweety Mohanty, M.Sc."),

        html.Br(),

        html.P("Project Team:"),
        html.Ul([
            html.Li("Ceyda Dut – stu247737"),
            html.Li("Ahmad Aldali – stu247158"),
            html.Li("Ali Al Mahmoud – stu246024"),
            html.Li("Rayyan – stu244778"),
        ]),

        html.Br(),

        html.P(
            "This website was developed by students as part of the Data Science Project "
            "course at Kiel University. The purpose of the website is to present and "
            "communicate insights from a data science analysis project."
        ),

        html.Br(),

        html.P("University:"),
        html.P("Christian-Albrechts-Universität zu Kiel"),
        html.P("Christian-Albrechts-Platz 4"),
        html.P("24118 Kiel, Germany"),
    ], style=section_style)
