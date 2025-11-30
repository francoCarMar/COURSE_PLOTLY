from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Primer Dashboard con Dash")
])

if __name__ == "__main__":
    app.run()