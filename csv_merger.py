import os
import pandas as pd

master = []

for file in os.listdir(os.getcwd()):
    if file.startswith('sales_'):
        master.append(pd.read_csv(file,on_bad_lines='skip'))  

master_df = pd.concat(master, ignore_index=True)
master_df.to_csv('all_sales.csv', index=False)
