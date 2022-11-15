
def scrapterremoto():
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    url='https://ourworldindata.org/natural-disasters#data-quality'
    print(f'Estamos scrapeando la web {url}')

    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html.parser')
    tabla=soup.find('table',attrs={'class':'tablepress tablepress-id-100'})

    rows=soup.find('table',attrs={'class':'tablepress tablepress-id-100'}).find('tbody').find_all('tr')
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

    df=pd.DataFrame({'Ranking':ranking,'Ciudad':ciudades,'Año':fechas,'Muertes':muertes,'Magnitud':magnitud})

    df['Año']=pd.to_numeric(df['Año'],errors='coerce')
    df['Magnitud']=pd.to_numeric(df['Magnitud'],errors='coerce')

    df['Muertes'] = df['Muertes'].str.replace(',','').astype(float)

    df.to_csv('dfterremoto.csv')
    print('Se exportó correctamente a CSV')

    dfterremoto_=pd.read_csv('dfterremoto.csv')

    dfterremoto_= dfterremoto_.drop('Unnamed: 0', axis=1)

    print('Leyendo los datos del csv\nRanking de los terremotos más devastadores:')
    print(dfterremoto_)


scrapterremoto()

