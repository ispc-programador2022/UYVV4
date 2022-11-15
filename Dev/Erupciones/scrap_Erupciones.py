
import selenium
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


'''
# script de la generacion del csv general, donde se incluyen todos los datos
# de aca se extaera la informacion de sequia para cada pais

# Inicio del Srapping
#
#**********************************************************************************************************************

ruta = ChromeDriverManager(path="./chromedriver").install()

# Opciones de Chrome
options = Options()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")
options.add_argument("--disable-web-security")
options.add_argument("--disable-notifications")
options.add_argument("--disable-ignore-certificate-errors")
options.add_argument("--no-sandbox")
options.add_argument("--log-level=3")
options.add_argument("--allow-running-insecure-content")
options.add_argument("--no-default-browser-check")
options.add_argument("--no-first-run")
options.add_argument("--no-proxy-server")
options.add_argument("--disable-blink-features=AutomationControlled")

# Parametros a omitir en el inicio de crhome driver
exp_opt=[
    'enable-automation',
    'enable-logging',
    'ignore-certificate-errors',
]
options.add_experimental_option("excludeSwitches", exp_opt)

#Parametros que definen preferencias en chromedriver
prefs = {
    'profile.default_content_setting_values': 2,
    'intl.accept_languages': ["es-ES,es"],
    'credentials_enable_service': False
}
options.add_experimental_option('prefs', prefs)


# Instanciames el servicios de chrome driver
s = Service(ruta)

# Instanciamos el driver de chrome
driver = webdriver.Chrome(service=s, options=options)

# Iniciamos el driver
#url = 'https://public.emdat.be'
url = 'https://ourworldindata.org/explorers/natural-disasters'
#url = 'https://www.desinventar.net/DesInventar/'
driver.get(url)
time.sleep(5)

# Click a la tabla de datos
driver.find_element("xpath",'//*[@id="ExplorerContainer"]/div/div[3]/div/div[3]/div[2]/nav/ul/li[3]/a').click()
time.sleep(2)
# Click a download
driver.find_element("xpath", '//*[@id="ExplorerContainer"]/div/div[3]/div/div[2]/div[2]/nav/ul/li[5]/a').click()
time.sleep(2)
# Click a CSV
driver.find_element("xpath", '//*[@id="ExplorerContainer"]/div/div[3]/div/div[4]/div/div[2]/div/button/div[2]/span').click()
time.sleep(2)


input("Presione Enter para continuar...")

driver.quit()
#**********************************************************************************************************************

# Fin del Srapping

#**********************************************************************************************************************

'''

# script de la generacion del csv para sequia para cada pais por decada
# utilizar pandas para la lectura del csv general

import pandas as pd

rutaCsv = './Dev/z_Scrapping/natural-disasters.csv'
rutaCsvDrought = './Dev/Erupciones/erupciones.csv'

# Lectura del csv general
df = pd.read_csv(rutaCsv, sep=',', encoding='utf-8')

# Generar csv de sequia y cargar la columna Entity
df_erupciones = df.filter(like='volcanic activity') # filtrar por drought o sequias
df_erupciones['Pais'] = df['Entity']   # agregar columna pais
print(df_erupciones) 

# Lo guardo en un archivo csv
df_erupciones.to_csv(rutaCsvDrought, index=False, encoding='utf-8')
