import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd


# Browser default for rendering
pio.renderers.default = "browser"


def demo1() -> None:
    # Read vertically
    source = [0, 0]
    target = [1, 2]
    value = [2, 1]

    link = {'source': source, 'target': target, 'value': value}
    sankey = go.Sankey(link=link)
    fig = go.Figure(sankey)
    fig.show()


def demo2() -> None:
    source = [0, 0, 3, 3]
    target = [1, 2, 2, 1]
    value = [1, 2, 3, 4]
    label = ['A', 'B', 'C', 'D']
    link = {'source': source, 'target': target, 'value': value}
    node = {'label': label, 'pad': 15, 'thickness': 35}

    sankey = go.Sankey(link=link, node=node)
    fig = go.Figure(sankey)
    fig.show()


if __name__ == "__main__":
    demo2()
