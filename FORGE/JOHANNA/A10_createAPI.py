# Load your NetCDF as before:
import netCDF4 as nc 
import numpy as np
import json
import sys
import argparse

### Section start - PIECE OF CODE TO HANDLE THE ARGUMENTS
args = sys.argv
if len(args)== 4:
    print(args)
    lat = float(args[1])
    lon = float(args[2])
    file = str(args[3])

if len(args)==7:
    parser = argparse.ArgumentParser()
    parser.add_argument("-lat", "--lat", required=True)
    parser.add_argument("-lon","--lon", required=True)
    parser.add_argument('-f','--file', required=True)
    args = parser.parse_args()
    print(args)

    lat = float(args.lat)
    lon = float(args.lon)
    file = str(args.file)

### Section end - PIECE OF CODE TO HANDLE THE ARGUMENTS

ds = nc.Dataset(file)

### you can copy code from your previous assignment and adapt your Lat, Lon and NetCDF file to become variables 
#list of the lat, lon, coordinates and precipitation
lats = ds.variables['lat'][:]
lons = ds.variables['lon'][:]
dry_NOXdep = ds.variables['DDEP_OXN_m2Grid']
dry_NRDdep = ds.variables['DDEP_RDN_m2Grid']
wet_NOXdep = ds.variables['WDEP_OXN']
wet_NRDdep = ds.variables['WDEP_RDN']

# Retrieve indexes of coordinates values for the location near Beja, with Lat: 37.9, Lon: -7.8
indexLat = np.absolute(lats-lat).argmin()
indexLon = np.absolute(lons-lon).argmin()

# retrieve values
outLat = round(lats[indexLat],2)
outLon = round(lons[indexLon],2)
dNox = dry_NOXdep[:,indexLat, indexLon]
dNrd = dry_NRDdep[:,indexLat, indexLon]
wNox = wet_NOXdep[:,indexLat, indexLon]
wNrd = wet_NRDdep[:,indexLat, indexLon]

# sum them up and convert it to Kg/ha from mg/m2
total_N_dep = dNox + dNrd + dNox+ wNrd
total_N_dep = round(float(total_N_dep) * 0.01,2)

# generate dict
out = {
    "version": "0.1",
    "version_notes": "Exercise for Green DataScience. Data extracted from 2019 EMEP (www.emep.int) dataset EMEP01_rv4.42_year.2019met_2019emis.nc with 0.1 degrees resolution (approx 11.1 km) - Dry and wet deposition of oxidized and reduced N (DDEP_OXN_m2Grid + DDEP_RDN_m2Grid + WDEP_OXN + WDEP_RDN) converted from mgN m-2 to kg ha-1",
    "coordinate_requested": {
        "lon": lon,
        "lat": lat
    },
    "coordinate_retrieved": {
        "lon": outLon,
        "lat": outLat
    },
    "data": {
        "total_n_deposition": {
            "value": total_N_dep,
            "unit": "kg ha-1"
        }
    }
}

# convert to json file
out = json.dumps(out, indent=4)
print(out)