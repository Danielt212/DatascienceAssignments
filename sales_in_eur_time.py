import pandas as pd

from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show

output_file('sales_in_eur_time.html',
            title='Sales in EUR over time')
output_notebook() 

df = pd.read_csv('filtered_sales.csv')
df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])

x = df["Transaction Date"]
y = df["Amount (Merchant Currency)"].cumsum()
p = figure(title="Sales in EUR over time", 
           x_axis_label='Date', y_axis_label='Sales (EUR)', 
           x_axis_type="datetime")

p.line(x, y, color="blue", legend_label = "Sales in EUR", line_width=2)

show(p)