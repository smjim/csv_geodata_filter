from math import radians, cos, sin, asin, sqrt
import pandas as pd
import numpy as np
import re

# load waypoints from .gpx file into np arr `combined`
GPXfile = '../../data/GraphHopper.gpx' 
waypoints = open(GPXfile).read()
lat = np.array(re.findall(r'lat="([^"]+)',waypoints),dtype=float)
lon = np.array(re.findall(r'lon="([^"]+)',waypoints),dtype=float)
combined = np.array(list(zip(lat,lon)))
# points of interest
poi = pd.read_csv('../../data/mines_data.csv', index_col=0)

# exclusion radius
radius = 20.0 #kilometers

# use haversine formula to calculate distance between given and data coords
# function from Michael Dunn (stackoverflow)
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r

# filter out data farther away than the radius permits
# 'great circle' distance using haversine formula 
filtered = pd.DataFrame()
def filter_data(pos):
	global filtered
	x = pos[0]
	y = pos[1]
	poi['distance'] = poi.apply(lambda row : haversine(row['longitude'], row['latitude'], y, x), axis = 1)
	filtered = filtered.append(poi[poi['distance'] < radius])
	print(filtered)

np.apply_along_axis(filter_data, axis=1, arr=combined)

# filter out 'problem_types'
filtered = filtered[(filtered['problem_type'] == 'HEF') | (filtered['problem_type'] == 'P') | (filtered['problem_type'] == 'VO')]

# eliminate duplicates
filtered.drop_duplicates()

filtered.to_csv('out.csv')
print('Successfully generated out.csv')
