# Assignment 9

import netCDF4 as nc
import json
import myFunctions as mf

# First we need a path to the netcdf file

fn = '../../EMEP01_rv4.42_year.2019met_2019emis.nc'
ds = nc.Dataset(fn)

# List of the lat, lon, coordinates and precipitation

lats = ds.variables['lat'][:]
lons = ds.variables['lon'][:]

"""
Name of the layers in the NetCDF for the dry and wet, oxidized and reduced nitrogen:
- Dry deposition of oxidized nitrogen per m2 grid --- DDEP_OXN_m2Grid
- Dry deposition of reduced nitrogen per m2 grid --- DDEP_RDN_m2Grid
- Wet deposition of oxidized nitrogen --- WDEP_OXN
- Wet deposition of reduced nitrogen --- WDEP_RDN
"""

dry_NOXdep = ds.variables['DDEP_OXN_m2Grid']
dry_NRDdep = ds.variables['DDEP_RDN_m2Grid']
wet_NOXdep = ds.variables['WDEP_OXN']
wet_NRDdep = ds.variables['WDEP_RDN']

# Retrieve those, sum them up and convert it to Kg/ha, for the location near Beja, with Lat: 37.9, Lon: -7.8

inLat = 37.9
ind_Lat = mf.geo_idx(37.9, lats)
inLon = -7.8
ind_Lon = mf.geo_idx(-7.8, lons)

output_lat = round(lats[ind_Lat], 2)
output_lon = round(lons[ind_Lon], 2)
DNOX = dry_NOXdep[:, ind_Lat, ind_Lon]
DNRD = dry_NRDdep[:, ind_Lat, ind_Lon]
WNOX = wet_NOXdep[:, ind_Lat, ind_Lon]
WNRD = wet_NRDdep[:, ind_Lat, ind_Lon]

# Sum of all layers
dep_N = DNOX + DNRD + WNOX + WNRD

# Convert result to kg/ha

dep_N = (float(dep_N)*0.01)

# Create a dictionary of data you wish to expose before serializing to JSON

output = {
    "version": "0.1",
    "version_notes": "Exercise for Green DataScience. Data extracted from 2019 EMEP (www.emep.int) dataset EMEP01_rv4.42_year.2019met_2019emis.nc with 0.1 degrees resolution (approx 11.1 km) - Dry and wet deposition of oxidized and reduced N (DDEP_OXN_m2Grid + DDEP_RDN_m2Grid + WDEP_OXN + WDEP_RDN) converted from mgN m-2 to kg ha-1",
    "coordinate_requested": {
        "lon": "-7.80",
        "lat": "37.90"
    },
    "coordinate_retrieved": {
        "lon": "-7.85",
        "lat": "37.95"
    },
    "data": {
        "total_n_deposition": {
            "value": "2.6",
            "unit": "kg ha-1"
        }
    }
}

# We want to output a json with the Nitrogen deposition in Kg/ha and some metadata; json.dumps() function will convert a subset of Python objects into a json string

jsonFile = json.dumps(output, indent=3)
print(jsonFile)