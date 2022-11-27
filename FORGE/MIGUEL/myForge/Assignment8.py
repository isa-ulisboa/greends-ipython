# Load your NetCDF as before:
import numpy as np 
import netCDF4 as nc 
fn = 'EMEP01_rv4.42_year.2019met_2019emis.nc' # update this path to your own file
ds = nc.Dataset(fn)
#list of the lat, lon, coordinates and precipitation
lats = ds.variables['lat'][:]
lons = ds.variables['lon'][:]
prec = ds.variables['WDEP_PREC'][:]

#Função para calcular coordenada mais próxima
def nearest_coordinate(x_value, x_array):
    nearest_c = (np.abs(x_array - x_value)).argmin()
    
    return nearest_c

#Coordenadas mais próximas para inLat: 38.568, inLon: -9.720
lat_index = nearest_coordinate(38.568, lats)
lon_index = nearest_coordinate(-9.720, lons)

#Obter valores
print(lon_index) #202
print(lat_index) #85

#Obter precipitação
print(prec[0, lat_index, lon_index]) #392.64078

