# Load your NetCDF as before:
import netCDF4 as nc 
fn = 'EMEP01_rv4.42_year.2019met_2019emis.nc' # update this path to your own file
ds = nc.Dataset(fn)
#list of the lat, lon, coordinates and precipitation
lats = ds.variables['lat'][:]#85
lons = ds.variables['lon'][:]#202
time = ds.variables['time'][0]

###inLat: 38.568, inLon: -9.720

#the regular way that fail if the center of the center (origem em PT) of the grid changes

def indexlat (y):
    #yr = round(y, 2)
    iny = 10*y-300.5
    y_lat = (int(iny))
    return (y_lat)
#indexlat(38.568)

def indexlon (y):
    iny = 10*y+299.5
    y_lon = (int(iny))
    return (y_lon)
#indexlon(-9.720)

######################
#beatriz code triggred me
#i believe that  this method can applied to different grids
#even if the center of the grid changes it won't affect the function reliability
#i believe but im not 100% sure because i did not have a differnt one to test
######################

def indexlat2 (y):
    m = lats[1]-lats[0]
    m_rv = round(1/m)
    inx = m_rv*(y-lats[0])
    y_lat = (int(inx))
    return (y_lat)
#print(indexlat2(38.568))

def indexlon2 (x):
    m = lons[1]-lons[0]
    m_rv = round(1/m)
    in_x = m_rv*(x-lons[0])
    y_lat = (int(in_x))
    return (y_lat)
#print(indexlon2(-9.720))