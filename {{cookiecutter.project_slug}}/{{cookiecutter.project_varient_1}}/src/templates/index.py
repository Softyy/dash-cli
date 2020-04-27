import dash_core_components as dcc
import dash_html_components as html

from plotly import graph_objs as go


def render():
    return html.Div(children=[
        html.H1(children='{{cookiecutter.project_slug}}'),

        html.Div(children='Dash: A web application framework for Python.'),

        dcc.Graph(
            id='example-graph',
            figure=go.Figure(
                data=[
                    go.Bar(
                        x=[1, 2, 3],
                        y=[4, 1, 2],
                        name='SF'
                    ),
                    {
                        'x': [1, 2, 3],
                        'y': [2, 4, 5],
                        'type': 'bar',
                        'name': u'Montréal'
                    },
                ],
                layout=go.Layout(
                    title='Dash Data Visualization'
                )
            )
        )
    ])
