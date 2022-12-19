import numpy as np

def nearest_index(x_value, x_array):
    """_summary_

        Calculation of the nearest index that a given longitude or latitude corresponds in the NetCDF grid.

        Args:
        x_value (float): longitude or latitude given values 
        x_array (array): array of the values of longitude or latitude extract from the NetCDF file 

    Returns:
        _type_: nearest index of the coordinate found in the x_array
    """

    nearest_idx = (np.abs(x_array - x_value)).argmin()
    
    return nearest_idx


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