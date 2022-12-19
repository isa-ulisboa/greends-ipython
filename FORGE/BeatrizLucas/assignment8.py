# Assignement 8_get precipitation from location inLat: 38.568, inLon: -9.720
import netCDF4 as nc
import myFunctions as func
import numpy as np 

f = "EMEP01_rv4.42_year.2019met_2019emis.nc"
ds = nc.Dataset(f)

#print(ds)
#print(ds.variables.keys()) # get all the varibles names
#print(ds.dimensions)

# Access to time, latitude, longitude and precipitation data 

time = ds.variables['time']
lat = ds.variables['lat']
lon = ds.variables['lon']
precipitation = ds.variables['WDEP_PREC']

#print(time)
#print(time[:])
#print(lat)
#print(lon)
#print(precipitation)
#print(precipitation.dimensions)

# Extract latitude, longitude, time and precipitation values to numpy arrays

lat_values = ds.variables['lat'][:]
lon_values = ds.variables['lon'][:]
time_values = ds.variables['time'][:]
precipitation_values = ds.variables['WDEP_PREC'][:]

#print(lat_values)
#print(lon_values)
#print(precipitation_values)
#print(lat_values.shape)
#print(lon_values.shape)


# Get the closest indexes from location inLat: 38.568, inLon: -9.720

lat_index = func.closest_index(38.568, lat_values)
lon_index = func.closest_index(-9.720, lon_values)

#print(lat_index, lat.units)
#print(lon_index, lon.units)

# Print the precipitation for those indexes (lat_index = 85, lon_index = 202)

print(precipitation_values[0, lat_index, lon_index], precipitation.units)

print("done")