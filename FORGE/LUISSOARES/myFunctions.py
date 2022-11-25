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
