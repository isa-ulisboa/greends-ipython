
# Load your NetCDF as before:
import netCDF4 as nc 
import aux_func
fn = 'EMEP01_rv4.42_year.2019met_2019emis.nc' # update this path to your own file
ds = nc.Dataset(fn)

###
#this method is only applicable for this specific cordinnate grid
#bea method is much more accurate
###

#list of the lat, lon, coordinates and precipitation
lats = ds.variables['lat'][:]#85
lons = ds.variables['lon'][:]#202
prec = ds.variables['WDEP_PREC'][:]

###time is "irelevant" because it as only one value
time = ds.variables['time'][:]

#acess precipiation data units
precipitation = ds.variables['WDEP_PREC']

#insert the coordinates you want
lat_value = 38.568
lat_index = aux_func.indexlat2(lat_value)

#insert the coordiantes you want
lon_value = -9.720
lon_index = aux_func.indexlon2(lon_value)

#just to be more readable
print('')
print( 'Registered precipitation ->',  prec[0, lat_index, lon_index], precipitation.units)
print('')
