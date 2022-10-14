f = open("GreenDSfile1.csv")
lst = f.readlines()
f.close()

fout = open("GreenDSfile1_sample.csv","w")
for i in range(100):
    fout.writelines(lst[1])
fout.close()

import os

os.remove("GreenDSfile1_sample.csv")

fp = open("GreenDSfile1.csv", 'r')
x = len(fp.readlines())
print('Total lines:', x)
fp.close()