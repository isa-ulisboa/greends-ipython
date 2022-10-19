f = open("GreenDSfile1.csv")
lst = f.readlines()
f.close()

fout = open("GreenDSfile1_sample.csv", "w")
for i in range(100):
    fout.writelines(lst[1])
fout.close()

# Delete a file?
import os
os.remove("GreenDSfile1_sample.csv")

# Counting lines
#   observe the different timings of execution

fp = open("GreenDSfile1.csv", "r")
x = len(fp.readlines())
print('Total lines:', x)
fp.close()

#netCDF4 project

import netCDF4 as nc
import xarray as xa
