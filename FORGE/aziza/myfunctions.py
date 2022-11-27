import math
import numpy as np



def function():
    return "hello"


def string():
    return "hey"

def fieldcapacity(C,D,S,OM,TS): 
    val1=0.7919 
    val2=0.001691*C
    val3= 0.29619*D
    val4= 0.000001491*(S**2)
    val5= 0.0000821*(OM**2)
    val6= 0.02427*(C**-1)
    val7= 0.01113*(S**-1)
    val8= 0.01472*(math.log(S))
    val9= 0.0000733*OM*C
    val10=0.000619*D*C
    val11=0.001183*D*OM
    val12= 0.0001664*TS*S
    return val1+val2-val3-val4+val5+val6+val7+val8-val9-val10-val11-val12

print(fieldcapacity(0.2,1.3,0.2,0.05,1))

def calculate_vpd(Tmax, Tmin, RHmean):
    eo_Tmax = 0.6108 * np.exp((17.27 * Tmax)/(Tmax + 237.3))
    eo_Tmin = 0.6108 * np.exp((17.27 * Tmin)/(Tmin + 237.3))
    es = (eo_Tmax + eo_Tmin)/2
    ea = es * RHmean/100
    return es - ea

import numpy as np
#create a function  to find the index of nearest coordinate, eg a function that receives as arguments 1) a number (coordinate), and 2) a list (of coordinates), returning the index of the nearest coodinate found in that list
def nearest_index(value_given, array_i):
    difference_array= np.absolute(array_i-value_given)
    nearest_idx = difference_array.argmin()
    return nearest_idx
