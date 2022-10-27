from math import exp, log


def myfirst():
    return "Hello"

def mysecond():
    return "Hi"

#Soil Field Capacity

def soil_field_capacity(C,D,S,OM,topsoil):
    a=0.7919
    b=0.001691*C
    c=0.29619*D
    d=0.000001491*S**2
    e=0.0000821*OM**2
    f=0.02427*C**-1
    g=0.01113*S**-1
    h=0.01472*log(S)
    i=0.0000733*OM*C
    j=0.000619*D*C
    k=0.001183*D*OM
    l=0.0001664*topsoil*S

    return a+b-c-d+e+f+g+h-i-j-k-l

#Tmax = Temp max (ºC)
#Tmin = Temp min (ºC)
#RHmean = Mean of Relative Humidity (kPa)
def calculate_vpd(Tmax,Tmin,RHmean):
    eTmax=((0.6108*exp((17.27*Tmax))/(Tmax+237.3)))
    eTmin=((0.6108*exp((17.27*Tmin))/(Tmin+237.3)))

    #saturation vapour pressure: es
    es=(eTmax+eTmin)/2

    #actual vapour pressure: ea
    ea=(es*RHmean)/100

    #vapour pressure deficit: vpd
    vpd=es-ea
    return(vpd)

