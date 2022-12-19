# Load your NetCDF as before:
import netCDF4 as nc
import numpy as np
import json
import aux_func
fn = 'EMEP01_rv4.42_year.2019met_2019emis.nc' # update this path to your own file
ds = nc.Dataset(fn)

lats_var = ds.variables['lat'][:]
lons_var = ds.variables['lon'][:]
#Dry deposition of oxidized nitrogen per m2 grid 
n_dry_ox = ds.variables['DDEP_OXN_m2Grid'][:]
#Wet deposition of oxidized nitrogen --- WDEP_OXN
n_wet_ox = ds.variables['WDEP_OXN'][:]
#Dry deposition of reduced nitrogen per m2 grid --- DDEP_RDN_m2Grid
n_dry_red = ds.variables['DDEP_RDN_m2Grid'][:]
#Wet deposition of reduced nitrogen --- WDEP_RDN
n_wet_red = ds.variables['WDEP_RDN'][:]

#insert lat and long
lon_value = -7.80
lat_value = 37.95
#index calcullation
cor_indexes = aux_func.index_lat_and_lon(lat_value, lon_value, lats_var, lons_var)
lons_ret = round(lons_var[cor_indexes[1]], 3)
lats_ret = round(lats_var[cor_indexes[0]], 3)

# call for the variables assciated with the previuous calcullated indexes
n_dry_ox_val = n_dry_ox[:, cor_indexes[0], cor_indexes[1]]
n_wet_ox_val = n_wet_ox[:, cor_indexes[0], cor_indexes[1]]
n_dry_red_val = n_dry_red[:, cor_indexes[0], cor_indexes[1]]
n_wet_red_val = n_wet_red[:, cor_indexes[0], cor_indexes[1]]

#keep those values inside a list to facilitate the sum
n_values = [n_dry_ox_val, n_wet_ox_val, n_dry_red_val, n_wet_ox_val]

#sum of all the n values
n_total = sum(n_values)

#unit tranformation mg/m2 to kg/ha
#basically a factor of 1/100
n_total_kg_ha = n_total/100

#structure your output as json file
###notice that the coordinates retrived and requested and the variable type
###dont match with the ones in the assignment requirements
### 1)-> its due to the lons_var and lats_var being arrays popullated
###         with floats with many decimal cases, and once lat requested is 37.9
###         lats_ret is 37.85000000000011 it is closer to lat requested then
###         37.95000000000012 which is the assignement required
### 2)-> in the assignement output they are all string, but in mine they
###         they are majorly floats, 
data1 = {
    "version": "0.1",
    "version_notes": "Exercise for Green DataScience. Data extracted from 2019 EMEP (www.emep.int) dataset EMEP01_rv4.42_year.2019met_2019emis.nc with 0.1 degrees resolution (approx 11.1 km) - Dry and wet deposition of oxidized and reduced N (DDEP_OXN_m2Grid + DDEP_RDN_m2Grid + WDEP_OXN + WDEP_RDN) converted from mgN m-2 to kg ha-1",
    "coordinate_requested": {
        "lon": lon_value,
        "lat": lat_value
    },
    "coordinate_retrieved": {
        "lon": lons_ret,
        "lat": lats_ret
    },
    "data":{
        "total_n_deposition": {
            "value": float(n_total_kg_ha),
            "unit": "kg ha-1"}
        } }

#convert into JSON format
j_data = json.dumps(data1, indent=4)

#print them
print (j_data)




