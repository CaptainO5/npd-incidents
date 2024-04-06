from src.weather import distance
from src.geocode import GeoCoder, side
from src import config
import os

def test_distance():
    assert distance((0, 0), (0, 1)) == 1

def test_side():
    # Default direction
    assert side(config.CENTER) == 'E'

def test_sides():
    assert side((35.220507, -97.461021)) == 'W'
    assert side((35.238455, -97.445057)) == 'N'
    assert side((35.202891, -97.444199)) == 'S'
    assert side((35.219385, -97.427204)) == 'E'

def test_cache():
    gc = GeoCoder()
    assert not os.path.exists(gc.cache_path) or gc.cache

def test_latlong():
    gc = GeoCoder()

    # Get Location of Norman OK
    assert (35.208566, -97.44451) == gc.get_latlong('')

def test_bad_latlong():
    gc = GeoCoder()

    # Get Location of Default Norman OK
    assert (35.208566, -97.44451) == gc.get_latlong('UNKOENWN') and gc.api_hit_count == 1