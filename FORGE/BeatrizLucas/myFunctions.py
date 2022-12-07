import numpy as np

# Functions List

## Simple functions

def myFunction():
    return "hello world"

def myFunction2():
    return "hello world!"

## Soil function

def vol_water_soil_content(C, D, S, OM, topsoil):
    a = 0.7919
    b = 0.001691*C
    c = 0.29619*D
    d = 0.000001491*S**2
    e = 0.0000821*OM**2
    f = 0.02427*C**-1
    g = 0.01113*S**-1
    h = 0.01472*np.log(S)
    i = 0.0000733*OM*C
    j = 0.000619*D*C
    k = 0.001183*D*OM
    l = 0.0001664*topsoil*S
       
    return a+b-c-d+e+f+g+h-i-j-k-l

#print(vol_water_soil_content(0.2, 1.3, 0.1, 0.05, 1))

## Assinment 6 function_VPD function

def calculate_vpd(Tmax, Tmin, RHmean):

    """_summary_This function calculates the daily vapor pressure deficit (kPa). 
      
    Args:
        Tmax (float): daily values of the maximum temperature (celsius)
        Tmin (float): daily values of the minimum temperature (celsius)
        RHmean (float): daily values of the mean realtive humidity (percentage)

    Variables inside the function:
        eo_Tmax (float): saturation vapour pressure at daily maximum temperature (kPa)
        eo_Tmin (float): saturation vapour pressure at daily minimum temperature (kPa)
        es (float): saturation vapour pressure (kPa)
        ea (float): actual vapour pressure (kPa)

    Returns:
        es - ea (float): daily values of vapor pressure deficit (kPa)
    """
   
    eo_Tmax = 0.6108 * np.exp((17.27 * Tmax)/(Tmax + 237.3))
    eo_Tmin = 0.6108 * np.exp((17.27 * Tmin)/(Tmin + 237.3))

    es = (eo_Tmax + eo_Tmin)/2

    ea = es * RHmean/100

    return es - ea

## Assignment 8 function_Coordinates function
## A function to find the index of nearest coordinate

def nearest_index(x_value, x_array):
    """_summary_

        Calculation of the nearest index that a given longitude or latitude corresponds in the NetCDF grid.

        Args:
        x_value (float): longitude or latitude given values 
        x_array (array): array of the values of longitude or latitude extract from the NetCDF file 

    Returns:
        _type_: nearest index of the coordinate found in the x_array
    """

    nearest_idx = (np.abs(x_array - x_value)).argmin()
    
    return nearest_idx