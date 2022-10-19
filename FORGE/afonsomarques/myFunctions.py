def my_funnction1():
    print ("python is amazing")

def my_function2():
    print ("python is very nice")

import numpy as np

def vap_pres_def(Tmax, Tmin, RHm):
    #vap_pres_def = vapor pressure deficit (kPa)
    #Tmax = max temperature (ºC)
    #Tmin = min temperature (ºC)
    #RHm = mean Relative Humidity (kPa)
    
    Es = ((0.6108*np.exp((17.27*Tmax)/(Tmax+237.3)))+(0.6108*np.exp((17.27*Tmin)/(Tmin+237.3)))/2)
    Ea = (RHm/100)*Es
    VPD = (Es-Ea)
    return(VPD)



