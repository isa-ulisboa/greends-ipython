import netCDF4 as nc
import numpy as np
import json
import argparse
import myFunctions as mf
fn = "EMEP01_rv4.42_year.2019met_2019emis.nc"

parser = argparse.ArgumentParser()

parser.add_argument("--lat", type= float, required=True, help= "Latitude do local a ser estudado, (--lat)" )
parser.add_argument("--lon", type=float, required=True, help= "Longitude do local a ser estudado, (--lon)")
parser.add_argument("--fn", type=str, required=True, help="Nome do ficheiro dos dados a utilizar ,(--fn)")

args = parser.parse_args()

ds = nc.Dataset(args.fn)

# from ndeposition.py file

### List of the Lat, Lon, coordinates and precipitation

lats = ds.variables["lat"][:]
lons = ds.variables["lon"][:]


dry_NOXdep = ds.variables["DDEP_OXN_m2Grid"][:]
dry_NOXdep_info = ds.variables["DDEP_OXN_m2Grid"]
wet_NOXdep = ds.variables["WDEP_OXN"][:]
Ox_Ndep = ds.variables["DDEP_OXN_m2Grid"][:]
reduced_Ndep = ds.variables["DDEP_RDN_m2Grid"][:]

### print(dry_NOXdep_info)

lon_id = mf.obtain_index(args.lon, lons)
lat_id = mf.obtain_index(args.lat, lats)

lat_coord = lats[lat_id]
lon_coord = lons[lon_id]

lon_val = args.lon
lat_val = args.lat

N_dep_total = round((dry_NOXdep[0, lat_id, lon_id] + wet_NOXdep[0, lat_id, lon_id] + Ox_Ndep[0, lat_id, lon_id] + reduced_Ndep[0, lat_id, lon_id])/100, 3)

# print("The total N deposited in the soil is: ", N_dep_total, "Kg/ha.")


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

json_dump_2 = json.dumps(N_calc_func, indent=4)

with open("FORGE/LUISSOARES/ndeposition_ex10.json", "w") as dump_file_2:
    dump_file_2.write(json_dump_2)

print("Success..!")