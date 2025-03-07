import pandas as pd
from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.transform import dodge

output_file('sales_vol_sku_country.html', title='Transaction Count by Country and SKU ID')
output_notebook()

df = pd.read_csv("filtered_sales.csv")

grouped = df.groupby(["Buyer Country", "Sku Id"]).size().unstack().reset_index()
print(grouped["Buyer Country"])

source = ColumnDataSource(data={
"Buyer Country": grouped["Buyer Country"],
"premium": grouped["premium"] if "premium" in grouped.columns else [0] * len(grouped),
"unlockcharactermanager": grouped["unlockcharactermanager"] if "unlockcharactermanager" in grouped.columns else [0] * len(grouped)
})

p = figure(title="Transaction Count by Country and SKU ID",
        x_axis_label="Country",
        y_axis_label="Transaction Count",
        x_range=FactorRange(*grouped["Buyer Country"]),
        width=800, height=400)


p.vbar(x=dodge("Buyer Country", -0.2, range=p.x_range), top="premium", source=source, 
    width=0.3, color="blue", legend_label="premium")

p.vbar(x=dodge("Buyer Country", 0.2, range=p.x_range), top="unlockcharactermanager", source=source, 
    width=0.3, color="red", legend_label="unlockcharactermanager")

show(p)