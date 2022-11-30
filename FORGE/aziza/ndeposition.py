# Load your NetCDF as before:
import netCDF4 as nc 
import json
#Consider our file EMEP01_rv4.42_year.2019met_2019emis.nc
fn_1 = "EMEP01_rv4.42_year.2019met_2019emis.nc" 
ds = nc.Dataset(fn_1)
#list of the lat, lon, coordinates and precipitation
#Dry deposition of oxidized nitrogen per m2 grid --- DDEP_OXN_m2Grid
#Wet deposition of oxidized nitrogen --- WDEP_OXN
#Dry deposition of reduced nitrogen per m2 grid --- DDEP_RDN_m2Grid
#Wet deposition of reduced nitrogen --- WDEP_RDN
#Precipitation --- WDEP_PREC
lats = ds.variables['lat'][:]
lons = ds.variables['lon'][:]
dry_NOXdep = ds.variables['DDEP_OXN_m2Grid']
wet_NOXdep= ds.variables ['WDEP_OXN']
dry_NRDdep = ds.variables['DDEP_RDN_m2Grid']
wet_NRDdep= ds.variables ['WDEP_RDN']
prec = ds.variables['WDEP_PREC']
# element to which nearest value is to be found
Lats1 = 37.9
Lons1 = -7.8
coordinate_requested1= (Lats1,Lons1)
print (coordinate_requested1)
# find the index of minimum element from the array
import myfunctions as f
lats_index = f.nearest_index(Lats1, lats)
print (lats_index)
lons_index = f.nearest_index(Lons1, lons)
print (lons_index)
coordinate_retrived1=(lats[lats_index],lons[lons_index])
lats_retrived=lats[lats_index]
lons_retrived=lons[lons_index]
# get the element that correspond those index
dry_NOXdep_1=dry_NOXdep[:,lats_index, lons_index]
print (dry_NOXdep_1)
wet_NOXdep_1=wet_NOXdep[:,lats_index, lons_index]
print (wet_NOXdep_1)
dry_NRDdep_1=dry_NRDdep[:,lats_index, lons_index]
print (dry_NRDdep_1)
wet_NRDdep_1=wet_NRDdep[:,lats_index, lons_index]
print (wet_NRDdep_1)
# total nitrogen 
nitrogen= dry_NOXdep_1+wet_NOXdep_1+dry_NRDdep_1+wet_NRDdep_1
print(nitrogen)
#conversion 
nitrogen_1= nitrogen/100
print (nitrogen_1)
# json format 
# a Python object (dict):

data1 = {
    "version": "0.1",
    "version_notes": "Exercise for Green DataScience. Data extracted from 2019 EMEP (www.emep.int) dataset EMEP01_rv4.42_year.2019met_2019emis.nc with 0.1 degrees resolution (approx 11.1 km) - Dry and wet deposition of oxidized and reduced N (DDEP_OXN_m2Grid + DDEP_RDN_m2Grid + WDEP_OXN + WDEP_RDN) converted from mgN m-2 to kg ha-1",
    "coordinate_requested": {
        "lon": Lons1,
        "lat": Lats1
    },
    "coordinate_retrieved": {
        "lon": lons_retrived,
        "lat": lats_retrived
    },
    "data":{
        "total_n_deposition": {
            "value": float(nitrogen_1),
            "unit": "kg ha-1"}
        } }
# convert into JSON:
j_data = json.dumps(data1)
print (j_data)
