#ASSIGNMENT 5 - HANDLING AN ASCII FILE

import csv

i=0

with open ("GreenDSfile1.csv", 'r') as file:

    csvreader = csv.reader(file)
    for row in csvreader:
        i=i+1

print(i)

#para eliminar a 1.ª linha (quando há título, p.ex.): header = next(csvreader)

lst = []
i=0

with open ("GreenDSfile1.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        while i < 500000:
            i=i+1
            lst.append(row)


with open ("GreenDSfile1_sample500k.csv", 'w') as file:
    for row in lst:
        file.write(str(row)+ ', ')

