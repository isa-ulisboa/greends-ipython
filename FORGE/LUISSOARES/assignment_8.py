import netCDF4 as nc
import numpy as np
import myFunctions as mf

fn = "EMEP01_rv4.42_year.2019met_2019emis.nc"
ds = nc.Dataset(fn)

#List of the lat, lon and percipitation

lats = ds.variables["lat"][:]
lons = ds.variables["lon"][:]
prec = ds.variables["WDEP_PREC"][:]
time = ds.variables["time"][:]


lon_id = mf.obtain_index(-9.720, lons)
lat_id = mf.obtain_index(38.568, lats)


#print(type(prec))
#print(prec)
#print(time)
#print(prec.shape)
#print(ds)
#print(prec[0, 38, -9])
#print(lons)
#print(lon_id)
#print(lat_id)
print("The precipitation value for the given coordinates is", prec[0, lon_id, lat_id],"mm.")
