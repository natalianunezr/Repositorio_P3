import psycopg2
import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

# Establecer la conexión a la base de datos
conn2 = psycopg2.connect(
    host="david.cuz8vbzi7nnr.us-east-1.rds.amazonaws.com",
    database="datos_figura2",
    user="postgres",
    password="proyecto3"
)

# Crear un objeto cursor a partir de la conexión
cursor = conn2.cursor()

# Ejecutar una consulta SQL
query = "SELECT * FROM fig;"
cursor.execute(query)

# Obtener los resultados y cargarlos en un DataFrame
df_count = pd.read_sql(query, conn2)

# Cerrar el cursor y la conexión
cursor.close()
conn2.close()

# Renombrar las columnas del DataFrame
df_count.columns = ['Área de Ubicación', 'Cantidad de Municipios']

# Definir los colores para el gráfico de pastel
colors = ['#99c2ff', '#9fdf9f']  # Azul claro y verde claro

# Crear la figura del gráfico de pastel
fig2 = go.Figure(data=[go.Pie(labels=df_count['Área de Ubicación'], values=df_count['Cantidad de Municipios'], marker=dict(colors=colors))])

# Personalizar el diseño de la figura
fig2.update_layout(
    title="Distribución de municipios por área de ubicación",
    title_x=0.5,
    title_font=dict(size=24),
)

# Crear la aplicación de Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Definir el diseño y los componentes del dashboard
app.layout = html.Div(
    children=[
        html.H1("Distribución de municipios por área de ubicación"),
        dcc.Graph(figure=fig2),
    ]
)

# Ejecutar la aplicación de Dash
if __name__ == "__main__":
    app.run_server(debug=True)
