Información sobre el archivo .py

Contiene la función para realizar el scrapping de un sitio web. 
*Importación de librerías: las mismas serán utilizadas para el scrapping como para manipular el csv. 
*Scrapping: se realiza la captura del sitio utilizando varios métodos como requests/beautiful soup, de acuerdo
al tipo de contenido y codificicación del sitio web. 
*Soup: se buscan elementos con beautiful soup para crear listas con los mismos. Estas listas serán 
las que conformarán cada columna del dataframe. 
*Armado de tabla: se genera una tabla la cual se almacena en una variable.
*Limpieza de datos: algunos datos del dataframe se limpiaron y se dió formato para una utilización posterior sin
errores. 
*Exportación a csv: mediante Pandas se exportó a un archivo csv, el cual se analizará posteriormente.
