import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys 


# Crear un programa que realice el analisis de datos a partir de un csv generado
# cuyo path se le pasa como parametro al programa. rutaCsv = './Dev/z_Scrapping/natural-disasters.csv'

rutaCsv = './Dev/z_Scrapping/natural-disasters.csv'

# Lectura del csv general - creacion de dataframe, con pandas
df = pd.read_csv(rutaCsv, sep=',', encoding='utf-8')

# Definir una lista de categorias definidas en el csv
categorias = ['drought', 'earthquakes', 'extreme temperatures', 'floods', 'landslides', 'volcanic activity', 'wildfires','Entity','Year']

# crear ayuda del programa, la misma debe ser dn.py -h
# la ayuda debe mostrar las categorias disponibles para el analisis
# la ayuda debe mostrar el uso del programa dn.py -i <presentacion> -c <categoria> -p <pais> -y <año> -d <decada>
# verificar parametro ingresado -h

#print(sys.argv)


if sys.argv[1] == '-h':
    print('     ')
    print(' *** Este programa muestra el analisis de datos de desastres naturales ***')
    print('     ')
    print(' El uso del programa es:  dn.py -c <categoria> -p <pais> -r <rango> -i <presentacion>')
    print(' donde:')
    print('     ')
    print(' -c <categoria> : 1 = sequia, 2 = terremotos, 3 = temperaturas extremas, 4 = inundaciones, 5 = deslizamientos, 6 = erupciones, 7 = incendios, 8 = storms')
    print(' -p <pais o continente> : cualquier pais del mundo o continente en ingles. Ejemplo: Brazil, Africa, Asia, Europe, North America, South America, Oceania')
    print(' -r <rango> : desde 1900 hasta 2010')
    print(' -i <presentacion> : 1 = grafico, 2 = tabla')
    print('     ')
    print(' Ejemplo de uso: dn.py 4 Argentina 1900-2010 1')
    print('     ')
    sys.exit()

# Asignar valores de argumentos pasados al programa

if sys.argv != 0 : 
  if sys.argv[1] != 'h': categoria = sys.argv[1]
  pais = sys.argv[2]
  rango = sys.argv[3]
  presentacion = sys.argv[4]

# convertir categoria a ingles
if(categoria == '1'): categoria = 'drought'
if(categoria == '2'): categoria = 'earthquakes'
if(categoria == '3'): categoria = 'extreme temperatures'
if(categoria == '4'): categoria = 'floods'
if(categoria == '5'): categoria = 'landslides'
if(categoria == '6'): categoria = 'volcanic activity'
if(categoria == '7'): categoria = 'wildfires'
if(categoria == '8'): categoria = 'storms'



# realizar analisis de datos
tabla_aux = df.filter(like = categoria)
tabla_aux['Pais'] = df['Entity']   # agrega las regiones para procesar

tabla_cat = tabla_aux[[pais]]

print(tabla_cat)

