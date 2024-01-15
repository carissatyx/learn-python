#%% 
# Step 1 Import CSV file
# Step 2 Calculate 7 day averages crawl request
# Step 3 Store it into a list

#%% 
import pandas as pd
import numpy as np

csv_files = ['www.csv', 'widget.csv']
crawl_request = []

for csv_file in csv_files:
    mean_values = []  # Initialize an empty list for each CSV file
    for i in range(42, 85, 7):  
        df = pd.read_csv(csv_file)
        crawl_data = df.iloc[i:i+7, 1].to_list()
        mean_value = np.mean(crawl_data)
        mean_values.append(mean_value)
    crawl_request.append((csv_file, *mean_values))  # Unpack mean_values

# Convert crawl_request to a DataFrame
columns = ['File'] + [f'Mean_{i}' for i in range(42, 85, 7)]
df_crawl_request = pd.DataFrame(crawl_request, columns=columns)

# Save the DataFrame to a CSV file
df_crawl_request.to_csv('crawl_request.csv', index=False)
# %%
