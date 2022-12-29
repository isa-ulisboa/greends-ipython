import netCDF4 as nc 
import json
fn = 'EMEP01_rv4.42_year.2019met_2019emis.nc'
import Assignment8 as a8

ds = nc.Dataset(fn)

#Valores de lats, lons, dry and wet, oxidized and reduced nitrogen
lats = ds.variables['lat'][:]
lons = ds.variables['lon'][:]
dry_NOXdep = ds.variables['DDEP_OXN_m2Grid'] [:]
dry_NRdep = ds.variables['DDEP_RDN_m2Grid'] [:]
wet_NRdep = ds.variables['WDEP_RDN'] [:]
wet_NOXdep = ds.variables['WDEP_OXN'] [:]

# Obter index mais próximo para Lat= 37.9 e Lon= -7.8
lats1 = 37.9
lons1 = -7.8
coordinate_requested= (lats1,lons1)
#print (coordinate_requested1)

# Coordenadas mais próximas para Lat: 37.9, Lon: -7.8

lats_index = a8.nearest_coordinate(lats1, lats)
#print (lats_index)
lons_index = a8.nearest_coordinate(lons1, lons)
#print (lons_index)
coordinate_retrived=(lats[lats_index],lons[lons_index])
lats_retrived=lats[lats_index]
lons_retrived=lons[lons_index]

# Obter valores que correspondem a esses index

dry_NOXdep_1=dry_NOXdep[:,lats_index, lons_index]
#print (dry_NOXdep_1)
wet_NOXdep_1=wet_NOXdep[:,lats_index, lons_index]
#print (wet_NOXdep_1)
dry_NRdep_1=dry_NRdep[:,lats_index, lons_index]
#print (dry_NRdep_1)
wet_NRdep_1=wet_NRdep[:,lats_index, lons_index]
#print (wet_NRdep_1)

# Azoto total
nitrogen= dry_NOXdep_1+wet_NOXdep_1+dry_NRdep_1+wet_NRdep_1
print(nitrogen)

#Conversão de unidades
nitrogen_1= nitrogen*0.01
print (nitrogen_1)

# Data para ser escrita em Formato JSON

data = {
    "version": "0.1",
    "version_notes": "Exercise for Green DataScience. Data extracted from 2019 EMEP (www.emep.int) dataset EMEP01_rv4.42_year.2019met_2019emis.nc with 0.1 degrees resolution (approx 11.1 km) - Dry and wet deposition of oxidized and reduced N (DDEP_OXN_m2Grid + DDEP_RDN_m2Grid + WDEP_OXN + WDEP_RDN) converted from mgN m-2 to kg ha-1",

    "coordinate_requested": {
        "lon": lons1,
        "lat": lats1
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
# Converter para JSON
json_data = json.dumps(data)
print (json_data)

