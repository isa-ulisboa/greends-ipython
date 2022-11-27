import netCDF4 as nc
import numpy as np
import myfunctions as mf

fn = (r'c:/Users/inesb/.ipython/greends-ipython/EMEP01_rv4.42_year.2019met_2019emis.nc')
ds =nc.Dataset(fn)


lat = ds.variables['lat']
lon = ds.variables['lon']
prec = ds.variables['WDEP_PREC']

lat_values = ds.variables['lat'][:]
lon_values = ds.variables['lon'][:]
prec_values = ds.variables['WDEP_PREC'][:]

# closest indexes from lat 38.568, lon -9.720

lat_index = mf.geo_index(38.568, lat_values)
lon_index = mf.geo_index(-9.720, lon_values)
#print(lat_index, lat.units)
#print(lon_index, lon.units)

#Precipitation for 85 degrees north, 202 degrees east

print(prec_values[:, lat_index, lon_index], prec.units)

ds.close()

