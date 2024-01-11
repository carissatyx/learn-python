#%% 
import pandas as pd
import requests
import time 
from bs4 import BeautifulSoup

urls = ['coingecko.com']

indexes = {}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

def make_request(url,headers): 
    try: 
        r = requests.get(url,headers=headers)
    except requests.exceptions.RequestException as e: 
        raise SystemExit(e)
    return r

for url in urls: 
    search_url = f'https://www.google.com/search?q=site%3A{url}&sca_esv=597070936&ei=rvOdZaP_JfzZseMPh86d8A4&ved=0ahUKEwijjq281tGDAxX8bGwGHQdnB-4Q4dUDCBA&uact=5&oq=site%3A{url}&gs_lp=Egxnd3Mtd2l6LXNlcnAiEnNpdGU6Y29pbmdlY2tvLmNvbUiKDVCEAlj_C3ABeAGQAQCYAXOgAbUFqgEEMTEuMrgBA8gBAPgBAcICChAAGEcY1gQYsAPiAwQYACBBiAYBkAYI&sclient=gws-wiz-serp'
    r = make_request(search_url, headers)
    soup = BeautifulSoup(r.text,"html.parser")
    index = soup.find('div',{'id':'result-stats'}).text
    index  = index.split('About ')[1].split(' results')[0]
    indexes[url] = index
    time.sleep(1)

df = pd.DataFrame.from_dict(indexes, orient='index', columns= ['indexed_pages'])
df.to_csv('indexes_pages_2.csv')
# %%
df_2 = pd.read_csv(r'indexes_pages_2.csv')
df.head()
# %%
