
def scrapaludes():
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import numpy as np
    url='https://es.wikipedia.org/wiki/Anexo:Avalanchas_en_Chile'
    print(f'Estamos scrapeando la web {url}')
    
    r=requests.get(url).content
    df_list=pd.read_html(r)

    df=df_list[-1]

    df= df.drop('Referencia', axis=1)
    df['Heridos']=pd.to_numeric(df['Heridos'],errors='coerce')
    
    df.to_csv('dfaludes.csv')
    print('Se exportó correctamente a CSV')

    dfaludes_=pd.read_csv('dfaludes.csv')
    dfaludes_= dfaludes_.drop('Unnamed: 0', axis=1)

    print('Leyendo los datos del csv\nRegistro de avalanchas fatales en Chile:')
    print(dfaludes_)

scrapaludes()
