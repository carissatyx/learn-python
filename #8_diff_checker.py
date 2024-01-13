#%% 
import os
print(os.getcwd())
# %%
import pandas as pd
import numpy as np

df_1 = pd.DataFrame(pd.read_csv('internal_all.csv',low_memory = False, header = 0))
df_1 = df_1[['Address','Status','Inlinks']].copy()

df_2 = pd.DataFrame(pd.read_csv('internal_all.csv',low_memory= False, header=0))
df_2 = df_2[['Address','Status','Outlinks']].copy()

df = pd.merge(df_1, df_2, left_on='Address', right_on='Address', how='outer')

df['Diff Links'] = df['Inlinks'] - df['Outlinks']
df['Diff Status'] = np.where((df['Status_x']) == (df['Status_y']),"Yes", "No")

df.to_csv("compare_links.csv")
# %%
df_3 = pd.read_csv('compare_links.csv')
df_3.head()
# %%
