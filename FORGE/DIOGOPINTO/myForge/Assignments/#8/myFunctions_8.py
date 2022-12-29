import numpy as np


def nearest_coordinate(x_value, x_array):
    n_c= (np.abs(x_array - x_value)).argmin()
    return n_c

