from geopy.geocoders import Geocodio
from src import config
import numpy as np
import os
import sys
import pickle

def side(loc_latlong):
    # Shift the center to (0, 0)
    y, x = loc_latlong
    y -= config.CENTER[0] # longitude
    x -= config.CENTER[1] # latitude

    angle = np.arctan2(y, x) * 180 / np.pi % 360

    # Return the side of the town if angle falls in the range
    for side, angle_range in config.SIDE_ANGLES:
        if angle >= angle_range[0] and angle < angle_range[1]:
            return side
    return 'E' # Default to East side

class GeoCoder:
    def __init__(self):
        self.geocoder = Geocodio(api_key='89c56386313b867160e7b69e600b6c676c9617e')
        self.cache_path = os.path.join(config.RESOURCE_PATH, 'latlong_cache.pkl')
        if os.path.exists(self.cache_path):
            with open(self.cache_path, 'rb') as f:
                self.cache = pickle.load(f)
        else:
            self.cache = {}
        self.api_hit_count = 0

    def update_cache(self):
        with open(self.cache_path, 'wb') as f:
            pickle.dump(self.cache, f)

    def get_latlong(self, location):
        # Handle locations of the type "lat;long"
        try:
            if ';' in location:
                latlong = location.split(';')
                latlong = (float(latlong[0]), float(latlong[1]))
                return latlong
        except ValueError:
            print('Location is not of kind "lat;long": ' + location, file=sys.stderr)

        if location not in self.cache:
            try:
                self.api_hit_count += 1
                loc = self.geocoder.geocode(location + config.CITY)
                self.cache[location] = (loc.latitude, loc.longitude) if loc else config.CENTER
            except Exception: # Location not found
                self.cache[location] = config.CENTER

        return self.cache[location]