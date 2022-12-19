import numpy as np
import math

def nearest_coordinate(x_value, x_array):
    n_c= (np.absolute(x_array-x_value)).argmin()
    return n_c

