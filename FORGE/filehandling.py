# Open data source csv

import sys

p = open("GreenDSfile1.csv")
a = p.readlines()
p.close()

# Print first 500k lines in new document

pw = open("GreenDSfile1_sample500k.csv", "w")
for i in range(500000):
    pw.writelines(a[i])
pw.close()

# Print the number of lines in the source csv

p = open("GreenDSfile1.csv", "r")
lst = len(p.readlines())
print("Nº total de linhas:", lst)
p.close()

# Create a new file to store the last 100 lines from the data source csv

p = open("GreenDSfile1.csv")
a = p.readlines()
p.close()

pw2 = open("GreenDSfile1_samplelast100.csv", "w")
for x in range(1999900, 2000000):
    pw2.writelines(a[x])
pw2.close()

   