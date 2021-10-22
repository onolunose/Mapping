import folium
import pandas
data = pandas.read_csv("volcano.txt")
lat = list(data["LAT"])
lon= list(data["LON"])
elev=list(data["ELEV"])
def icon_colour(elevation):
    if elevation <900:
        return "red"
    elif 900<=elevation<2500:
        return "pink"
    else:
        return "blue"
map =folium.Map(location=[9.078,7.408], tiles="stamen Terrain", zoom_start=6)
fg = folium.FeatureGroup(name="My map")
for lt,ln ,el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], popup= str(el)+"m", icon=folium.Icon(color =icon_colour(el))))
map.add_child(fg)
map.save("volcanomap.html")
