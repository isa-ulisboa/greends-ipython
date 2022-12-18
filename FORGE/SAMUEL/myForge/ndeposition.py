#Assignment 9

import netCDF4 as nc 
import numpy as np
import json
import myFunctions as mf

fn = 'EMEP01_rv4.42_year.2019met_2019emis.nc'  # update this path to your own file

ds = nc.Dataset(fn)

#imput 
in_lat = 37.9
in_lon = -7.8
lats = ds.variables['lat'][:]
lons = ds.variables['lon'][:]
dry_OXNdep = ds.variables['DDEP_OXN_m2Grid'][:]   #Dry deposition of oxidized nitrogen per m2 grid (pagina emep)
dry_RDNdep = ds.variables['DDEP_RDN_m2Grid'][:]   #Dry deposition of reduced nitrogen per m2 grid (pagina emep)
wet_OXNdep = ds.variables['WDEP_OXN'][:]          #wet deposition of oxidized nitrogen (pagina emep)
wet_RDNdep = ds.variables['WDEP_RDN'][:]         #wet deposition of reduced nitrogen (pagina emep)


lat_index = mf.nearest_index(37.9, lats)
lon_index = mf.nearest_index(-7.8, lons)

nearest_lat = lats[lat_index]
nearest_lon = lons[lon_index]

def calculate_deposition (fn, nearest_lat , nearest_lon ): #assignment 10


    d1 = dry_OXNdep[0, lat_index, lon_index]   #d de dry
    d2 = dry_RDNdep[0, lat_index, lon_index]
    w1 = wet_OXNdep[0, lat_index, lon_index]    #w de wet
    w2 = wet_RDNdep[0, lat_index, lon_index]

    nitrogen = d1+d2+w1+w2
    print (nitrogen)

    #conversão unidades
    final_nitrogen = nitrogen/100

    return (final_nitrogen)

a = {
    "version": "0.1",
    "version_notes": "Exercise for Green DataScience. Data extracted from 2019 EMEP (www.emep.int) dataset EMEP01_rv4.42_year.2019met_2019emis.nc with 0.1 degrees resolution (approx 11.1 km) - Dry and wet deposition of oxidized and reduced N (DDEP_OXN_m2Grid + DDEP_RDN_m2Grid + WDEP_OXN + WDEP_RDN) converted from mgN m-2 to kg ha-1",
    "coordinate_requested": {
        "lon": in_lon,
        "lat": in_lat
    },
    "coordinate_retrieved": {
        "lon": nearest_lon,
        "lat": nearest_lat
    },
    "data": {
        "total_n_deposition": {
            "value": calculate_deposition(fn, nearest_lat, nearest_lon),
            "unit": "kg ha-1"
        }
    }
}

with open ("assignemtn9.json", "w") as f:
    b=json.dumps(a)
    json.dump(b,f)

