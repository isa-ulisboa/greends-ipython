def string():
    return "data"
def myfunction():
    return "joana"

import math
def soil_field_capacity(C, S, OM, D, TS):
    a = 0.7919
    b = 0.001691*C
    c = 0.29619*D
    d = 0.000001491*S**2
    e = 0.0000821*OM**2
    f = 0.02427*C**-1
    g = 0.01113*S**-1
    h = 0.01472*(math.log(S))
    i = 0.0000733*OM*C
    j = 0.000619*D*C
    k = 0.001183*D*OM
    l = 0.0001664*TS*S

    return a+b-c-d+e+f+g+h-i-j-k-l


#assignment 6 - calculate Vapour Pressure Deficit    

import math

def calculate_vpd(Tmax, Tmin, RHmean):
    es = (0.6108*math.exp(17.27*Tmax/(Tmax+237.3))+0.6108*math.exp(17.27*Tmin/(Tmin+237.3)))/2
    ea = RHmean/100*es
    vpd = es - ea
    return vpd
    
