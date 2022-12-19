import numpy as np

def index_lat_and_lon (y, x, lats, lons):
    
    ######for lat
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