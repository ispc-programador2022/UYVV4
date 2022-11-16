import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys 



# Crear un programa que realice el analisis de datos a partir de un csv generado
# cuyo path se le pasa como parametro al programa. rutaCsv = './Dev/z_Scrapping/natural-disasters.csv'
# crear ayuda del programa, la misma debe ser dn.py -h
# la ayuda debe mostrar las categorias disponibles para el analisis
# la ayuda debe mostrar el uso del programa dn.py -i <presentacion> -c <categoria> -p <pais> -y <año> -d <decada>
# verificar parametro ingresado -h

#print(sys.argv)

# Declaracion o implementacion de funciones

# ******************************************************************************************************************

# ******************************************************************************************************************

# Crear funcion de ayuda

def ayuda(): 
    print('     ')
    print(' *** Este programa muestra el analisis de datos de desastres naturales ***')
    print('     ')
    print(' El uso del programa es:  dn.py -i <presentacion> -c <categoria> -p <pais> -r <rango>')
    print(' donde:')
    print('     ')
    print(' -i <presentacion> : i = graf, i = tab')
    print(' -c <categoria> : c = seq [sequia], c = ter [terremotos], c = tex [temperaturas extremas], 4 = inu [inundaciones], 5 = des [deslizamientos], 6 = eru [erupciones], 7 = inc [incendios], 8 = tor [tormentas]]')
    print(' -p <pais o continente> : cualquier pais del mundo o continente en ingles. Ejemplo: Brazil, Africa, Asia, Europe, North America, South America, Oceania')
    print(' -r <rango> : desde 1900 hasta 2010')
    print('     ')
    print(' Ejemplo de uso: dn.py graf inu Argentina 1900-2010')
    print('     ')
    print('     ')
    print('Para obtener ayuda sobre cada parametro -i, -c, -p, -r, ingrese: dn.py -h<parametro>')
    print('     ')
    print('dn.py -hi : muestra ayuda sobre el parametro -i <presentacion>')
    print('dn.py -hc : muestra ayuda sobre el parametro -c <categoria>')
    print('dn.py -hp : muestra ayuda sobre el parametro -p <pais>')
    print('dn.py -hr : muestra ayuda sobre el parametro -r <rango>')
    print('     ')
    print('     ')
    print(' *** Fin de ayuda ***')
    print('     ')
    sys.exit()
    return

# ******************************************************************************************************************
# Definir la ayuda del parametro -i <presentacion>
def ayuda_i():
  if sys.argv[1] == '-hi':
      print('     ')
      print(' formato:  dn.py [-i <presentacion>] [-c <categoria>] [-p <pais>] [-r <rango>]')
      print('     ')
      print(' -i <presentacion> : i = graf, i = tab')
      print('     ')
      print('Donde <presentacion> puede ser:')
      print('     ')
      print(' graf : grafico de barras')
      print(' tab : tabla de datos')
      print('     ')
      print('Ejemplo de uso: dn.py graf [-c <categoria>] [-p <pais>] [-r <rango>]')
      print(' --> Imprimira un grafico de barras sobre la categoria, pais y rango seleccionado')
      print('     ')
      print(' *** Fin de ayuda_i ***')
      print('     ')
      sys.exit()
  return
# Fin de funcion ayuda_i

# ******************************************************************************************************************
# Definir la ayuda del parametro -c <categoria>
def ayuda_c():
  if sys.argv[1] == '-hc':
      print('     ')
      print(' formato:  dn.py [-i <presentacion>] [-c <categoria>] [-p <pais>] [-r <rango>]')
      print('     ')
      print(' -c <categoria> : c = seq [sequia], c = ter [terremotos], c = tex [temperaturas extremas], 4 = inu [inundaciones], 5 = des [deslizamientos], 6 = eru [erupciones], 7 = inc [incendios], 8 = tor [tormentas]]')
      print('     ')
      print('Donde <categoria> puede ser:')
      print('     ')
      print(' seq : sequia')
      print(' ter : terremotos')
      print(' tex : temperaturas extremas')
      print(' inu : inundaciones')
      print(' des : deslizamientos')
      print(' eru : erupciones')
      print(' inc : incendios')
      print(' tor : tormentas')
      print('     ')
      print('Ejemplo de uso: dn.py tab ter [-p <pais>] [-r <rango>]')
      print(' --> Imprimira una tabla de datos sobre los terremotos del pais y rango seleccionado')
      print('     ')
      print(' *** Fin de ayuda_c ***')
      print('     ')
      sys.exit()
  return
# Fin de funcion ayuda_c

# ******************************************************************************************************************
# Definir la ayuda del parametro -p <pais>
def ayuda_p():
  if sys.argv[1] == '-hp':
      print('     ')
      print(' formato:  dn.py [-i <presentacion>] [-c <categoria>] [-p <pais>] [-r <rango>]')
      print('     ')
      print(' -p <pais o continente> : cualquier pais del mundo o continente en ingles. Ejemplo: Brazil, Africa, Asia, Europe, North America, South America, Oceania')
      print('     ')
      print('Ejemplo de uso: dn.py tab inu Brazil [-r <rango>]')
      print(' --> Imprimira una tabla de datos sobre las inundaciones en Brasil en el rango seleccionado')
      print('     ')
      print(' *** Fin de ayuda_p ***')
      print('     ')
      sys.exit()
  return
# Fin de funcion ayuda_p

# ******************************************************************************************************************
# Definir la ayuda del parametro -r <rango>
def ayuda_r():
  if sys.argv[1] == '-hr':
      print('     ')
      print(' formato:  dn.py [-i <presentacion>] [-c <categoria>] [-p <pais>] [-r <rango>]')
      print('     ')
      print(' -r <rango> : desde 1900 hasta 2010')
      print('     ')
      print('Ejemplo de uso: dn.py graf inu Argentina 1900-2010')
      print(' --> Imprimira un grafico de barras sobre las inundaciones en Argentina en el rango 1900-2010')
      print('     ')
      print(' *** Fin de ayuda_r ***')
      print('     ')
      sys.exit()
  return
# Fin de funcion ayuda_r

# ******************************************************************************************************************
# Implementacion de la funcion listaEnRango(parametro)
# El parametro es un string formado por dos numeros de 4 digitos entre 1900 y 2010 separados por un guion medio
# La funcion verifica que el rango este cargado correctamente con los siguientes criterios: 
# 1) que el string tenga 9 caracteres
# 2) que los dos numeros esten separados por un guion medio
# 3) que los dos numeros sean de 4 digitos
# 4) que el formato sea n1-n2, donde n1 < n2
# 5) que n1 y n2 esten entre 1900 y 2010 
def listaEnRango(parametro):
  if len(parametro) == 9 and parametro[4] == '-' and parametro[0:4].isdigit() and parametro[5:9].isdigit() and int(parametro[0:4]) < int(parametro[5:9]) and int(parametro[0:4]) >= 1900 and int(parametro[5:9]) <= 2010:
    return True
  else:
    return False


# ******************************************************************************************************************
#                           # Inicio del programa ppal #                                                           *  
# ******************************************************************************************************************


# Definicion de variables
# ruta del csv a analizar 
rutaCsv = './Dev/z_Scrapping/natural-disasters.csv'
# Lectura del csv general - creacion de dataframe, con pandas
df = pd.read_csv(rutaCsv, sep=',', encoding='utf-8')
# Definir una lista de categorias definidas en el csv
listaEnRep = ['tab', 'graf']
listaEnCat = ['seq', 'ter', 'tex', 'inu', 'des', 'eru', 'inc', 'tor']
# Definir una lista de paises definidos en el csv
listaEnPais = df.filter(like = 'Entity')
# convertir listaEnPais en una lista de strings
listaEnPais = listaEnPais['Entity'].tolist()

# Verificar los parametros pasados al programa
# Si no se ingresan parametros, mostrar ayuda. 

if len(sys.argv) == 2 :
  # utilizar excepcion para mostrar ayuda
  try:
    if sys.argv[1] == '-h': ayuda()
    elif sys.argv[1] == '-hi': ayuda_i()
    elif sys.argv[1] == '-hc': ayuda_c()
    elif sys.argv[1] == '-hp': ayuda_p()
    elif sys.argv[1] == '-hr': ayuda_r()
    else: 
      print('Error: No se ingreso ningun parametro correcto')
      sys.exit()
  except:
    print('Error: No se ingreso ningun parametro correcto')
    sys.exit()

elif len(sys.argv) == 5 :
  try: 
    # cargo y verifico representacion = sys.argv[1]
    if sys.argv[1] == 'tab' or sys.argv[1] == 'graf':
      if sys.argv[1] == 'tab':
        representacion = 'tab'
      elif sys.argv[1] == 'graf':
        representacion = 'graf' 
    else:
      print('Error: No se ingresa parametros correctos')
      ayuda()
      sys.exit()

    # cargo y verifico categoria = sys.argv[2]
    if sys.argv[2] in listaEnCat:
      categoria = sys.argv[2]
    else:
      print('Error: No se ingresa parametros correctos')
      ayuda()
      sys.exit()

    # cargo y verifico pais = sys.argv[3]
    if sys.argv[3] in listaEnPais:
      pais = sys.argv[3]
    else:
      print('Error: No se ingresa parametros correctos')
      ayuda()
      sys.exit() 

    # cargo y verifico rango = sys.argv[4]
    if listaEnRango(sys.argv[4]):
      rango = sys.argv[4]
    else:
      print('Error: No se ingresa parametros correctos')
      ayuda()
      sys.exit()

  except:
    print('Error: No se ingreso ningun parametro correcto')
    sys.exit()
else:
  print('Error: No se ingreso ningun parametro correcto')
  ayuda()


# convertir categoria a ingles
if(categoria == 'seq'): categoria = 'drought'
if(categoria == 'ter'): categoria = 'earthquakes'
if(categoria == 'tex'): categoria = 'extreme temperatures'
if(categoria == 'inu'): categoria = 'floods'
if(categoria == 'des'): categoria = 'landslides'
if(categoria == 'eru'): categoria = 'volcanic activity'
if(categoria == 'inc'): categoria = 'wildfires'
if(categoria == 'tor'): categoria = 'storms'



# realizar analisis de datos sobre la tabla auxiliar filtrada por categoria
tabla_aux = df.filter(like = categoria)
# Agregar las regiones para procesar en la primera columna
tabla_aux.insert(0, 'Pais', df['Entity'])
# Agregar los años para procesar en la segunda columna
tabla_aux.insert(1, 'Año', df['Year'])
#tabla_aux['Pais'] = df['Entity']   # agrega las regiones para procesar
#tabla_aux['Año'] = df['Year']      # agrega los años para procesar

tabla_cat = tabla_aux[tabla_aux['Pais'] == pais]  # filtra por region

print(tabla_cat)


