
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

### to get the cordinate indexes its a simple regression
### y=mx+b where x the desired value



def index_lat_and_lon (y, x, lats, lons):
    
    #####for lat
    m = lats[1]-lats[0]
    m_rv = round(1/m)
    inx = m_rv*(y-lats[0])
    y_lat = (int(inx))
    ######for lon
    m1 = lons[1]-lons[0]
    m1_rv = round(1/m1)
    in_x = m1_rv*(x-lons[0])
    x_lat = (int(in_x))
    return (y_lat, x_lat)
#print(indexlat2(38.568))
