# Agyei Bacchus
# Email: agyei.bacchus92@myhunter.cuny.edu
# Collisions Map

import folium
import pandas as pd
filename = input('Enter filename:')
outf = input('Enter output file name:')

jig = pd.read_csv(filename)
print(jig['TIME'])
mapCUNY = folium.Map(location=[40.75, -74.125],tiles="Cartodb Positron",zoom_start = 10)
for index, row in jig.iterrows(): 
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    name = row["TIME"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapCUNY)
mapCUNY.save(outf)
