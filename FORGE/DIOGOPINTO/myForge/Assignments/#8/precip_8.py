import netCDF4 as nc
import myFunctions_8 as mf8

file='EMEP01_rv4.42_year.2019met_2019emis.nc'
ds= nc.Dataset(file)

#Getting data: time, lat, long and prec
lats=ds.variables['lat'][:]
lons=ds.variables['lon'][:]
prec=ds.variables['WDEP_PREC'][:]

#Info 
lat=ds.variables['lat']
lon=ds.variables['lon']
pre=ds.variables['WDEP_PREC']

'''print(ds)
print (pre.units)'''


time= ds.variables['time'][:]

#Returning the index of the nearest coordinate found in the list
Lat_v= 38.568
Lon_v= -9.720

lats_index=mf8.nearest_coordinate(Lat_v, lats)
lons_index=mf8.nearest_coordinate(Lon_v, lons)

#Printing the precipitation 
print('Precipitation:',round(prec[0, lats_index, lons_index],2),(pre.units))

