import pandas as pd

df = pd.read_csv('all_sales.csv')
df = df[df['Product id'] == 'com.vansteinengroentjes.apps.ddfive']
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
df.to_csv('filtered_sales.csv', index=False)