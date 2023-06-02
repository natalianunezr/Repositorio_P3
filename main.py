from dash import Dash, html
from dash_bootstrap_components.themes import BOOTSTRAP
from src.components.layout import create_layout
import dash_core_components as dcc
import plotly.graph_objects as go
from pgmpy.inference import VariableElimination
from pgmpy.models import BayesianModel
from pgmpy.models import BayesianNetwork
from src.components.cuestionario import render as render_cuestionario
from src.components.dropdown_periodo import render as render_periodo
from pgmpy.estimators import MaximumLikelihoodEstimator, BayesianEstimator
from src.components.ids import DROPDOWN_PERIODO
from src.components.ids import SELECT_ALL_PERIODS_BUTTON
from src.components.ids import INPUT_MUNICIPIO
from dash.dependencies import Input, Output
import dash_core_components as dcc
import pandas as pd

#Importar datos
df = pd.read_csv("datos_p3.csv")

#Discretizamos
#Discretizar cole area ubicacion
df["COLE_AREA_UBICACION_DISCRETO"] = df["COLE_AREA_UBICACION"]
df['COLE_AREA_UBICACION'] = pd.factorize(df['COLE_AREA_UBICACION_DISCRETO'])[0]

#Discretizar cole bilingue
df["COLE_BILINGUE_DISCRETO"] = df["COLE_BILINGUE"]
df['COLE_BILINGUE'] = pd.factorize(df['COLE_BILINGUE_DISCRETO'])[0]

#Discretizar COLE_DEPTO_UBICACION
df["COLE_DEPTO_UBICACION_DISCRETO"] = df["COLE_DEPTO_UBICACION"]
df['COLE_DEPTO_UBICACION'] = pd.factorize(df['COLE_DEPTO_UBICACION_DISCRETO'])[0]

#Discretizar COLE_JORNADA
df["COLE_JORNADA_DISCRETO"] = df["COLE_JORNADA"]
df['COLE_JORNADA'] = pd.factorize(df['COLE_JORNADA_DISCRETO'])[0]

#Discretizar COLE_MCPIO_UBICACION
df["COLE_MCPIO_UBICACION_DISCRETO"] = df["COLE_MCPIO_UBICACION"]
df['COLE_MCPIO_UBICACION'] = pd.factorize(df['COLE_MCPIO_UBICACION_DISCRETO'])[0]

#Discretizar FAMI_EDUCACIONMADRE
df["FAMI_EDUCACIONMADRE_DISCRETO"] = df["FAMI_EDUCACIONMADRE"]
df['FAMI_EDUCACIONMADRE'] = pd.factorize(df['FAMI_EDUCACIONMADRE_DISCRETO'])[0]

#Discretizar FAMI_EDUCACIONPADRE
df["FAMI_EDUCACIONPADRE_DISCRETO"] = df["FAMI_EDUCACIONPADRE"]
df['FAMI_EDUCACIONPADRE'] = pd.factorize(df['FAMI_EDUCACIONPADRE_DISCRETO'])[0]

#Discretizar FAMI_ESTRATOVIVIENDA
df["FAMI_ESTRATOVIVIENDA_DISCRETO"] = df["FAMI_ESTRATOVIVIENDA"]
df['FAMI_ESTRATOVIVIENDA'] = pd.factorize(df['FAMI_ESTRATOVIVIENDA_DISCRETO'])[0]

#Discretizar FAMI_TIENEINTERNET
df["FAMI_TIENEINTERNET_DISCRETO"] = df["FAMI_TIENEINTERNET"]
df['FAMI_TIENEINTERNET'] = pd.factorize(df['FAMI_TIENEINTERNET_DISCRETO'])[0]

#Discretizar puntaje global

df["PUNT_GLOBAL_DISCRETO"] = df["PUNT_GLOBAL"]

df.loc[df["PUNT_GLOBAL_DISCRETO"] < 100, "PUNT_GLOBAL" ] = 1
df.loc[(100 <= df["PUNT_GLOBAL_DISCRETO"]) & (df["PUNT_GLOBAL_DISCRETO"] < 200), "PUNT_GLOBAL" ] = 2
df.loc[(200 <= df["PUNT_GLOBAL_DISCRETO"]) & (df["PUNT_GLOBAL_DISCRETO"] < 300), "PUNT_GLOBAL" ] = 3
df.loc[(300 <= df["PUNT_GLOBAL_DISCRETO"]) & (df["PUNT_GLOBAL_DISCRETO"] < 400), "PUNT_GLOBAL" ] = 4
df.loc[(400 <= df["PUNT_GLOBAL_DISCRETO"]) & (df["PUNT_GLOBAL_DISCRETO"] < 500), "PUNT_GLOBAL" ] = 5
df.PUNT_GLOBAL = df.PUNT_GLOBAL.astype(int)
#No lo toma como numero

#Discretizar periodo
df["PERIODO_DISCRETO"] = df["PERIODO"]

df.loc[(df["PERIODO_DISCRETO"] == 20191), "PERIODO"] = 1
df.loc[(df["PERIODO_DISCRETO"] == 20194), "PERIODO"] = 4
df.PERIODO = df.PERIODO.astype(int)

#Eliminamos columnas sobrantes
df.drop(["PERIODO_DISCRETO", "PUNT_GLOBAL_DISCRETO","COLE_AREA_UBICACION_DISCRETO","COLE_BILINGUE_DISCRETO",
         "COLE_DEPTO_UBICACION_DISCRETO","COLE_JORNADA_DISCRETO","COLE_MCPIO_UBICACION_DISCRETO",
         "FAMI_EDUCACIONMADRE_DISCRETO","FAMI_EDUCACIONPADRE_DISCRETO","FAMI_ESTRATOVIVIENDA_DISCRETO","FAMI_TIENEINTERNET_DISCRETO"], axis=1, inplace=True)


#Creamos modelo
model = BayesianNetwork(
    [ ("FAMI_TIENEINTERNET", "PUNT_GLOBAL"),
     ("COLE_BILINGUE", "PUNT_GLOBAL"),
     ("FAMI_ESTRATOVIVIENDA", "FAMI_TIENEINTERNET"),
     ("PERIODO", "COLE_BILINGUE"),
     ("COLE_JORNADA", "COLE_BILINGUE"),
     ("FAMI_EDUCACIONMADRE", "FAMI_ESTRATOVIVIENDA"),
     ("FAMI_EDUCACIONPADRE", "FAMI_ESTRATOVIVIENDA"),
     ("COLE_MCPIO_UBICACION", "COLE_BILINGUE"),     
     ("COLE_DEPTO_UBICACION", "COLE_MCPIO_UBICACION"),
     ("COLE_AREA_UBICACION", "COLE_DEPTO_UBICACION"),
     ("COLE_AREA_UBICACION", "FAMI_ESTRATOVIVIENDA"),
     ("FAMI_ESTRATOVIVIENDA", "COLE_BILINGUE"),

    ]
)


#PARAMETRIZACION
#MAXIMUM LIKELIHOOD
model.fit(
    data=df,
    estimator=MaximumLikelihoodEstimator
)

def inference(evidence):
    infer=VariableElimination(model)
    prob=infer.query(variables=['PUNT_GLOBAL'], evidence=evidence)
    return prob.values



def main () -> None:

    app = Dash(external_stylesheets= [BOOTSTRAP])
    app.title = "Estado de la educación - Herramienta resultados Saber 11"
    app.layout = create_layout(app)



    app.run()

if __name__ == "__main__":
    main()