import folium
import pandas


def elevation_to_color(elev):
    if elev >= 3000:
        c = 'black'
    elif elev >= 2000:
        c = 'red'
    elif elev >= 1000:
        c = 'lightred'
    else:
        c = 'green'
    return c


# read volcanos data
data = pandas.read_csv("files/volcanoes.txt")

# volcanoes feature group
FG_VOLCANOES = folium.FeatureGroup('Volcanoes')

# add volcanos markers
for i, (name, lat, lon, elev) in enumerate(zip(data["NAME"], data.LAT, data.LON, data.ELEV)):
    color=elevation_to_color(elev)
    marker = folium.CircleMarker(
        radius=8,
        location=(lat, lon),
        popup=name + "\n" + str(elev) + "m",
        color='grey',
        #icon=folium.Icon(color=elevation_to_color(elev)),
        fill=True,
        fill_color=color,
        fill_opacity=0.7
    )
    FG_VOLCANOES.add_child(marker)