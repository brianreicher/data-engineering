from dash import Dash, html, dcc, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.H1('Slider Dash'),
    dcc.Slider(0, 10, 1, value=5),
    html.H1('Radio Button'),
    dcc.RadioItems(['New York', 'Montreal', 'San Francisco'], 'San Francisco'),
    html.H1('Dropdown Dash'),
    dcc.Dropdown(['NYC', 'MTL', 'SF'], 'SF', id='demo-dropdown'),
    html.Div(id='dd-output-container')
])


@app.callback(Output('dd-output-container', 'children'), Input('demo-dropdown', 'value'))
def update_output(value):
    return f'You have selected {value}'


if __name__ == '__main__':
    app.run_server(debug=True)
