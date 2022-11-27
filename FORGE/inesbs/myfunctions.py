from cmath import log, log10
import numpy as np

def myfunction():
    return "GreenDS"

def myfunction():
    return "Hello"

def myfirstgreendsfunction():
    return "return of my first function"

def mysecondgreendsfunction():
    return "return of my second function"

def VolWaterContent(c, d, s, om, ts):
    return 0.7919 + 0.001691 * c - 0.29619 * d - 0.000001491 * pow(s, 2) + 0.0000821 * pow(om, 2) + 0.02427 * pow(c, -1) + 0.01113 * pow(s, -1) + 0.01472 * (log(s)) - (0.0000733 * om * c) - (0.000619 * d * c) - (0.001183 * d * om) - (0.0001664 * ts * s)

#function for assignment #6 to calculate vapor pressure

import math

def VPdef(Tmax, Tmin, RHmean):
    e0_Tmax = 0.6108 * np.exp((17.27 * Tmax)/(Tmax + 237.3))
    e0_Tmin = 0.6108 * np.exp((17.27 * Tmin)/(Tmin + 237.3))
    es = (e0_Tmax + e0_Tmin)/2
    ea = es * RHmean/100
    return es - ea


#assignment 8
def geo_index(x_value, x_array):
    """
    Returns:
        _type_: nearest index of the coordinate found in the x_array
    """

    geo_idx = (np.abs(x_array - x_value)).argmin()
    
    return geo_idx