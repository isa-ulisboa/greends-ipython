# Open a File
import sys

# Counting and printing lines
fp= open("GreenDSfile1.csv","r")
x = len(fp.readlines())
print("total lines", x)

# Creating New Files:
# 500000 lines

f1 = open('GreenDSfile1.csv')
lst1=f1.readlines()

ft1= open('GreenDSfile1_sample500k.csv','w')
for i in range(500000):
    ft1.writelines(lst1[i])

  ##Last 100 lines
f2= open('GreenDSfile1.csv')
lst2=f2.readlines()[-100:]

ft2= open('GreenDSfile1_samplelast100.csv','w')
for i in range(100):
    ft2.writelines(lst2[i])