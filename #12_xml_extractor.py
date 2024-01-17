#%% 

import requests
import pandas as pd

url = 'https://www.coingecko.com/sitemaps/coins-pl.xml'

response = requests.get(url)
with open('sitemap.xml', 'wb') as file: 
    file.write(response.content)

# %%