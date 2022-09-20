'''Description: Ploty & Pandas wrapper for sankey diagrams'''

import pandas as pd
import plotly.graph_objects as go


class Sankey:
    def __init__(self, filepath, src, targ, vals=None):
        self.df = pd.read_csv(filepath)
        self.src = src
        self.targ = targ
        self.vals = vals

    def _code_mapping(self):
        """Maps labels/strings in self.src and self.targ and
        converts them into integers"""

        # Extract distinct labels
        labels = sorted(list(set(list(self.df[self.src]) +
                                 list(self.df[self.targ]))))

        # define integer codes
        codes = list(range(len(labels)))

        # pair labels with list
        lc_map = dict(zip(labels, codes))

        # in df, substitute codes for labels
        self.df = self.df.replace({self.src: lc_map, self.targ: lc_map})
        return labels

    def make_sankey(self, **kwargs):
        labels = self._code_mapping()
        if self.vals is None:
            self.vals = [1] * len(self.df)

        # Process **kwargs
        pad = kwargs.get('pad', 50)  # get - grabs dict value if it exists, otherwise returns defined value
        thickness = kwargs.get('thickness', 30)
        line_color = kwargs.get('line_color', 'black')
        line_width = kwargs.get('line_width', 1)
        
        # Init link & node dicts
        link = {'source': self.df[self.src],
                'target': self.df[self.targ],
                'value': self.df[self.vals]}
        node = {'label': labels, 'pad': pad, 'thickness': thickness, 'line': {'color': line_color, 'width': line_width}}

        sankey: go.Sankey = go.Sankey(link=link, node=node)
        fig: go.Figure = go.Figure(sankey)
        fig.show()

