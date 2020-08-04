import folium
import pandas
import geopy

#reource of data = https://www.theguardian.com/world/2020/aug/04/coronavirus-uk-map-the-latest-deaths-and-confirmed-covid-19-cases

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"]) 
lon = list(data["LON"]) 
elevation = list(data["ELEV"])

start_coord = [44.569090, 4.945561] #set to some random location in france

locations = {"France": [46.233232, 6.139241], "Geneva": [46.187067, 6.131917] 

}

map = folium.Map(location= start_coord, zoom_start=5, tiles ="Stamen Terrain")

#all elements added to map will need to be added between the creation of the map 
#and the saving of the map 

#is string onctains a txt file use popup = folium.Popup(str(hahs), parse_html=True)

feature_group = folium.FeatureGroup(name="New Map")

for ln, lg, el in zip(lat, lon, elevation):
    feature_group.add_child(folium.CircleMarker(location = [ln,lg], popup =str(el) + " m", 
    fill_opacity = 0.8, fill_color = 'red', color = 'grey',  radius = 6, weight = 1,))

#read the multipoylogon coordinates
# These will map out an area/region to map out the countries by population
#could not find one specifically for the UK at the moment

feature_group.add_child(folium.GeoJson(data=open('World.json' , 'r', encoding = 'utf-8-sig').read(), 
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 100000 
else 'orange' if 1000000 <= x['properties']['POP2005'] < 20000000 else 'red' })) #encode the data so that its readable

#if the population of the polygon area is less than 100000 then it will be green
#if the population is between 1mil and 20mil then orange else red

#encode the data so that its readable

map.add_child(feature_group)

map.save("Map.html")



