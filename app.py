#Author: Tashinga


import folium
import pandas
from geopy.geocoders import Nominatim

#data resource  = https://www.theguardian.com/world/2020/aug/04/coronavirus-uk-map-the-latest-deaths-and-confirmed-covid-19-cases

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"]) 
lon = list(data["LON"]) 
elevation = list(data["ELEV"])

data = pandas.read_csv("covid.txt")
area_name = list(data["Area"])
case_count = list(data["Cases"])
population = list(data["Population"])
coordinates = list(data["Coordinates"])


start_coord = [52.947944, -1.881104] #set to some random in the UK

#use this method to calculate the coordinates of an arera
#push these values back into the txt file in an excel sheet 
def calculateLatLong(city_names):
    for x in city_names:
        loc = Nominatim(user_agent="myGeoCoder")
        location = loc.geocode(x)
        return (location.latitude , location.longitude)
        

map = folium.Map(location= start_coord, zoom_start=5, tiles ="Stamen Terrain")

#all elements added to map will need to be added between the creation of the map 
#and the saving of the map 

#if string onctains a txt file use popup = folium.Popup(str(hahs), parse_html=True)

feature_group1 = folium.FeatureGroup(name="Points")

for ln, lg, el in zip(lat, lon, elevation):
    feature_group1.add_child(folium.CircleMarker(location = [ln,lg], popup =str(el) + " m", 
    fill_opacity = 0.8, fill_color = 'red', color = 'grey',  radius = 6, weight = 1,))

#read the multipoylogon coordinates
# These will map out an area/region to map out the countries by population
#could not find one specifically for the UK at the moment

feature_group2 = folium.FeatureGroup(name="Polygon Layer")

feature_group2.add_child(folium.GeoJson(data=open('World.json' , 'r', encoding = 'utf-8-sig').read(), 
style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 100000 
else 'orange' if 1000000 <= x['properties']['POP2005'] < 20000000 else 'red' })) #encode the data so that its readable

#if the population of the polygon area is less than 100000 then it will be green
#if the population is between 1mil and 20mil then orange else red

#encode the data so that its readable

map.add_child(feature_group1)
map.add_child(feature_group2)

#turn on and off feature groups
map.add_child(folium.LayerControl())

map.save("Map.html")

#print(calculateLatLong(area_name))

