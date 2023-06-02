from dash import Dash, dcc, html
import plotly.express as px
from dash.dependencies import Input, Output
from . import ids

ICFES_DATA = px.data.medals_long()

def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.BAR_CHART, "children"),
        Input(ids.DROPDOWN_PERIODO, "value")
    )
    def update_bar_chart(periodos: list[str]) -> html.Div:
        filtered_data = ICFES_DATA.query("periodo en @periodos")

        fig = px.bar(filtered_data, x =  "COLE_DEPTO_UBICACION", y = "PUNT_GLOBAL", color = "periodo", text = "periodo")
        return html.Div(dcc.Graph(figure = fig), id = ids.BAR_CHART)
    return html.Div(id=ids.BAR_CHART)