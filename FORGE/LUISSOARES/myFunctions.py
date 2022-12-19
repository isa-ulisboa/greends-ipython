def myFunction():
    return "Hello World!"



def myFunction1():
    return "Hello World?"


# Assignment nº6
import numpy as np

def calculate_vpd(Tmax, Tmin, RHmean):
    """Function calculates daily Vapor Pressure Deficit (kPa) between the years 1981-2010, acording to FAO 56.

    Args:
        Tmax (float): Maximum recorded temperature (ºC)
        Tmin (float): Minimum recorded temperature (ºC)
        RHmean (float): Mean of the recorded relative humidity (%)

    Returns:
        float: Daily vapor pressure deficit values (kPa)
    """

    es = (0.6108*np.exp(17.27*Tmax/(Tmax + 237.3)) + 0.6108*np.exp(17.27*Tmin/(Tmin + 237.3))) / 2

    ea = es*(RHmean/100)

    return es - ea


# Assignment nº8

def obtain_index(coord, coord_list):
    """Function that retrieves the nearest index of geographical coordinates in order to obtain precipitation data from the specified location.

    Args:
        coord (float): Retrieves the latitude or longitude in question.
        coord_list (list): Expresses a list of the studied coordinate from the netCDF file.
        
    Returns:
        index (float): Index of the nearest coordinate from the one requested.
    """
    closest_id = (np.absolute(coord_list-coord)).argmin()

    return closest_id
