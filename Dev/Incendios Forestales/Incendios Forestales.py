'''
import selenium
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
 #inicio del scraping 
#from bs4 import BeautifulSoup
ruta = ChromeDriverManager(path="./chromedriver").install()

# Opciones de Chrome

#options = webdriver.ChromeOptions()
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

#options.add_argument('--headless')
#options.add_argument('--no-sandbox')
#options.add_argument('--disable-dev-shm-usage')

# Instanciames el servicios de chrome driver
s = Service(ruta)
# Instanciamos el driver de chrome
driver = webdriver.Chrome(service=s, options=options)


#url = 'https://public.emdat.be'
url = 'https://ourworldindata.org/explorers/natural-disasters'
#url = 'https://www.desinventar.net/DesInventar/'
driver.get(url)
#driver.find_element("xpath", '/html/body/div[2]/div/div/div/div[2]/button/span/svg').click() 
time.sleep(5)

# Click en el boton de aceptar cookies
#time.sleep(2)
#driver.find_element("xpath", '/html/body/div[2]/div/div/div/div[2]/button/span/svg').click() 

# Selecciono tormentas
#driver.find_element("xpath",'//*[@id="ExplorerContainer"]/div/form/div[1]/div[2]/div/div[1]/div[1]').click()
#menuDesplegable = driver.find_element("id", "react-select-2-live-region")
#drop = Select(driver.find_element("id", "react-select-2-live-region")).select_by_visible_text("Storms")
#Select(driver.find_element("id", "react-select-2-live-region")).select_by_visible_text("Storms")
#drop.select_by_visible_text("Storms")
time.sleep(2)

# Click a la tabla de datos
driver.find_element("xpath",'//*[@id="ExplorerContainer"]/div/div[3]/div/div[3]/div[2]/nav/ul/li[3]/a').click()
time.sleep(2)
# Click a download
driver.find_element("xpath", '//*[@id="ExplorerContainer"]/div/div[3]/div/div[2]/div[2]/nav/ul/li[5]/a').click()
time.sleep(2)
# Click a CSV
driver.find_element("xpath", '//*[@id="ExplorerContainer"]/div/div[3]/div/div[4]/div/div[2]/div/button/div[2]/span').click()
time.sleep(2)

# Path: chromedriver.exe
#driver = webdriver.Chrome(ChromeDriverManager().install())

input("Presione Enter para continuar...")

driver.quit()
#*************************************************************'''
import pandas as pd

rutaCsv = './Dev/z_Scrapping/natural-disasters.csv'
rutaCsvWildfires = './Dev/Incendios Forestales/incendios forestales.csv'

# Lectura del csv general
df = pd.read_csv(rutaCsv, sep=',', encoding='utf-8')

# Generar csv de sequia y cargar la columna Entity
df_wildfires = df.filter(like='wildfires') # filtrar por drought o sequias
df_wildfires['Pais'] = df['Entity']   # agregar columna pais
print(df_wildfires) 

# Lo guardo en un archivo csv
df_wildfires.to_csv(rutaCsvWildfires, index=False, encoding='utf-8')
