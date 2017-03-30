import pickle
from scipy.spatial import distance
import pandas as pd

# Load in the rgb-pantone mapping
rgb_to_pantone = pickle.load(open("rgb_to_pantone.p", "rb"))

# The following method could be vectorized with something like 
# min(sqrt (rgb_keys - rgb_target .^2))

def closest_pantone(r, g, b):
    rgb_keys = rgb_to_pantone.keys()
    # maximum rgb distance = sqrt(3*(255^2)) = 441.67...
    min_dist = 442
    x1 = (r, g, b)
    i_min = -1
    # iterate pantone color keys
    for i in range(0, len(rgb_keys)):
        # convert the key to a tuple
        x2 = rgb_keys[i].split(", ")
        x2 = tuple(map(int, x2))
        dist = distance.euclidean(x1, x2)
        # update min
        if dist < min_dist:
            min_dist = dist
            i_min = i
    return rgb_to_pantone[rgb_keys[i_min]]
