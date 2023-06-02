from dash import Dash, html
from . import bar_chart
from . import dropdown_periodo
from . import cuestionario
from . import visualizaciones
import dash_core_components as dcc
from src.components.visualizaciones import crear_grafica1
from src.components.visualizaciones import crear_grafica2


def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(
                children=app.title,
                style={
                    "textAlign": "center",
                    "fontSize": "98px",
                    "fontFamily": "Arial, sans-serif",
                    "color": "#003893",
                },
            ),
            html.Hr(),
            html.Div(
                className="content-container",
                style={
                    "display": "flex",
                    "justifyContent": "space-between",
                },
                children=[
                    html.Div(
                        className="charts-container",
                        style={"display": "flex"},  # Agregar estilo para que las gráficas se muestren en línea
                        children=[
                            html.Div(
                                className="dropdown-container",
                                style={"margin-right": "50px"},
                                children=[
                                    dropdown_periodo.render(app),
                                ]
                            ),
                            dcc.Graph(
                                id='grafica1',
                                figure=crear_grafica1()
                            ),
                            dcc.Graph(
                                id='grafica2',
                                figure=crear_grafica2()
                            ),
                        ]
                    ),
                    html.Div(
                        className="cuestionario-container",
                        children=[
                            cuestionario.render(app),
                            html.Div(id='resultado-container', style={"textAlign": "center"})
                        ]
                    )
                ]
            ),
        ]
    )
