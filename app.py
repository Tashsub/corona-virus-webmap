import folium

#this is where the map will open
#takes in long and lat

coord = [48.310343, 4.137183] #set to france

locations = {"france": [46.233232, 6.139241] }

map = folium.Map(location= coord, zoom_start=5, tiles = "Stamen Terrain" )

#all elements added to map will need to be added between the creation of the map 
#and the saving of the map 

map.add_child(folium.Marker(location = locations["france"], popup ="String", icon = folium.Icon(color = 'green')))




map.save("Map.html")

