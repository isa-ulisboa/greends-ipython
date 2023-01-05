#assignment 9

import netCDF4 as nc 
import json
import myFunctions as mf

fn =(r'C:/Users/gast/Documents/LISSABON/IP/greends-ipython/EMEP01_rv4.42_year.2019met_2019emis.nc')

ds = nc.Dataset(fn)

#list of the lat, lon, coordinates
lats = ds.variables['lat'][:]
lons = ds.variables['lon'][:]

# name of the layers in the NetCDF for the dry and wet, oxidized and reduced nitrogen
#   DDEP_OXN_m2Grid: dry deposition of oxidized nitrogen per m2 grid
#   DDEP_RDN_m2Grid: dry deposition of reduced nitrogen per m2 grid  
#   WDEP_OXN: Wet deposition of oxidized nitrogen  
#   WDEP_RDN: Wet deposition of reduced nitrogen  

dry_NOXdep = ds.variables['DDEP_OXN_m2Grid'] 
dry_NRDdep = ds.variables['DDEP_RDN_m2Grid']
wet_NOXdep = ds.variables['WDEP_OXN']
wet_NRDdep = ds.variables['WDEP_RDN']


# location near Beja, with Lat: 37.9, Lon: -7.8

inLat = 37.9
inLon = -7.8
index_lat = mf.geo_index(inLat, lats)
index_lon = mf.geo_index(inLon, lons)
outLat = round(lats[index_lat],2)
outLon = round(lons[index_lon],2)

# Retrieve nitrogen-values for this location 

dryNox = dry_NOXdep[:,index_lat, index_lon]
dryNrd = dry_NRDdep[:,index_lat, index_lon]
wetNox = wet_NOXdep[:,index_lat, index_lon]
wetNrd = wet_NRDdep[:,index_lat, index_lon]

#sum them up and convert from mg/m2 to kg/ha

N_deposition = dryNox + dryNrd + wetNox + wetNrd 
N_depositionconverted = round(float(N_deposition)*0.01, 2) 

# data as the json file 


out = {
    "version": "0.1",
    "version_notes": "Exercise for Green DataScience. Data extracted from 2019 EMEP (www.emep.int) dataset EMEP01_rv4.42_year.2019met_2019emis.nc with 0.1 degrees resolution (approx 11.1 km) - Dry and wet deposition of oxidized and reduced N (DDEP_OXN_m2Grid + DDEP_RDN_m2Grid + WDEP_OXN + WDEP_RDN) converted from mgN m-2 to kg ha-1",
    "coordinate_requested": {
        "lon": inLon,
        "lat": inLat
    },
    "coordinate_retrieved": {
        "lon": outLon,
        "lat": outLat
    },
    "data": {
        "total_n_deposition": {
            "value": N_depositionconverted,
            "unit": "kg ha-1"
        }
    }
}

json_ndep = json.dumps(out, indent=3)
print(json_ndep)
