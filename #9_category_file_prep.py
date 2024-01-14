# Step 1: Import the file
# Step 2: Create a subset of csv file with desired columns, create so no name is missing 
# Step 3: update the key columns with 'categories.' at the start
# Step 4: Export to JSON file

#%%
import pandas as pd
import numpy as np
import json

df_1 = pd.DataFrame(pd.read_csv('categories.csv',low_memory= False))
df_1 = df_1[['id','key']].copy()

df_2 = pd.DataFrame(pd.read_csv('category_translation.csv',low_memory= False))
df_2 = df_2[['category_id','name']].copy()

df = df_1.merge(df_2, how='left', left_on='id', right_on='category_id')
df = df[['key','name']]
# Create a dictionary from DataFrame
categories_dict = dict(zip(df['key'], df['name']))

# Export dictionary to JSON file
output_file_path = 'Categories name.json'
with open(output_file_path, 'w') as json_file:
    json.dump({'categories': categories_dict}, json_file, indent=2)

print(f"Data saved to {output_file_path}")
