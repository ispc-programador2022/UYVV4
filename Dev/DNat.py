<<<<<<< HEAD
'''
La consigna consiste en desarrollar una aplicación en Python que: 
1) Tome los datos de alguna página web, haciendo Web Scraping,
2) Guardando los datos recolectados en un archivo csv, 
3) Para luego ser mostrados en una tabla por consola.
4) Por último, con dicha información, realizar un informe sobre el procesamiento de la
misma. 
5) Este informe puede ser simple a través de la comparación entre elementos
recolectados, estadísticos sobre las series de los datos o cualquier tipo de análisis del
tipo Big Data o Machine Learning, como regresiones, proyecciones, etc.

'''
# 1)
# Importamos las librerias necesarias
from turtle import clear
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# 2)
#crear variable con la web
url='https://ourworldindata.org/natural-disasters#data-quality'
#descargar el contenido de la página con requests.get
r=requests.get(url)
#uso beautiful soup. Con el .content ó podría tbn usar .text
soup=BeautifulSoup(r.content,'html.parser')
#encontrar la tabla tipo 'table' class:'' esto lo encuentro al inspeccionar la página web en estudio
#attrs son atributos, bss es el tipo de class que figura al inspeccionar
#se guarda en la variable tabla solo lo contenido en la tabla buscada
tabla=soup.find('table',attrs={'class':'tablepress tablepress-id-100'})
#lista con las filas de la tabla, las filas son tr dentro de html
#la tabla del sitio es la que está debajo del título ¿Cuáles fueron los terremotos más mortíferos del mundo?
rows=soup.find('table',attrs={'class':'tablepress tablepress-id-100'}).find('tbody').find_all('tr')

'''
#imprimo row para ver. Aqui cada elemento corresponde a una fila de la tabla del sitio web
print(rows[0])
print("")

#me trae primer elemento de la lista
rows[0].find_all('td')
print(rows[0].find_all('td'))
print("")

#me trae primer elemento de la lista, su segundo elemento que es el nombre de la ciudad/pais, su texto nomas
rows[0].find_all('td')[1].get_text()
print(rows[0].find_all('td')[1].get_text())
print("")

#imprimo de acuerdo a la tabla de la web en uso, el nombre de la ciudad del terremoto y los num de víctimas
print(rows[0].find_all('td')[1].get_text())
print(rows[0].find_all('td')[2].get_text())
print(rows[0].find_all('td')[3].get_text())
print("")

'''

# 3)
#defino una lista para las ciudades
#con el for recorro la lista rows que es donde están las filas/clumnas de la tabla, en este 
#caso la ubicación 1 traerá cada ciudad

ciudades=[]
magnitud=[]
muertes=[]
fechas=[]
ranking=[]

for row in rows:
	ciudades.append(row.find_all('td')[1].get_text())
	magnitud.append(row.find_all('td')[4].get_text())
	fechas.append(row.find_all('td')[2].get_text())
	muertes.append(row.find_all('td')[3].get_text())
	ranking.append(row.find_all('td')[0].get_text())

#crear un dataframe combinando las listas de datos
#con método index 
df=pd.DataFrame({'Ranking':ranking,'Ciudad':ciudades,'Año':fechas,'Muertes':muertes,
                 'Magnitud':magnitud})
#imprimo el dataframe
print(df)

# Exportar a csv
df.to_csv('DesastresNaturales.csv',index=False)
# imprimir csv
#print(df.to_csv('DesastresNaturales.csv',index=False))
=======


>>>>>>> c85059d5fddfd2f86466e2f987021a190e0e1075
