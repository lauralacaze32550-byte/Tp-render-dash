from dash import html, register_page

register_page(__name__, path='/', name='Home')

layout = html.Div([

    html.P('Bienvenue sur notre site de Fan de canards'),
    html.P("Elle est composé en pages sur les plats autour du canards ainsi que sur les caractéristiques biologique du canard"),
    
    html.H1("Le canard cet animal si commun"),
    html.P("Que ça soit un colver ou un canard de barbarie, les canards nous entourent au quotidien."),

    html.H2("Mais pourtant si bon"),
    html.P("De nombreux plats régionaux sont basés sur les canards. Notamment dans le Gers où le magret de canards, les gesiers ou bien le foie gras est un vrai incontournable."),


])