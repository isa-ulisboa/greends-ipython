#open file

import sys
f = open("GreenDSfile1.csv")

# count number of lines

x = len(f.readlines())
print('Total lines', x)
f.close()

# open the original file and list first 500k lines

f1 = open("GreenDSfile1.csv")
lst1 = f1.readlines()
f1.close()

# create a file to store the 500k lines

fout1 = open("GreenDSfile1_sample500k.csv","w")
for i in range(500000):
    fout1.writelines(lst1[i])
fout1.close()

# open original file and list the last 100 lines

f2 = open("GreenDSfile1.csv")
lst2 = f2.readlines()[-100:]
f2.close()

# create a the file to store the last 100 lines

fout2 = open("GreenDSfile1_samplelast100.csv","w")
for i in range(100):
    fout2.writelines(lst2[i])
fout2.close()