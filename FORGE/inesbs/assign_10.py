import netCDF4 as nc
import numpy as np
import json
import argparse
import myfunctions as mf

#API to deliver a JSON with atmospheric N Deposition
#The script will process the arguments passed from outside the code, e.g. 
#assignment_#10.py --lat 37.9 --lon -7.8 --file EMEP01_rv4.42_year.2019met_2019emis.nc


### Section start - PIECE OF CODE TO HANDLE THE ARGUMENTS
parser = argparse.ArgumentParser()

parser.add_argument('--lat', type = float, required=True)
parser.add_argument('--lon', type = float, required=True)
parser.add_argument('--file', type = str, required=True)

args = parser.parse_args()

### Section end - PIECE OF CODE TO HANDLE THE ARGUMENTS

### you can copy code from your previous assignment and adapt your Lat, Lon and NetCDF file to become variables 

