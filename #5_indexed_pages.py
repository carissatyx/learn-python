# %%
import pandas as pd 
import time 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

urls = [ 
    'coinmarketcap.com', 
    'coingecko.com', 
    'coinbase.com'
]

indexes = {}
xpath = '//*[@id = "result-stats"]'

def get_index(url,xpath,headless = True):
    print(f'Opening {url}')
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    index = driver.find_element("xpath",'//*[@id = "result-stats"]').text
    index = index.split('About ')[1].split(' results')[0]
    print(f'Index: {index}')
    driver.quit()
    return index

for url in urls: 
    search_url = f'https://www.google.com/search?q=site%3A{url}&sca_esv=597070936&ei=rvOdZaP_JfzZseMPh86d8A4&ved=0ahUKEwijjq281tGDAxX8bGwGHQdnB-4Q4dUDCBA&uact=5&oq=site%3A{url}&gs_lp=Egxnd3Mtd2l6LXNlcnAiEnNpdGU6Y29pbmdlY2tvLmNvbUiKDVCEAlj_C3ABeAGQAQCYAXOgAbUFqgEEMTEuMrgBA8gBAPgBAcICChAAGEcY1gQYsAPiAwQYACBBiAYBkAYI&sclient=gws-wiz-serp'
    index = get_index(search_url,xpath,headless=True)
    indexes[url] = index
    time.sleep(1)

df = pd.DataFrame.from_dict(indexes, orient='index', columns=['indexed_pages'])
df.to_csv('indexed_pages.csv')
# %%
df1 = pd.read_csv(r'indexed_pages.csv')
df1.head()

# %%
