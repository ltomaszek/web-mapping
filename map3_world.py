import folium
from location_data import SAN_MARINO_COOR
import feature_group as fg


POPULATION_2005_YEAR = "POP2005"
map = folium.Map(location=SAN_MARINO_COOR, zoom_start=5, tiles="Stamen Terrain")

# GeoJson
GEOJSON_FILE = 'files/world.json'

# Countries layer
folium.GeoJson(
    name='Countrie',
    data=(open('files/world.json', 'r', encoding='utf-8-sig').read()),
    style_function=lambda x: {
        'fillColor':'green'                                             # fill color depending on country's population size
        if x['properties'][POPULATION_2005_YEAR] <= 10_000_000      
        else 'yellow'
            if x['properties'][POPULATION_2005_YEAR] <= 50_000_000
            else 'red'
                if x['properties'][POPULATION_2005_YEAR] <= 100_000_000
                else 'black'
        }
).add_to(map)

# Volcanoes layer
map.add_child(fg.FG_VOLCANOES)

# LayerControl - must be added after all layers have been added
map.add_child(folium.LayerControl());

map.save("maps/map_world.html")