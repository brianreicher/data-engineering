import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd


# Browser default for rendering
pio.renderers.default = "browser"

# Read vertically
source = [0, 0]
target = [1, 2]
value = [2, 1]

link = {'source': source, 'target': target, 'value': value}
sankey = go.Sankey(link=link)
fig = go.Figure(sankey)
fig.show()
