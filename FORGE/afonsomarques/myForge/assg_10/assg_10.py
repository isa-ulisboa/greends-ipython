
import netCDF4 as nc
import json
import sys
import aux_func
import argparse
import glob

    #list all files with the corresponding file type 
nc_files = glob.glob('*.nc')

    #define the  arguments
parser = argparse.ArgumentParser()
parser.add_argument('--lat', type = float, required = True)
parser.add_argument('--lon', type = float, required = True)
parser.add_argument('--file', type = str, required = True)

args = parser.parse_args()

    #try to ensure the vallidity of the file
try:
    ds = nc.Dataset(args.file)
        #read the lats and lons from the file previouly listed 
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


        #if clause to define the possible values for lattitude
    if float(args.lat) >= lats_var[0] and float(args.lat) <= lats_var[-1]:
        cor_indexes = aux_func.index_lat_and_lon(args.lat, args.lon, lats_var, lons_var)
        lats_ret = round(lats_var[cor_indexes[0]], 3)
    else:
        print('')
        print('-> invalid lattitude')
        print ("--> lattitude value must be between", lats_var[0], 'and',lats_var[-1])
        print('')
        sys.exit()


        #if clause to define the possible values for longitude
    if float(args.lon) >= lons_var[0] and float(args.lon) <= lons_var[-1]:
        #cor_indexes = aux_func.index_lat_and_lon(args.lat, args.lon, lats_var, lons_var)
        lons_ret = round(lons_var[cor_indexes[1]], 3)
    else:
        print('')
        print('-> invalid longitude')
        print ("--> longitude value must be between", lons_var[0] , 'and', lons_var[-1])
        print('')
        sys.exit()

        
        #if clause to compute the the n deposition for a set of coordinataes
    if args.file in nc_files:
        #index calcullation
        cor_indexes = aux_func.index_lat_and_lon(args.lat, args.lon, lats_var, lons_var)
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
        data1 = {
            "version": "0.1",
            "version_notes": "Exercise for Green DataScience. Data extracted from 2019 EMEP (www.emep.int) dataset EMEP01_rv4.42_year.2019met_2019emis.nc with 0.1 degrees resolution (approx 11.1 km) - Dry and wet deposition of oxidized and reduced N (DDEP_OXN_m2Grid + DDEP_RDN_m2Grid + WDEP_OXN + WDEP_RDN) converted from mgN m-2 to kg ha-1",
            "coordinate_requested": {
                "lon": args.lon,
                "lat": args.lat
            },
            "coordinate_retrieved": {
                "lon": lons_ret,
                "lat": lats_ret
            },
            "data":{
                "total_n_deposition": {
                    "value": float(n_total_kg_ha),
                    "unit": "kg ha^-1"}
                } }
        #convert into JSON format
        j_data = json.dumps(data1, indent=4)
        #print them
        print (j_data)
        print('')
        print ('--- CONGRATULATIONS YOU HAVE DONE YOUR TASK ---')
        print('')

except FileNotFoundError:
    print('')
    print("--- CAN YOU PLEASE INSERT AN EXISTING DATASET? ---")
    print('')
    print ('--> currently existing dataset(s):', nc_files)
    print('')




