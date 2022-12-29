# Assignment 10
import netCDF4 as nc
import numpy as np
import json
import argparse
import myFunctions as func

# Definition of the arguments of the script 

parser = argparse.ArgumentParser()

parser.add_argument('--lat', type = float, required = True)
parser.add_argument('--lon', type = float, required = True)
parser.add_argument('--f', type = str, required = True)

args = parser.parse_args()

# Open the netCDF dataset object

ds = nc.Dataset(args.f)

# Access the information from the object ds

#print(ds.variables.keys())
#print(ds.dimensions) 
lat = ds.variables['lat']
lon = ds.variables['lon']
dry_OXNdep = ds.variables['DDEP_OXN_m2Grid']
wet_OXNdep = ds.variables['WDEP_OXN']
dry_RDNdep = ds.variables['DDEP_RDN_m2Grid']
wet_RDNdep = ds.variables['WDEP_RDN']

# Extract latitude and longitude values to numpy arrays

lat_np_array = ds.variables['lat'][:]
lon_np_array = ds.variables['lon'][:]

# Get the closest indexes from location Lat: 37.9, Lon: -7.8

lat_index = func.closest_index(args.lat, lat_np_array)
lon_index = func.closest_index(args.lon, lon_np_array)

#print("latitude:", lat_index, lat.units) 
#print("longitude:", lon_index, lon.units) 

#Latitude and Longitude retrieved

lat_retrieved = float(lat[lat_index])
lon_retrieved = float(lon[lon_index])

# Calculation of the Total nitrogen deposition (mgN/m2)

total_n_deposition = dry_OXNdep[0, lat_index, lon_index] + wet_OXNdep[0, lat_index, lon_index] + dry_RDNdep[0, lat_index, lon_index] + wet_RDNdep[0, lat_index, lon_index]
total_n_deposition = round(total_n_deposition, 2)
print(total_n_deposition, dry_OXNdep.units)

# Convertion of the total nitrogen deposition into kg ha-1

convertion = (total_n_deposition/100)
convertion = round(convertion, 2)
print(convertion, "kg ha-1")

# Data to be written in the json file 

data = {
    "version": "0.1",
    "version_notes":"Exercise for Green DataScience."
                    "Data extracted from 2019 EMEP (www.emep.int) dataset EMEP01_rv4.42_year.2019met_2019emis.nc"
                    "with 0.1 degrees resolution (approx 11.1 km) - Dry and wet deposition of oxidized and reduced N"
                    "(DDEP_OXN_m2Grid + DDEP_RDN_m2Grid + WDEP_OXN + WDEP_RDN) converted from mgN m-2 to kg ha-1",
    "coordinate_requested": {
        "lon": args.lat,
        "lat": args.lon
},
    "coordinate_retrieved": {
        "lon": lon_retrieved,
        "lat": lat_retrieved
    },
    "data": {
        "total_n_deposition": {
            "value": convertion,
            "unit": "kg ha-1"
        }
    }
}
 
# Serializing json, i.e., transformation of data into a series of bytes to be stored or transmitted across a network
json_object = json.dumps(data, indent=3) # To handle the data flow in a file, the JSON library in Python uses dump() or dumps() function to convert the Python objects into their respective JSON object
 
# Writing to ndeposition.json
with open("FORGE/BeatrizLucas/ndeposition_ex10.json", "w") as outfile:
    outfile.write(json_object)

print('done')

