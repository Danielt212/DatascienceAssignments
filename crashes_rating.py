import pandas as pd
import geopandas as gpd 
import numpy as np 

from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.layouts import column
from bokeh.io import output_notebook

#Load data
crashes_df = pd.read_csv("stats_crashes_*_overview.csv") 
ratings_df = load_csv_files("stats_ratings_*_country.csv")
sales_df = pd.read_csv('filtered_sales.csv')

#Format
crashes_df["Date"]
ratings_df["Date"]
sales_df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])

