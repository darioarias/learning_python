"""In this example, I intend to create a data classes that allows for sorting"""
from dataclasses import dataclass

@dataclass(frozen=False, order=True)
class Coordinate(object):
  lat: float = 0
  lon: float = 0
  name: str = ""

nyc = Coordinate(40.730610, -73.935242, "New York City")
la = Coordinate(34.052235, -118.243683, "Los Angeles")
sf = Coordinate(37.733795, -122.446747, "San Francisco")
sa = Coordinate(29.424349, -98.491142, 'San Antonio')
# changing some values to test my sorting_keys
# nyc.lon = 0
# sf.lon = 0
# la.lon = 0

# takes a coordiante and returning a sorting value in the form of (lon, lat) which is used to sort the given coordinate
def sort_by_lon_first(obj: Coordinate):
  return (obj.lon, obj.lat)

# takes a coordinate and returns a sorted value in the form of (lat, lon) which is used to sort the coordinate
def sort_by_lat_first(obj: Coordinate):  # you may realize that this is the natural order for the coordinate. So this key does not do much. 
  return (obj.lat, obj.lon)              # But if there were to be a clash between lat and lon, name will break the tie. 
                                         # But a clash would not make sense since it would mean the same location  

for city in sorted([nyc, la, sf, sa], key=sort_by_lat_first, reverse=True):
  print(f'{city.name}')