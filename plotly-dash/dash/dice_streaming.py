# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import random as rnd
from collections import Counter
import pandas as pd


def roll(n):
    return sum([rnd.randint(1,6) for _ in range(n)])


def main():

    latest_rolls = [roll(1) for _ in range(10)]

    # LAYOUT
    app = Dash(__name__)
    app.layout = html.Div([
        html.H1('Roll outcome distribution'),
        dcc.Graph(id='dice'),
        dcc.Interval(id='interval', interval=500, n_intervals=0),
        html.P("# of 6-sided dice"),
        dcc.Slider(id='num_dice', min=1, max=10, step=1, value=2),
        html.P("# rolls"),
        dcc.Slider(id='num_rolls', min=1000, max=10000, step=1000, value=1000)
    ])

    @app.callback(
        Output('dice', 'figure'),
        Input('num_dice', 'value'),
        Input('num_rolls', 'value'),
        Input('interval', 'n_intervals'),
    )
    def update_distribution(num_dice, num_rolls, n_intervals):
        rolls = [roll(num_dice) for _ in range(num_rolls)]
        c = Counter(rolls)
        df = pd.DataFrame({'value':c.keys(), 'freq':c.values()})
        fig = px.bar(df, x="value", y="freq")
        fig.update_layout(yaxis_range=[0,num_rolls/num_dice],
                          xaxis_range=[0,num_dice*6+1])
        return fig

    app.run_server(debug=True)


if __name__ == '__main__':
    main()
