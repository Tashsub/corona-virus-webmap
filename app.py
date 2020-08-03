import folium

#this is where the map will open
#takes in long and lat

coord = [48.310343, 4.137183] #set to france
locations = [[46.233232, 6.139241]]
map = folium.Map(location= coord, zoom_start=5, tiles = "Stamen Terrain" )

#all elements added to map will need to be added between the creation of the map 
#and the saving of the map 





map.Marker(locations[0])
map.save("Map1.html")

