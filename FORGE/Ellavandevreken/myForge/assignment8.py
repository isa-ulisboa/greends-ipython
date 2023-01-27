#assignment 8
import netCDF4 as nc
import numpy as np
import myFunctions as mf #zie mijn mapje

fn =(r'C:/Users/gast/Documents/LISSABON/IP/greends-ipython/EMEP01_rv4.42_year.2019met_2019emis.nc')
ds =nc.Dataset(fn)
lat = ds.variables['lat']
lon = ds.variables['lon']
prec = ds.variables['WDEP_PREC']

lat_values = ds.variables['lat'][:]
lon_values = ds.variables['lon'][:]
prec_values = ds.variables['WDEP_PREC'][:]

# the index of the latitude which is nearer to Lat: 38.568 and Lon: -9.720

lat_index = mf.geo_index(38.568, lat_values)
lon_index = mf.geo_index(-9.720, lon_values)

#print(lat_index, lat.units)
#print(lon_index, lon.units)

#Print the precipitation for indexes: lat_index = 85, lon_index = 202

print(prec_values[0, lat_index, lon_index], prec.units)

ds.close()
