import math

# Assignment #3
# define two different functions returning two different strings

def function_re_str(): 
    return("a string")
def function_re_str2():
    return("another string")

# Assignment #4
# create function that returns the Volumetric Water Content at saturation (Field Capacity) a Soil

def vol_water_content_saturated(clay,bulkdensity,silk,OM,topsoil):
    vwcs = 0.7919 + 0.001691*clay - 0.29619*bulkdensity - 0.000001491*silk**2 + 0.0000821*OM**2 + 0.02427*(1/clay) + 0.01113/silk + 0.01472*math.log(silk) - 0.0000733*OM*clay - 0.000619*bulkdensity*clay - 0.001183*bulkdensity*OM - 0.0001664*topsoil*silk
    return(vwcs)