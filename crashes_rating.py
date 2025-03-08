import pandas as pd
import geopandas as gpd 
import numpy as np 

from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.layouts import column
from bokeh.io import output_notebook

#Load data
crashes_df = pd.read_csv("stats_crashes_*_overview.csv") 
ratings_df = load_csv_files("stats_ratings_*overview.csv")
sales_df = pd.read_csv('filtered_sales.csv')

#Format
crashes_df["Date"] = pd.to_datetime(df["Date"])
ratings_df["Date"] = pd.to_datetime(df["Date"])
sales_df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])

# Task 3
ratings_vs_stability = crashes_df.merge(ratings_df, on="Date")
source = ColumnDataSource(ratings_vs_stability)

p1 = figure(title="Crashes vs Daily Average Rating", x_axis_label="Daily Crashes", y_axis_label="Daily Avg Rating",
            plot_width=800, plot_height=400)
p1.circle(x="Daily Crashes", y="Daily Average Rating", source=source, size=8, color="navy", alpha=0.6)
hover = HoverTool(tooltips=[("Date", "@Date{%F}"), ("Crashes", "@Daily Crashes"), ("Avg Rating", "@Daily Average Rating")],
                   formatters={"@Date": "datetime"})
p1.add_tools(hover)

# Task 4
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
ratings_per_country = ratings_df.groupby("Country")["Total Average Rating"].mean().reset_index()
sales_per_country = sales_df.groupby("Buyer Country")["Amount (Merchant Currency)"].sum().reset_index()
merged = world.merge(ratings_per_country, left_on="iso_a3", right_on="Country", how="left").merge(
    sales_per_country, left_on="iso_a3", right_on="Buyer Country", how="left")

source_map = ColumnDataSource(merged)
p2 = figure(title="Geographical Sales and Ratings", plot_width=800, plot_height=500)
p2.patches("xs", "ys", source=source_map, fill_color="Total Average Rating", line_color="black", line_width=0.5,
          fill_alpha=0.7)
hover_map = HoverTool(tooltips=[("Country", "@Country"), ("Avg Rating", "@Total Average Rating"), ("Total Sales", "@Amount (Merchant Currency)")])
p2.add_tools(hover_map)

# Output
output_file("dashboard.html")
show(column(p1, p2))
