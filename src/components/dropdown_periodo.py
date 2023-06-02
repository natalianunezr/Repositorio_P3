from dash import Dash, html, dcc
from . import ids
from dash.dependencies import Input, Output
import dash_core_components as dcc

def render(app: Dash) -> html.Div:
    todos_periodos = ["20191", "20194"]

    @app.callback(
        Output(ids.DROPDOWN_PERIODO, "value"),
        Input(ids.SELECT_ALL_PERIODS_BUTTON, "n_clicks"),
    )
    def select_all_periods(_: int) -> list[str]:
        return todos_periodos

    return html.Div(
        style={
            'display': 'inline-block',  # Mostrar como bloque en línea
            'border': '1px solid #E0E0E0',  # Agregar borde
            'borderRadius': '8px',  # Agregar bordes redondeados
            'padding': '20px',  # Agregar espacio interno
            'margin' : '0 auto', #Centrar horizontalmente
            'textAlign': 'center'
        },
        children=[
            html.Div(
                style={
                    'textAlign': 'center',  # Alinear
                    'fontFamily': 'Arial, sans-serif'  # Tipo de fuente amigable
                },
                children=[
                    html.H6(
                        "Seleccione el o los periodos de su interés",
                        style={
                            'fontSize': '38px',  # Disminuir el tamaño de la fuente
                        }
                    ),
                    dcc.Dropdown(
                        id=ids.DROPDOWN_PERIODO,
                        options=[{"label": periodo, "value": periodo} for periodo in todos_periodos],
                        value=todos_periodos,
                        multi=True,
                        style={
                            'textAlign': 'center',  # Alinear al centro
                            'fontSize': '25px',  # Disminuir el tamaño de la fuente
                            'fontFamily': 'Arial, sans-serif',  # Tipo de fuente
                            'borderRadius': '8px',  # Agregar bordes redondeados
                            'padding': '12px 12px',  # Ajustar el espacio interno
                            'backgroundColor': '#F0F0F0',  # Cambiar el color de fondo
                            'width': '400px',  # Ajustar el ancho
                            'margin': '0 auto',
                        }
                    ),
                    html.Button(
                        className="dropdown-button",
                        children=["Seleccionar todo"],
                        id=ids.SELECT_ALL_PERIODS_BUTTON,
                        style={
                            'textAlign': 'center',  # Centrar el texto
                            'fontSize': '20px',  # Disminuir el tamaño de la fuente
                            'fontFamily': 'Arial, sans-serif',  # Tipo de fuente
                            'backgroundColor': '#003893',  # Cambiar el color de fondo
                            'color': 'white',  # Cambiar el color del texto
                            'border': 'none',  # Quitar borde
                            'padding': '6px 12px',  # Ajustar el espacio interno
                            'borderRadius': '8px'  # Agregar bordes redondeados
                        }
                    )
                ]
            )
        ]
    )
