import folium
from folium.plugins import HeatMap
import pandas as pd

data = pd.read_csv('latlongvalues.csv', usecols=['Latitude', 'Longitude'])

lat_lon = data[['Latitude', 'Longitude']].values.tolist()

#this is the general lat long for Buffalo NY
m = folium.Map(location=[42.887691, -78.879372], zoom_start=10)

HeatMap(lat_lon).add_to(m)

m.save('heatmap.html')