def myFunction():
    return "hello world"




def myFunction2():
    return "hello world!"

import math

def calculate_vpd(Tmax, Tmin, RHmean):

    """_summary_This function calculates the daily vapor pressure deficit (kPa). 
      
    Args:
        Tmax (list): daily values of the maximum temperature (celsius)
        Tmin (list): daily values of the minimum temperature (celsius)
        RHmean (list): daily values of the mean realtive humidity (percentage)

    Variables inside the function:
        eo_Tmax (float): saturation vapour pressure at daily maximum temperature (kPa)
        eo_Tmin (float): saturation vapour pressure at daily minimum temperature (kPa)
        es (float): saturation vapour pressure (kPa)
        ea (float): actual vapour pressure (kPa)

    Returns:
        es - ea (float): daily values of vapor pressure deficit (kPa)
    """
   
    eo_Tmax = 0.6108 * math.exp((17.27 * Tmax)/(Tmax + 237.3))
    eo_Tmin = 0.6108 * math.exp((17.27 * Tmin)/(Tmin + 237.3))

    es = (eo_Tmax + eo_Tmin)/2

    ea = es * RHmean/100

    return es - ea


