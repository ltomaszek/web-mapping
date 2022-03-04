import folium
from location_data import SAN_MARINO_COOR, ROME_COOR, MADRID_COOR

# create Map
map = folium.Map(location=SAN_MARINO_COOR, zoom_start=5, tiles="Stamen Terrain")

# add 1st marker
folium.Marker(location=SAN_MARINO_COOR, popup="San Marino marker").add_to(map)

# add 2nd marker
map.add_child(folium.Marker(location=ROME_COOR, popup="Rome Marker", icon=folium.Icon(color='red')))

# feature group
fg = folium.FeatureGroup(name="Map")

# add 3nd marker
fg.add_child(folium.Marker(location=MADRID_COOR, popup="Madrid marker", icon=folium.Icon(color='green')))

# add feature group to map
map.add_child(fg)

# create html file
map.save("maps/map_cities.html")