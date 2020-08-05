#Author: Tashinga


import folium
import pandas
import json
from geopy.geocoders import Nominatim
from folium.plugins import MarkerCluster,FloatImage

import os

#data resource  = https://www.theguardian.com/world/2020/aug/04/coronavirus-uk-map-the-latest-deaths-and-confirmed-covid-19-cases


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

#return the colour of teh icon and the icon
def health_risk(caseCount):
    if caseCount > 4000:
        return "red","remove","Avoid if Possible"
    elif caseCount > 2000:
        return "orange","eye-open", "Watch this area closely"
    else:
        return "green","check","Proceed with caution"
      

def convert_str_int(val):
    if val.type(str):
        return int(val)
    else:
        return val


map = folium.Map(location= start_coord, zoom_start=8, tiles ="Stamen Terrain")

marker_cluster = MarkerCluster().add_to(map)

#all elements added to map will need to be added between the creation of the map 
#and the saving of the map 

#if string onctains a txt file use popup = folium.Popup(str(hahs), parse_html=True)

feature_group1 = folium.FeatureGroup(name="Points")



for coord, arr, cas, pop in zip(coordinates, area_name, case_count, population):
    lat_value = (coord.split())[0]
    long_value =  (coord.split())[1]

    
    #icon is decided on the case count of the area
    marker_color = health_risk(cas)[0]

    val = 4

    mystring = 'Area: {}, \n Cases: {}, \n N. of people/100K: {}'.format(arr, cas, pop  )
    print(mystring)


    html = """
    <h1> Area: """ + arr +   """</h1><br>
    <p>Cases: """ + str(cas) + """</p>
    <p>Confirmed cases/100k: """ + str(pop) + """</p>
    <p>Conclusion: """ + health_risk(cas)[2] + """</p>


    """

    
    feature_group1.add_child(folium.Marker(location = [lat_value,long_value], popup = html,
    tooltip = arr ,icon = folium.Icon(color=marker_color, icon_color='white', icon=health_risk(cas)[1])))
   


#read the multipoylogon coordinates
# These will map out an area/region to map out the countries by population
#could not find one specifically for the UK at the moment

feature_group2 = folium.FeatureGroup(name="Polygon Layer")

feature_group2.add_child(folium.GeoJson(data=open('World.json' , 'r', encoding = 'utf-8-sig').read(), 
style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 100000 
else 'orange' if 1000000 <= x['properties']['POP2005'] < 20000000 else 'red' })) #encode the data so that its readable

#if the population of the polygon area is less than 100000 then it will be green
#if the population is between 1mil and 20mil then orange else red


#add the legend 
image_file = 'legend1.PNG'

feature_group3 = fFloatImage(image_file, bottom=-5, left=85)

map.add_child(feature_group1)
map.add_child(feature_group2)
map.add_child(feature_group3)

#turn on and off feature groups
map.add_child(folium.LayerControl())

map.save("Map.html")

#print(calculateLatLong(area_name))

