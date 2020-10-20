import folium
import pandas as pd
import json
from folium import plugins

df = pd.read_csv('olist_customers_dataset.csv')

with open('laMap.geojson') as f:
    laArea = json.load(f)
