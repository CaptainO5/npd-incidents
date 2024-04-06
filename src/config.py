import os

RESOURCE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../resources'))
CITY = ', Norman, OK'
CENTER = (35.220833, -97.443611)

SIDE_ANGLES = [
    ('N', (67.5, 112.5)),
    ('NE', (22.5, 67.5)),
    ('E', (337.5, 22.5)),
    ('SE', (292.5, 337.5)),
    ('S', (247.5, 292.5)),
    ('SW', (202.5, 247.5)),
    ('W', (157.5, 202.5)),
    ('NW', (112.5, 157.5))
]