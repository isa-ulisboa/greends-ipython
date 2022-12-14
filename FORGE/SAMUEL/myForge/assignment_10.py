import netCDF4 as nc 
import numpy as np
import json
import sys
import myFunctions as mf
import ndeposition

lat = sys.argv[2]
print(lat)

lon = sys.argv[4]

file_name = sys.argv[6]

ds = nc.Dataset(file_name)

lats = ds.variables['lat'][:]
lons = ds.variables['lon'][:]

lat_index = mf.nearest_index(37.9, lats)
lon_index = mf.nearest_index(-7.8, lons)

nearest_lat = lats[lat_index]
nearest_lon = lons[lon_index]

dry_OXNdep = ds.variables['DDEP_OXN_m2Grid'][:]   #Dry deposition of oxidized nitrogen per m2 grid (pagina emep)
dry_RDNdep = ds.variables['DDEP_RDN_m2Grid'][:]   #Dry deposition of reduced nitrogen per m2 grid (pagina emep)
wet_OXNdep = ds.variables['WDEP_OXN'][:]          #wet deposition of oxidized nitrogen (pagina emep)
wet_RDNdep = ds.variables['WDEP_RDN'][:]         #wet deposition of reduced nitrogen (pagina emep)

d1 = dry_OXNdep[0, lat_index, lon_index]   #d de dry
d2 = dry_RDNdep[0, lat_index, lon_index]
w1 = wet_OXNdep[0, lat_index, lon_index]    #w de wet
w2 = wet_RDNdep[0, lat_index, lon_index]

ndeposition.

a = {
    "version": "0.1",
    "version_notes": "Exercise for Green DataScience. Data extracted from 2019 EMEP (www.emep.int) dataset EMEP01_rv4.42_year.2019met_2019emis.nc with 0.1 degrees resolution (approx 11.1 km) - Dry and wet deposition of oxidized and reduced N (DDEP_OXN_m2Grid + DDEP_RDN_m2Grid + WDEP_OXN + WDEP_RDN) converted from mgN m-2 to kg ha-1",
    "coordinate_requested": {
        "lon": lat,
        "lat": lon
    },
    "coordinate_retrieved": {
        "lon": nearest_lon,
        "lat": nearest_lat
    },
    "data": {
        "total_n_deposition": {
            "value": final_nitrogen,
            "unit": "kg ha-1"
        }
    }
}

with open ("assignemtn9.json", "w") as f:
    b=json.dumps(a)
    json.dump(b,f)
