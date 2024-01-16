#%% 
import pandas as pd 

df = pd.read_csv('hreflang_all.csv')

#drop columns
df = df.drop(df.columns[7:],axis="columns")
drop_df = df.drop(df.columns[5],axis='columns')

#melt 
crawl_df = pd.melt(drop_df, id_vars='Address', value_vars=drop_df.iloc[:,4:], var_name='hreflangUrls', value_name='Hreflang').dropna()

crawl_df.head(10)

value = 'https://www.coingecko.com/zh'
result = crawl_df.isin([value])
print(result)


# %%
