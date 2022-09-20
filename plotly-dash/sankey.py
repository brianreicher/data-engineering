import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default = "browser"


class Sankey:
    def __init__(self, demo_num=3):
        # Browser default for rendering
        self.demo_num = demo_num

    @staticmethod
    def demo1() -> None:
        # Read vertically
        source: list[int] = [0, 0]
        target: list[int] = [1, 2]
        value: list[int] = [2, 1]

        link = {'source': source, 'target': target, 'value': value}
        sankey = go.Sankey(link=link)
        fig = go.Figure(sankey)
        fig.show()

    @staticmethod
    def demo2() -> None:
        source: list[int] = [0, 0, 3, 3]
        target: list[int] = [1, 2, 2, 1]
        value: list[int] = [1, 2, 3, 4]
        label: list[str] = ['A', 'B', 'C', 'D']
        link: dict[str, list[int]] = {'source': source, 'target': target, 'value': value}
        node = {'label': label, 'pad': 15, 'thickness': 35}

        sankey: go.Sankey = go.Sankey(link=link, node=node)
        fig: go.Figure = go.Figure(sankey)
        fig.show()

    @staticmethod
    def demo3() -> None:
        source: list[int] = [0, 0, 0, 1, 1, 2, 2, 2]
        target: list[int] = [3, 4, 5, 3, 5, 3, 4, 5]
        value = [1, 1, 1, 1, 2, 2, 0.5, 1]
        label: list[str] = ['Stomach', 'Lung', 'Brain', 'Gx', 'Gy', 'Gz']

        link_colors: list[str] = ['lightgrey'] * 4
        link_colors[1] = '#E18D32'
        link_colors[2] = 'rgb(38,105,149)'
        link = {'source': source, 'target': target, 'value': value, 'color': link_colors}

        node_colors: list[str] = ['mediumslateblue']*3 + ['palegoldenrod']*3
        node = {'label': label, 'pad': 100, 'thickness': 35, 'line': {'color': 'black',
                                                                      'width': 2},
                                                             'color': node_colors}

        sankey: go.Sankey = go.Sankey(link=link, node=node)
        fig: go.Figure = go.Figure(sankey)
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
        self.demo3()


if __name__ == "__main__":
    sankey_demo = Sankey()
    sankey_demo.run_demo()
