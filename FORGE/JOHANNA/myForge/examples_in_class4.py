# make a sample file with the first 1000
f = open("GreenDSfile1.csv")
lst = f.readlines()
f.close() # if opening a file into an object, always close it- otherwise it will stay open.


fout = open("GreenDSfile1_sample.csv", "w")
for i in range(100):
    fout.writelines(lst[i])
fout.close()

# count lines
fp = open("GreenDSfile1.csv", 'r')
x = len(fp.readlines())
fp.close()
print("Total lines:", x)

# using csv modules
# NOTE: only for big files (bigger than memory of computer)

#netCDF4
import netCDF4 as nc


