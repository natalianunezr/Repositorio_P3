import psycopg2
import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

def crear_grafica1():
    # Establecer la conexión a la base de datos
    conn = psycopg2.connect(
        host="david.cuz8vbzi7nnr.us-east-1.rds.amazonaws.com",
        database="datos_figura1",
        user="postgres",
        password="proyecto3"
    )

    # Crear un objeto cursor a partir de la conexión
    cursor = conn.cursor()

    # Ejecutar una consulta SQL
    query = "SELECT * FROM proye;"
    cursor.execute(query)

    # Obtener los resultados y cargarlos en un DataFrame
    df_promedio = pd.read_sql(query, conn)

    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()

    # Definir una paleta de colores personalizada con 34 tonos de verde a azul
    colors = ['#006837', '#057036', '#0B6835', '#116934', '#176834', '#1D6F33', '#237032', '#297632',
              '#2F7531', '#357A30', '#3B7F2F', '#41842F', '#47882E', '#4D8D2D', '#53922D', '#59982C',
              '#5F9D2B', '#65A32B', '#6BA82A', '#71AD29', '#77B229', '#7DB728', '#83BC27', '#89C127',
              '#8FC626', '#95CB25', '#9BD025', '#A1D524', '#A7DA23', '#ADEF23', '#B3F423', '#BAF923',
              '#C0FF22', '#C6FF22', '#CCFF21', '#D2FF20']

    fig = go.Figure()

    # Agregar la barra para los puntajes promedio por departamento
    fig.add_trace(go.Bar(
        x=df_promedio['cole_depto_ubicacion'],
        y=df_promedio['punt_global'],
        marker=dict(color=colors),
        name='Puntaje promedio por departamento'
    ))

    # Calcular el promedio total de todos los departamentos
    promedio_total = round(df_promedio['punt_global'].mean(), 0)

    # Agregar la línea para el promedio total
    fig.add_shape(
        type='line',
        x0=0,
        y0=promedio_total,
        x1=len(df_promedio['cole_depto_ubicacion']) - 1,
        y1=promedio_total,
        line=dict(color='black', dash='dash'),
        name='Promedio total'
    )

    # Agregar la leyenda para el promedio total
    fig.add_annotation(
        xref='paper',
        yref='y',
        x=1,
        y=promedio_total + 230,  # Ajustar el valor de la coordenada y para posicionar más arriba
        text=f'Promedio del país: {promedio_total:.2f}',
        showarrow=False,
        font=dict(color='black', size=14),  # Ajustar el tamaño de fuente deseado
        align='right',
        xanchor='right',
        yanchor='top'
    )

    fig.update_layout(
        title="Puntaje promedio en el ICFES por departamento",
        title_x=0.5,
        title_font=dict(size=24),
        yaxis=dict(range=[0, 500]),
        yaxis_title='Puntaje promedio del ICFES',
        xaxis_title='Departamento'
    )

    fig.update_traces(texttemplate='%{y}', textposition='outside')
    # Ajustar el tamaño de la gráfica
    fig.update_layout(width=1000, height=800)

    return fig

def crear_grafica2():
    
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



    return fig2
