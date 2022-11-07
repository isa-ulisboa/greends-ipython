import numpy as np
def MyFirstGreenDSFunction():
    return "This is the return of my first function"

def MySecondGreenDSFunction():
    return "This is the return of my second function"

def calculate_vpd(Tmax, Tmin, RHmean):
    eo_Tmax = 0.6108 * np.exp((17.27 * Tmax)/(Tmax + 237.3))
    eo_Tmin = 0.6108 * np.exp((17.27 * Tmin)/(Tmin + 237.3))
    es = (eo_Tmax + eo_Tmin)/2
    ea = es * RHmean/100
    return es - ea