
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
lats_var = ds.variables['lat'][:]#85
lons_var = ds.variables['lon'][:]#202
prec = ds.variables['WDEP_PREC'][:]

###time is "irelevant" because it as only one value
time = ds.variables['time'][:]

#acess precipiation data units
precipitation = ds.variables['WDEP_PREC']

#insert the coordinates you want
lat_value = 38.568
lon_value = -9.720
cor_indexes = aux_func.index_lat_and_lon(lat_value, lon_value, lats_var, lons_var)
#print(cor_indexes[0])

#just to be more readable
print('')
print( 'Registered precipitation ->',  prec[0, cor_indexes[0], cor_indexes[1]], precipitation.units)
print('')
