import os
import pandas as pd

master_sales = []
master_crashes = []
master_ratings = []

for file in os.listdir(os.getcwd()):
    if file.startswith('sales_'):
        master_sales.append(pd.read_csv(file,on_bad_lines='skip'))  
    elif file.startswith('stats_crashes_') and file.endswith('_overview.csv'):
        master_crashes.append(pd.read_csv(file, on_bad_lines='skip'))
    elif file.startswith('stats_ratings_') and file.endswith('_overview.csv'):
        master_ratings.append(pd.read_csv(file, on_bad_lines='skip'))

crashes_df = pd.concat(master_crashes, ignore_index=True)
ratings_df = pd.concat(master_ratings, ignore_index=True)
sales_df = pd.concat(master_sales, ignore_index=True)

crashes_df.to_csv('all_crashes.csv', index=False)
ratings_df.to_csv('all_ratings.csv', index=False)
sales_df.to_csv('all_sales.csv', index=False)
