import plotly.graph_objects as go
import plotly.io as pio


class Sankey:
    def __int__(self, demo_num=2, dataframe='bio.csv'):
        # Browser default for rendering
        pio.renderers.default = "browser"
        self.demo_num = demo_num

    # @staticmethod
    def demo1(self) -> None:
        # Read vertically
        source = [0, 0]
        target = [1, 2]
        value = [2, 1]

        link = {'source': source, 'target': target, 'value': value}
        sankey = go.Sankey(link=link)
        fig = go.Figure(sankey)
        fig.show()

    # @staticmethod
    def demo2(self) -> None:
        source = [0, 0, 3, 3]
        target = [1, 2, 2, 1]
        value = [1, 2, 3, 4]
        label = ['A', 'B', 'C', 'D']
        link = {'source': source, 'target': target, 'value': value}
        node = {'label': label, 'pad': 15, 'thickness': 35}

        sankey = go.Sankey(link=link, node=node)
        fig = go.Figure(sankey)
        fig.show()

    # @staticmethod
    def demo3(self) -> None:
        source = [0, 0, 0, 1, 1, 2, 2, 2]
        target = [3, 4, 5, 3, 5, 3, 4, 5]
        value = [1, 1, 1, 1, 2, 2, 0.5, 1]
        label = ['Stomach', 'Lung', 'Brain', 'Gx', 'Gy', 'Gz']

        link_colors = ['lightgrey'] * 4
        link_colors[1] = '#E18D32'
        link_colors[2] = 'rgb(38,105,149)'
        link = {'source': source, 'target': target, 'value': value, 'color': link_colors}

        node_colors = ['mediumslateblue']*3 + ['palegoldenrod']*3
        node = {'label': label, 'pad': 100, 'thickness': 35, 'line': {'color': 'black',
                                                                      'width': 2},
                                                             'color': node_colors}

        sankey = go.Sankey(link=link, node=node)
        fig = go.Figure(sankey)
        fig.show()

    def run_demo(self):
        if self.demo_num == 1:
            self.demo1()
        elif self.demo_num == 2:
            self.demo2()
        elif self.demo_num == 3:
            self.demo3()
        else:
            raise NotImplementedError("Please enter a valid demo number")


if __name__ == "__main__":
    x = Sankey()
    x.run_demo()
