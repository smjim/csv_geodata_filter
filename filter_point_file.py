from math import radians, cos, sin, asin, sqrt
import pandas as pd

df = pd.read_csv('../../data/mines_data.csv', index_col=0)

# center coords and exclusion radius 
x = 35.9823474 
y = -84.0694523
radius = sqrt(44.0) #kilometers
#x = 38.1121134
#y = -81.361529
#radius = sqrt(100.0) #kilometers

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
df['distance'] = df.apply(lambda row : haversine(row['longitude'], row['latitude'], y, x), axis = 1)
data = df[df['distance'] < radius**2]

# filter out 'problem_types'
#data = data[data['problem_type'] == ('HEF' | 'P' | 'VO')]
data = data[(data['problem_type'] == 'HEF') | (data['problem_type'] == 'P') | (data['problem_type'] == 'VO')]

data.to_csv('out.csv')
print('Successfully generated out.csv')
