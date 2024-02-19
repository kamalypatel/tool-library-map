import folium
from folium.plugins import HeatMap

data = [
    [40.748817, -73.985428],
    [37.774929, -122.419416],
]

m = folium.Map(location=[42.887691, -78.879372], zoom_start=10)

HeatMap(data).add_to(m)

m.save('heatmap.html')