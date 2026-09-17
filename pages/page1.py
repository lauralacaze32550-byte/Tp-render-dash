from dash import html, register_page, dcc

register_page(__name__, name="Page 1")

opt = ["Oui", "Non"]

layout = html.Div([
    html.H1("J'aime le canard :"),
    dcc.Dropdown(
        id="dropdown1",
        options=opt,
        value=opt[0]
    ),

    html.H1("J'aime le canard confit :"),
    dcc.Dropdown(
        id="dropdown2",
        options=opt,
        value=opt[0]
    )
])