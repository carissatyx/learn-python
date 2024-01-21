# %%
# Converting crawled not indexed to Python
# Step 1: Read the CSV
# Step 2: New column called subfolder - REGEX
# Step 3: New column called language - REGEX & IF
# Step 4: New column called currency - REGEX
# Step 5: New column called EN or I18N- REGEX
# Step 6: Create a pivot table via subfolder
# Step 7: Create a bar chart for each subfolder

# %%
import pandas as pd 
import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt
import re

pd.set_option('max_colwidth', 0)

df = pd.read_csv('file_name')

def subfolder(url): 
    if re.search("/nft/",url):
        return "NFT"
    elif re.search("\?__cf_chl",url):
        return "?__cf_chl"
    elif re.search("\?",url):
        return "Query Param"
    elif re.search("categories/",url):
        return "Categories"
    elif re.search("/historical_data",url):
        return "Historical Data"
    elif re.search(".*/(munze|coins|monedas|pièces|koin_koin|monete|コイン|코인|waluty|moedas|Криптовалюты|coin|coins|ty_gia|數字貨幣|数字货币|عملات)/[^/]+/(([a-z]{3})|(bits|link|sats))$",url):
        return "Currency"
    elif re.search("börsen|exchanges|intercambios|platesformes|pertukaran|cambi|交換所|거래소|giełdy|câmbios|обмен|การซื้อขาย|borsalar|san_giao_dich|交易平台|عمليات التبادل",url):
        return "Exchanges"
    elif re.search("/(munze|coins|monedas|pièces|koin_koin|monete|コイン|코인|waluty|moedas|Криптовалюты|coin|ty_gia|數字貨幣|数字货币|عملات)/[^/]+$",url):
        return "Coins"
    else:
        return "Others"
    
def language(url): 
    lang = re.search(r"/([a-z]{2})/", url)
    if lang is not None:
        lang_match = lang.group(1)
        return lang_match
    else:
        return 'en'

def currency(subfolder,url): 
    if subfolder == 'Currency': 
        curr = re.search(".*/([a-z]{3}|bits|link|sats)+$",url)
        curr = curr.group(1)
        return curr 
    else:
        return ""

def EN_or_I18N(language): 
    if language == 'en': 
        return "EN"
    else: 
        return "I18N"

df['Subfolder'] = df['URL'].apply(lambda url: subfolder(url))
df['Language'] = df['URL'].apply(lambda url:language(url))
df['Currency'] = df.apply(lambda row: currency(row['Subfolder'],row['URL']), axis = 1)
df['EN_or_I18N'] = df['Language'].apply(lambda language:EN_or_I18N(language))

df.head()

# %% 
columns_inc = ['URL','Subfolder']
pivotTable = pd.pivot_table(df[columns_inc], index= 'Subfolder', aggfunc='count')
pivotTable.sort_values(by=['URL'], ascending=False)

#%% 
plt.figure(figsize = (12,12))
sns.barplot(x = 'Subfolder', y = 'URL', data = pivotTable)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Subfolder', fontsize=16)
plt.ylabel('URL', fontsize=16)
plt.show()
# %%
