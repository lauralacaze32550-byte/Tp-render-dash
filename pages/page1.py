from dash import html, register_page, Dash, html, callback, Input, Output, dcc

register_page(__name__, name='Page 1')

app=Dash(__name__)

opt = ['Oui', 'Non']

app.layout = html.Div([

    html.H1("J'aime le canard :"),
    dcc.Dropdown(id="dropdown", options=opt, value=opt[0]),

    html.H1("J'aime le canard confit :"),
    dcc.Dropdown(id="dropdown", options=opt, value=opt[0])

])

if __name__ == "__main__":
    app.run(debug=True)