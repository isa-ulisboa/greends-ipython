import math
import numpy as np

# Assignment #3
# define two different functions returning two different strings

def function_re_str(): 
    return("a string")
def function_re_str2():
    return("another string")

# Assignment #4
# create function that returns the Volumetric Water Content at saturation (Field Capacity) a Soil

def vol_water_content_saturated(clay,bulkdensity,silk,OM,topsoil):
    """calculates the Volumetric Water Content at saturation (Field Capacity) of a Soil"""
    vwcs = 0.7919 + 0.001691*clay - 0.29619*bulkdensity - 0.000001491*silk**2 + 0.0000821*OM**2 + 0.02427*(1/clay) + 0.01113/silk + 0.01472*math.log(silk) - 0.0000733*OM*clay - 0.000619*bulkdensity*clay - 0.001183*bulkdensity*OM - 0.0001664*topsoil*silk
    return(vwcs)

# Assignment #6
# create function which is going to calculate Vapour Pressure Deficit according to FAO Report nr 56

def calculate_vpd(Tmax, Tmin, RHmean):
    """calculate_vpd(Tmax, Tmin, RHmean) calculates Vapour Pressure Deficit in kPa
    Args:
        Tmax (float): Maximum temperature (°C)
        Tmin (float): Minimum temperature (°C)
        RHmean (float): Mean relative humidity (%)
    """
    # calculate es = mean saturation pressure in kPa
    es = (0.6108 * np.exp( 17.27*Tmax / (Tmax+237.3) ) + 0.6108*np.exp( 17.27*Tmin / (Tmin+237.3) ) ) / 2 
    # calculate ea = actual vapour pressure in kPa
    ea = RHmean / 100 * es
    # calculate vapour pressure deficit in kPa
    vpd = es - ea 
    return(vpd)

# Assignment #8
# create a function to find the index of nearest coordinate,
# receiving as arguments a number (coordinate) and a list (of coordinates),
# returning the index of the nearest coodinate found in that list
def nearest_coord_index(coord, coord_list):
    """given a coordinate and a list of coordinates, this function returns the index of
    the nearest coordinate in the list to the given coordinate

    Args:
        mycoord (float): the given coordinate
        coord_list (list): list of coordinates we have values for
    
    Returns:
        index (integer): index of that coordinate in the list which is closest to the given one (arg1)

    """
    index = np.absolute(coord_list-coord).argmin()
    return(index)
