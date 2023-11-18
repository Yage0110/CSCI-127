#Jay Bacchus 
#Email: agyei.bacchus92@myhunter.cuny.edu 
#NYC Map

import folium

outfile='nycMap.html'

mapCUNY = folium.Map(location=[40.75, -74.125],zoom_start = 10)
folium.Marker(location = [40.768731, -73.964915], popup = "Hunter College").add_to(mapCUNY)
mapCUNY.save(outfile)

