
#Importar librerías
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#leer el csv
df_terremotos=pd.read_csv(r'C:\Users\Usuario\Desktop\local_repo\2_ISPC\2022_PROYECTO_NOVIEMBRE\dfterremoto.csv',delimiter=',')

#Limpieza de datos
df_terremotos= df_terremotos.drop('Unnamed: 0', axis=1)
#crear columna combinando ciudad y año, para el caso de la ciudad repetida
df_terremotos['Terremoto']=df_terremotos.Ciudad +' ' + (df_terremotos.Año.map(str))
df_terremotos[['Ciudad','Pais']] = df_terremotos.Ciudad.str.split(',',expand=True)
print(df_terremotos)

  
#TOP 5 terremotos por magnitud
print('Terremotos más fuertes de la historia ',df_terremotos[['Terremoto','Magnitud']].groupby('Terremoto').sum().sort_values('Magnitud',ascending=False).head(5))