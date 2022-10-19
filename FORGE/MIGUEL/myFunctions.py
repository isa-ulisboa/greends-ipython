from math import log


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