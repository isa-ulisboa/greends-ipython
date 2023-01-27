def firstfun():
  return "first"

def secondfun():
  return "second"

#assignment 4 (zie link paper table 5 voor formule)
import math


def VolumetricWaterContent(clay, silt, D , OM, topsoil):
  vwc = 0.7919+0.001691*clay-0.29619*D-0.000001491*silt**2+0.0000821*OM**2+0.02427*clay**(-1)+0.01113*silt**(-1)+0.01472*math.log(silt)-0.0000733*OM*clay-0.000619*D*clay-0.001183*D*OM-0.0001664*topsoil*silt
  return(vwc)
# Test your function with :
# clay:0.2
# silt: 0.1
# bulk density: 1.3
# om: 0.05 
# topsoil: 1

# result should be 0.606 

#test:
t = VolumetricWaterContent(0.2,0.1,1.3,0.05,1)
print(t)



#voor assingment 6
exp = math.exp

def calculate_vpd(Tmax, Tmin, RHmean):
  """calculate_vpd(Tmax, Tmin, RHmean) calculates Vapour Pressure Deficit in kPa
  Args:
  Tmax (float): Maximum temperature (°C)
  Tmin (float): Minimum temperature (°C)
  RHmean (float): Mean relative humidity (%)
  """
  # calculate es = mean saturation pressure in kPa
  es = (0.6108 * exp( 17.27*Tmax / (Tmax+237.3) ) + 0.6108*exp( 17.27*Tmin / (Tmin+237.3) ) ) / 2
  # calculate ea = actual vapour pressure in kPa
  ea = RHmean / 100 * es
  # calculate vapour pressure deficit in kPa
  vpd = es - ea 
  return(vpd)
#test
t = calculate_vpd(0.2,0.1,1.3)
print(t)



##mapje my functions
from cmath import log, log10
import numpy as np
import math

#assignment 8
def geo_index(x_value, x_array):
  """
  Returns:
    type_: nearest index of the coordinate found in the x_array
  """
  geo_idx = (np.abs(x_array - x_value)).argmin()
  
  return geo_idx