# Open GreenDSfile1.csv 
import sys

f = open("GreenDSfile1.csv")
f.close()

# Couting and printing lines

fp = open("GreenDSfile1.csv", "r")
x = len(fp.readlines())
print("Total lines:", x)
fp.close()

# Creating new files

f1 = open("GreenDSfile1.csv")
lst1 = f1.readlines()
f1.close()

fout1 = open("GreenDSfile1_sample500k.csv", "w")
for i in range(500000):
    fout1.writelines(lst1[i])
fout1.close()

f2 = open("GreenDSfile1.csv")
lst2 = f2.readlines()[-100:]
f2.close()

fout2 = open("GreenDSfile1_samplelast100.csv", "w")
for i in range(100):
    fout2.writelines(lst2[i])
fout2.close()

