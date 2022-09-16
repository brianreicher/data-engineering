import plotly.graph_objects as go
import pandas as pd

# Read vertically
source = [0, 0]
target = [1, 2]
value = [2, 1]

link = {'source': source, 'target': target, 'value': value}
sankey = go.Sankey(link=link)
fig = go.Figure(sankey)
fig.show()