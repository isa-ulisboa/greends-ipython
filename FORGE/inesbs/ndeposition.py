# Load your NetCDF as before:
import netCDF4 as nc 
import json
import myfunctions as mf

fn = (r'c:/Users/inesb/.ipython/greends-ipython/EMEP01_rv4.42_year.2019met_2019emis.nc')

ds = nc.Dataset(fn)

#list of the lat, lon, coordinates and precipitation
lats = ds.variables['lat'][:]
lons = ds.variables['lon'][:]
dry_NOXdep = ds.variables['DDEP_OXN_m2Grid'] 

# names os layers
# Wet deposition of oxidized nitrogen --- WDEP_OXN
# dry deposition of reduced nitrogen per m2 grid --- DDEP_RDN_m2Grid
# Wet deposition of reduced nitrogen --- WDEP_RDN

dry_NRDdep = ds.variables['DDEP_RDN_m2Grid']
wet_NOXdep = ds.variables['WDEP_OXN']
wet_NRDdep = ds.variables['WDEP_RDN']

# indexes of coordinates values for the location near Beja
inLat = 37.9
inLon = -7.8
index_lat = mf.geo_index(37.9, lats)
index_lon = mf.geo_index(-7.8, lons)

# retrieve values
outLat = round(lats[index_lat],2)
outLon = round(lons[index_lon],2)
dryNox = dry_NOXdep[:,index_lat, index_lon]
dryNrd = dry_NRDdep[:,index_lat, index_lon]
wetNox = wet_NOXdep[:,index_lat, index_lon]
wetNrd = wet_NRDdep[:,index_lat, index_lon]
   
N_deposition = dryNox + dryNrd + wetNox+ wetNrd #sum all values to get total N_deposition
N_deposition = (float(N_deposition)*0.01) #convert mg/m2 to kg/ha

# generate dict
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
            "value": N_deposition,
            "unit": "kg ha-1"
        }
    }
}

# convert to json file
json_file = json.dumps(out, indent=3)
print(json_file)
