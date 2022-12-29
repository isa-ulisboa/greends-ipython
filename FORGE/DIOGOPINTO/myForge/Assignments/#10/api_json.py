import netCDF4 as nc
import numpy as np
import myFunctions_10 as mf10
import json
import argparse
import sys

#Giving the arguments

parser = argparse.ArgumentParser()

parser.add_argument('--lat', type = float, required = True)
parser.add_argument('--lon', type = float, required = True)
parser.add_argument('--file', type = str, required = True)

args = parser.parse_args()

#netCDF dataset
ds= nc.Dataset(args.file)

#List of lat, lon, coordinates and precipitation
lat= ds.variables['lat']
lon= ds.variables['lon']
dry_NOXdep= ds.variables['DDEP_OXN_m2Grid']
wet_NOXdep = ds.variables['WDEP_OXN']
dry_RDNdep = ds.variables['DDEP_RDN_m2Grid']
wet_RDNdep = ds.variables['WDEP_RDN']

#Getting lat and lon array
lats= ds.variables['lat'][:]
lons= ds.variables['lon'][:]

#Nearest distance from Lat= 37.9 and Lon= -7.8
lats_index = mf10.nearest_coordinate(args.lat,lats)
lons_index = mf10.nearest_coordinate(args.lon,lons)

#Summing up the total of nitrogen deposition (mgN(m2))
total_n_d = dry_NOXdep[0, lats_index, lons_index] + wet_NOXdep[0, lats_index, lons_index] + dry_RDNdep[0, lats_index, lons_index] + wet_RDNdep[0, lats_index, lons_index]
print('Total Nitrogen Deposition:',round(total_n_d,2), dry_NOXdep.units)

#Converting to Kg/ha
tnd_conv= round(float(total_n_d/100),2)
print('Total Nitrogen Deposition',tnd_conv,'Kg/ha')

#Retrieve values
Retr_lat = round(float(lats[lats_index]),2)
Retr_lon = round(float(lons[lons_index]),2)

#Data in Json format
output= {
    "version": "0.1",
    "version_notes": "Exercise for Green DataScience. Data extracted from 2019 EMEP (www.emep.int) dataset EMEP01_rv4.42_year.2019met_2019emis.nc with 0.1 degrees resolution (approx 11.1 km) - Dry and wet deposition of oxidized and reduced N (DDEP_OXN_m2Grid + DDEP_RDN_m2Grid + WDEP_OXN + WDEP_RDN) converted from mgN m-2 to kg ha-1",
    "coordinate_requested": {
        "lon": args.lon,
        "lat": args.lat
    },
    "coordinate_retrieved": {
        "lon": Retr_lon,
        "lat": Retr_lat
    },
    "data": {
        "total_n_deposition": {
            "value": tnd_conv,
            "unit": "kg ha-1"
        }
    }
}

#Converting to json file
output= json.dumps(output,indent=4)
print(output)
print('---DONE---')