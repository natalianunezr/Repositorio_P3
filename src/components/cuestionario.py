from dash import html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from . import ids


def render(app):
    return html.Div(
        className="cuestionario-container",
        style={
            'textAlign': 'center',  # Alinear a la izquierda
            'border': '1px solid #ccc',  # Agregar borde
            'padding': '10px',  # Agregar espacio interno
            'fontSize': '28px',  # Aumentar el tamaño de los textos
            'width': 'fit-content'  # Ajustar al contenido
        },

        children=[
            html.H3("Cuestionario", style={'fontSize': '44px'}),  # Aumentar el tamaño del título
            
            #UBICACION DEL COLEGIO
            html.Div([
                html.Label("Seleccione la ubicación del colegio:"),
                dcc.Dropdown(
                    options=[
                        {"label": "RURAL", "value": "RURAL"},
                        {"label": "URBANO", "value": "URBANO"}
                    ],
                    value=None  # Valor inicial seleccionado (puedes establecer el valor predeterminado si deseas)
                )
            ]),

            #TIPO DE JORNADA
            html.Div([
                html.Label("Seleccione el tipo de jornada:"),
                dcc.Dropdown(
                    options=[
                        {"label": "NOCHE", "value": "NOCHE"},
                        {"label": "SABATINA", "value": "SABATINA"},
                        {"label": "MAÑANA", "value": "MAÑANA"},
                        {"label": "TARDE", "value": "TARDE"},
                        {"label": "UNICA", "value": "UNICA"},
                        {"label": "COMPLETA", "value": "COMPLETA"}
                        
                    ],
                    value=None  # Valor inicial seleccionado (puedes establecer el valor predeterminado si deseas)
                )
            ]),

            #DEPARTAMENTO
            html.Div([
                html.Label("Seleccione el departamento:"),
                dcc.Dropdown(
                    options=[
                        {"label": "AMAZONAS", "value": "AMAZONAS"},
                        {"label": "ANTIOQUIA", "value": "ANTIOQUIA"},
                        {"label": "ARAUCA", "value": "ARAUCA"},
                        {"label": "ATLANTICO", "value": "ATLANTICO"},
                        {"label": "BOGOTA", "value": "BOGOTA"},
                        {"label": "BOGOTÁ", "value": "BOGOTÁ"},
                        {"label": "BOLIVAR", "value": "BOLIVAR"},
                        {"label": "BOYACA", "value": "BOYACA"},
                        {"label": "CAQUETA", "value": "CAQUETA"},
                        {"label": "CASANARE", "value": "CASANARE"},
                        {"label": "CAUCA", "value": "CAUCA"},
                        {"label": "CESAR", "value": "CESAR"},
                        {"label": "CHOCO", "value": "CHOCO"},
                        {"label": "CORDOBA", "value": "CORDOBA"},
                        {"label": "CUNDINAMARCA", "value": "CUNDINAMARCA"},
                        {"label": "GUAINIA", "value": "GUAINIA"},
                        {"label": "GUAVIARE", "value": "GUAVIARE"},
                        {"label": "HUILA", "value": "HUILA"},
                        {"label": "LA GUAJIRA", "value": "LA GUAJIRA"},
                        {"label": "MAGDALENA", "value": "MAGDALENA"},
                        {"label": "META", "value": "META"},
                        {"label": "NARIÑO", "value": "NARIÑO"},
                        {"label": "NORTE SANTANDER", "value": "NORTE SANTANDER"},
                        {"label": "PUTUMAYO", "value": "PUTUMAYO"},
                        {"label": "QUINDIO", "value": "QUINDIO"},
                        {"label": "RISARALDA", "value": "RISARALDA"},
                        {"label": "SAN ANDRES", "value": "SAN ANDRES"},
                        {"label": "SANTANDER", "value": "SANTANDER"},
                        {"label": "SUCRE", "value": "SUCRE"},
                        {"label": "TOLIMA", "value": "TOLIMA"},
                        {"label": "VALLE", "value": "VALLE"},
                        {"label": "VAUPES", "value": "VAUPES"},
                        {"label": "VICHADA", "value": "VICHADA"}
                    ],
                    value=None  # Valor inicial seleccionado (puedes establecer el valor predeterminado si deseas)
                )
            ]),

            #MUNICIPIO
            html.Br(),
            html.Div([
                html.Label("Ingrese el municipio en MAYÚSCULAS sin espacios: "),
                dcc.Input(
                    id=ids.INPUT_MUNICIPIO,
                    type="text",
                    placeholder="Escríbalo aquí",
                    value=None
                )
            ]),
            html.Br(),
            
            #BILINGUE
            html.Div([
                html.Label("Seleccione S si el colegio es bilingue, N de lo contrario:"),
                dcc.Dropdown(
                    options=[
                        {"label": "S", "value": "S"},
                        {"label": "N", "value": "N"}
                        
                    ],
                    value=None  # Valor inicial seleccionado (puedes establecer el valor predeterminado si deseas)
                )
            ]),

            #INTERNET
            html.Div([
                html.Label("Seleccione si la familia tiene acceso a Internet"),
                dcc.Dropdown(
                    options=[
                        {"label": "Si", "value": "Si"},
                        {"label": "No", "value": "No"}
                        
                    ],
                    value=None  # Valor inicial seleccionado (puedes establecer el valor predeterminado si deseas)
                )
            ]),

            #ESTRATO
            html.Div([
                html.Label("Seleccione el estrato que corresponda:"),
                dcc.Dropdown(
                    options=[
                        {"label": "Estrato 1", "value": "Estrato 1"},
                        {"label": "Estrato 2", "value": "Estrato 2"},
                        {"label": "Estrato 3", "value": "Estrato 3"},
                        {"label": "Estrato 4", "value": "Estrato 4"},
                        {"label": "Estrato 5", "value": "Estrato 5"},
                        {"label": "Estrato 6", "value": "Estrato 6"},
                        {"label": "Sin Estrato", "value": "Sin Estrato"},
                        {"label": "No Sabe", "value": "No Sabe"}
                        
                    ],
                    value=None  # Valor inicial seleccionado (puedes establecer el valor predeterminado si deseas)
                )
            ]),

            #EDUCACIÓN DEL PADRE
            html.Div([
                html.Label("Seleccione el nivel educativo del padre:"),
                dcc.Dropdown(
                    options=[
                        {"label": "Técnica o tecnológica completa", "value": "Técnica o tecnológica completa"},
                        {"label": "Técnica o tecnológica incompleta", "value": "Técnica o tecnológica incompleta"},
                        {"label": "Primaria completa", "value": "Primaria completa"},
                        {"label": "Primaria incompleta", "value": "Primaria incompleta"},
                        {"label": "Secundaria (Bachillerato) completa", "value": "Secundaria (Bachillerato) completa"},
                        {"label": "Secundaria (Bachillerato) incompleta", "value": "Secundaria (Bachillerato) incompleta"},
                        {"label": "Educación profesional completa", "value": "Educación profesional completa"},
                        {"label": "Educación profesional incompleta", "value": "Educación profesional incompleta"},
                        {"label": "Postgrado", "value": "Postgrado"},
                        {"label": "No Aplica", "value": "No Aplica"},
                        {"label": "No Sabe", "value": "No Sabe"},
                        {"label": "Ninguno", "value": "Ninguno"}
                        
                        
                    ],
                    value=None  # Valor inicial seleccionado (puedes establecer el valor predeterminado si deseas)
                )
            ]),
            
            
            #EDUCACIÓN DE LA MADRE
            html.Div([
                html.Label("Seleccione el nivel educativo del madre:"),
                dcc.Dropdown(
                    options=[
                        {"label": "Técnica o tecnológica completa", "value": "Técnica o tecnológica completa"},
                        {"label": "Técnica o tecnológica incompleta", "value": "Técnica o tecnológica incompleta"},
                        {"label": "Primaria completa", "value": "Primaria completa"},
                        {"label": "Primaria incompleta", "value": "Primaria incompleta"},
                        {"label": "Uno", "value": "Uno"},
                        {"label": "Dos", "value": "Dos"},
                        {"label": "Tres", "value": "Tres"},
                        {"label": "Cuatro", "value": "Cuatro"},
                        {"label": "Cinco", "value": "Cinco"},
                        {"label": "Seis o mas", "value": "Seis o mas"},
                        {"label": "Secundaria (Bachillerato) completa", "value": "Secundaria (Bachillerato) completa"},
                        {"label": "Secundaria (Bachillerato) incompleta", "value": "Secundaria (Bachillerato) incompleta"},
                        {"label": "Educación profesional completa", "value": "Educación profesional completa"},
                        {"label": "Educación profesional incompleta", "value": "Educación profesional incompleta"},
                        {"label": "Postgrado", "value": "Postgrado"},
                        {"label": "No Aplica", "value": "No Aplica"},
                        {"label": "No Sabe", "value": "No Sabe"},
                        {"label": "Ninguno", "value": "Ninguno"}
                        
                        
                    ],
                    value=None  # Valor inicial seleccionado (puedes establecer el valor predeterminado si deseas)
                )
            ]),

        ]
    )

