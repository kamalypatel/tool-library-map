import folium
from folium.plugins import HeatMap
import pandas as pd

data = pd.read_csv('your_file.csv', usecols=['Lat', 'Long'])

lat_lon = data[['Lat', 'Long']].values.tolist()

m = folium.Map(location=[42.887691, -78.879372], zoom_start=10)

HeatMap(lat_lon).add_to(m)

m.save('heatmap.html')