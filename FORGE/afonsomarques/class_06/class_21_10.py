###import netCDF4 as nc 
#### Download netCDFFile file from https://emep.int/mscw/mscw_moddata.html
#### also has a description of the variables
###fn = 'FORGE/afonsomarques/class_06/dataset-sis-agrometeorological-indicators-109ad28e-cf81-4870-886c-bfc24fbc7d53/109ad28e-cf81-4870-886c-bfc24fbc7d53-Solar-Radiation-Flux_C3S-glob-agric_AgERA5_20210301_final-v1_area_subset.nc'
###ds = nc.Dataset(fn)
###print(ds) # Peeking the contents


# Another way to read and Make a quick map to see it
import xarray as xr

emep = xr.open_dataset('FORGE/afonsomarques/class_06/dataset-sis-agrometeorological-indicators-109ad28e-cf81-4870-886c-bfc24fbc7d53/109ad28e-cf81-4870-886c-bfc24fbc7d53-Solar-Radiation-Flux_C3S-glob-agric_AgERA5_20210301_final-v1_area_subset.nc')

#print(emep)
prec = emep.solar_radiation_flux
#print(prec)
precgrid = prec.isel(time=0)# select one layer (there is only one layer (yearly value)

precgrid.plot(figsize=[20,10]) # set some properties to plot
precgrid.plot() # display it

# extract the value from a grid coordinate
precloc = precgrid.isel(lat=10, lon=10).values #note this is the index of the grid and not geografic coordinates
print (precloc)