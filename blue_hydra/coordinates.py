import simplekml



location [(lat1, lon1), (lat2, lon2)]

kml = simplekml.Kml()

for new in location:
	lat, lon= new
	kml.newpoint(name='newpoint', coords=[(lon, lat)])

kml.save('waypoints.kml') 
