# Step 1: Read csv files hd_crawl.csv and new_design.csv
# Step 2: Add new  column 'is_new_design'
# Step 3: 'is_new_design' check if URL matches the slugs in new_design.csv
# Step 4: Print dataframe

# %%
import pandas as pd
import re

hd_df = pd.read_csv('hd_crawl.csv')
design_df = pd.read_csv('new_design.csv')

def is_new_design(url): 
    match = re.search(r'.*/([^/]+)$', url)
    if match and match.group(1) in design_df['slug'].values:
        return 'yes'
    else:
        return 'no'

# Use apply with a lambda function
hd_df['is_new_design'] = hd_df['URL'].apply(lambda url: is_new_design(url))

# Display the DataFrame
hd_df.head()
