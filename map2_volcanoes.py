from turtle import color, fillcolor
from unicodedata import name
import folium
import feature_group as fg


# Add map
map = folium.Map(location=(fg.lat, fg.lon), zoom_start=5, tiles="Stamen Terrain")

# Add volcanoes markers
map.add_child(fg.FG_VOLCANOES)

# Layer Control
map.add_child(folium.LayerControl())

map.save("maps/map_volcanoes.html")