# Load your NetCDF as before:
import netCDF4 as nc 
import numpy as np
import myfunctions as f
fn = "EMEP01_rv4.42_year.2019met_2019emis.nc" # update this path to your own file
ds = nc.Dataset(fn)
print (ds)
#list of the lat, lon, coordinates and precipitation
lats = ds.variables['lat'][:]
lons = ds.variables['lon'][:]
prec = ds.variables['WDEP_PREC']
print(lats)
print(lons)
print(prec)
# element to which nearest value is to be found
Lats1 = 38.568
Lons1 = -9.720
# find the index of minimum element from the array
lats_index = f.nearest_index(Lats1, lats)
print (lats_index)
lons_index = f.nearest_index(Lons1, lons)
print (lons_index)
#print the precipitation for those indexes (wich is the precipitation of the inLat and inLon)
print(prec[-1,lats_index, lons_index])

