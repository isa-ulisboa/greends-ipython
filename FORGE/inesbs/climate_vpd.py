
# open a csv file

import sys

from myfunctions import VPdef
f = open("Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv") 

lst1 = f.readlines()     #store climate info in one list
# print(lst1[5])

all_values = []
header = []
lst2 = []
counter = 0

for line in lst1: 
    if counter <= 1:    # the first 2 lines are headers (line 0 and line 1)
        header.append(line)   # add first 2 lines to header list
    else:                         # otherwise 1. split the lines 2. gets values 3.calculate VPD values etc...
        lst2 = line.split(",")
        Tmin = lst2[4]    # Tmin in column 5
        Tmax = lst2[3]     # Tmax in column 4
        RHmean = lst2[5]  # RHmean in column 6
        VPD = VPdef(float(Tmax), float(Tmin), float(RHmean))   #VPdef in myfunctions.py
        lst2.append(VPD)    # create lst_vpd and add VPD values to list 2 
        all_values.append(lst2)     # add list to all_values list
    counter += 1

# print ([row[5] for row in all_values])  #code to print values from a column

import csv
with open("Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010_vpd.csv", "w", newline= '') as f2:

    write = csv.writer(f2)
    write.writerows(all_values)
f2.close()   
f.close()

## Second part of the assignment

fin = open("Climate_hisafe_knmircp85_daily_from_01-01-2006_to_31-12-2100.csv") 

lst3 = fin.readlines()     #store climate info in one list

values = []
header1 = []
lst4 = []
counter = 0



for day in lst3: 
    if counter <= 1:    # the first 2 lines are headers (line 0 and line 1)
        header1.append(day)   # add first 2 lines to header1 list
    else:                         # otherwise 1. split the lines 2. gets values 3.calculate VPD values etc...
        lst4 = day.split(",")
        Tmin = lst4[4]    # Tmin in column 4
        Tmax = lst4[3]     # Tmax in column 3
        RHmean = lst4[5]  # RHmean in column 5
        VPD = VPdef(float(Tmax), float(Tmin), float(RHmean))   #VPdef in myfunctions.py
        lst4.append(VPD)    # create lst_vpd and add VPD values to list 4
        values.append(lst4)     # add list to all_values list
    counter += 1


with open("Climate_hisafe_knmircp85_daily_from_01-01-2006_to_31-12-2100_vpd.csv", "w", newline = '') as f3:

    write = csv.writer(f3)
    write.writerows(values)
f3.close()
