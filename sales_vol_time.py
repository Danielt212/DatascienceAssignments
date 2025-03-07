import pandas as pd

from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

output_file('sales_vol_time.html',
            title='Transaction count over time')
output_notebook() 

df = pd.read_csv('filtered_sales.csv')
df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])
date = df["Transaction Date"].value_counts().sort_index()

x = date.index
y = date.values

p = figure(title="Transaction count per date", 
           x_axis_label='Date', y_axis_label='Transaction Count', 
           x_axis_type="datetime")

p.vbar(x, top = y, width=0.8, color="blue")

show(p)