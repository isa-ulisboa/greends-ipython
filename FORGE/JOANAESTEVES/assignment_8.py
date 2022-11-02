import netCDF4 as nc
import myFunctions as mf

# First we need a path to the netcdf file

fn = '../../EMEP01_rv4.42_year.2019met_2019emis.nc'
ds = nc.Dataset(fn)

# List of the lat, lon, coordinates and precipitation

lats = ds.variables['lat'][:]
lons = ds.variables['lon'][:]
prec = ds.variables['WDEP_PREC']

# Find the index of the latitude which is nearer to inLat and the same for the longitude

inLat = 38.568
ind_Lat = mf.geo_idx(38.568, lats)
inLon = -9.720
ind_Lon = mf.geo_idx(-9.720, lons)

"""
print(ind_Lat)
print(ind_Lon)
"""

# Retrieve precipitation (WDEP_PREC variable from the dataset) from the location with Lat: 38.568, Lon: -9.720

print(prec[0, ind_Lat, ind_Lon])