import netCDF4 as nc
import numpy as np
import json
import myFunctions as mf
fn = "EMEP01_rv4.42_year.2019met_2019emis.nc"

ds = nc.Dataset(fn)

# List of the Lat, Lon, coordinates and precipitation

lats = ds.variables["lat"][:]
lons = ds.variables["lon"][:]

dry_NOXdep = ds.variables["DDEP_OXN_m2Grid"][:]
dry_NOXdep_info = ds.variables["DDEP_OXN_m2Grid"]
wet_NOXdep = ds.variables["WDEP_OXN"][:]
Ox_Ndep = ds.variables["DDEP_OXN_m2Grid"][:]
reduced_Ndep = ds.variables["DDEP_RDN_m2Grid"][:]

#print(dry_NOXdep_info)

lon_id = mf.obtain_index(-7.8, lons)
lat_id = mf.obtain_index(37.9, lats)

lat_coord = lats[lat_id]
lon_coord = lons[lon_id]

N_dep_total = round((dry_NOXdep[0, lat_id, lon_id] + wet_NOXdep[0, lat_id, lon_id] + Ox_Ndep[0, lat_id, lon_id] + reduced_Ndep[0, lat_id, lon_id])/100, 3)

print("The total N deposited in the soil is: ", N_dep_total, "Kg/ha.")


# x = dry_NOXdep[0, lat_id, lon_id]
# print(x)
#print(lat_coord)
#print(lon_coord)


# print(dry_NOXdep)
# print(ds["time"][:])

lat_val = 37.9
lon_val = -7.8

## JSON file

N_calc_func = {
    "version": "0.1",
    "version_notes": "Exercise for Green DataScience. Data extracted from 2019 EMEP (www.emep.int) dataset EMEP01_rv4.42_year.2019met_2019emis.nc with 0.1 degrees resolution (approx 11.1 km) - Dry and wet deposition of oxidized and reduced N (DDEP_OXN_m2Grid + DDEP_RDN_m2Grid + WDEP_OXN + WDEP_RDN) converted from mgN m-2 to kg ha-1",
    "coordinate_requested": {
        "lon": lon_val,
        "lat": lat_val
    },
    "coordinate_retrieved": {
        "lon": lons[lon_id],
        "lat": lats[lat_id]
    },
    "data": {
        "total_n_deposition": {
            "value": round((dry_NOXdep[0, lat_id, lon_id] + wet_NOXdep[0, lat_id, lon_id] + Ox_Ndep[0, lat_id, lon_id] + reduced_Ndep[0, lat_id, lon_id])/100, 3),
            "unit": "kg ha-1"
        }
    }
}

json_dump = json.dumps(N_calc_func, indent=4)

with open("FORGE/LUISSOARES/ndeposition.json", "w") as dump_file:
    dump_file.write(json_dump)

print("Success :)")