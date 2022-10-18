import sys
import csv
import myFunctions
from itertools import zip_longest

#CSV FILE: "Climate_hisafe_kmnievaluation_..."

#Open the file "Climate_hisafe_kmnievaluation_..." and storage the data in lists

f = open("Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv", "r")

lst = f.readlines()[1:]

file1 = csv.DictReader(lst)

Day = []
Month = []
Year = []
Tmax = []
Tmin = []
RHmean = []
evspsbl = []
rsds = []
pr = []
sfcWind = []

for col in file1:
    Tmax.append(col["tasmax"])
    Tmin.append(col["tasmin"])
    RHmean.append(col["hurs"])
    Day.append(col["Day"])
    Month.append(col["Month"])
    Year.append(col["Year"])
    evspsbl.append(col["evspsbl"])
    rsds.append(col["rsds"])
    pr.append(col["pr"])
    sfcWind.append(col["sfcWind"])

''' 
print("Tmax:", Tmax)
print("Tmin:", Tmin)
print("RHmean:", RHmean)

print("Tmax_float:", Tmax_float)
print("Tmin_float":, Tmin_float)
print("RHmean_float":, RHmean_float)

print("Day:", Day)

'''
Tmax_float = [float(i) for i in Tmax]
Tmin_float = [float(i) for i in Tmin]
RHmean_float = [float(i) for i in RHmean]

#Creation of the list vpd with the vpd calculations

vpd = []

for idx,item in enumerate(Tmax_float):
    vpd.append(myFunctions.calculate_vpd(Tmax_float[idx], Tmin_float[idx], RHmean_float[idx]))

#Creating a csv file with all climate variables and vpd calculations

fields = ['Day', 'Month', 'Year', 'tasmax', 'tasmin', 'hurs', 'evspsbl', 'rsds', 'pr', 'sfcWind', 'vpd'] #field names
	
rows = [Day, Month, Year, Tmax, Tmin, RHmean, evspsbl, rsds, pr, sfcWind, vpd] # data rows of csv file, using the list defined in the lines 26-35

export_data = zip_longest(*rows, fillvalue = '')

with open("Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010_NEW.csv", 'w', encoding = "ISO-8859-1", newline = '') as f:
    
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(export_data)
f.close()

################################################################################################################################################

#CSV FILE: "Climate_hisafe_kmnircp85_..."

#Open the file "Climate_hisafe_kmnircp85_..." and storage the data in lists

g = open("Climate_hisafe_knmircp85_daily_from_01-01-2006_to_31-12-2100.csv", "r")

lst2 = g.readlines()[1:]

file2 = csv.DictReader(lst2)

Day_g = []
Month_g = []
Year_g = []
Tmax_g = []
Tmin_g = []
RHmean_g = []
evspsbl_g = []
rsds_g = []
pr_g = []
sfcWind_g = []

for col in file2:
    Tmax_g.append(col["tasmax"])
    Tmin_g.append(col["tasmin"])
    RHmean_g.append(col["hurs"])
    Day_g.append(col["Day"])
    Month_g.append(col["Month"])
    Year_g.append(col["Year"])
    evspsbl_g.append(col["evspsbl"])
    rsds_g.append(col["rsds"])
    pr_g.append(col["pr"])
    sfcWind_g.append(col["sfcWind"])

''' 
print("Tmax:", Tmax)
print("Tmin:", Tmin)
print("RHmean:", RHmean)

print("Tmax_float:", Tmax_float)
print("Tmin_float":, Tmin_float)
print("RHmean_float":, RHmean_float)

print("Day:", Day)

'''
Tmax_float_g = [float(i) for i in Tmax_g]
Tmin_float_g = [float(i) for i in Tmin_g]
RHmean_float_g = [float(i) for i in RHmean_g]

#Creation of the list vpd with the vpd calculations

vpd_g = []

for idx,item in enumerate(Tmax_float_g):
    vpd_g.append(myFunctions.calculate_vpd(Tmax_float_g[idx], Tmin_float_g[idx], RHmean_float_g[idx]))

#Creating a csv file with all climate variables and vpd calculations

fields_g = ['Day', 'Month', 'Year', 'tasmax', 'tasmin', 'hurs', 'evspsbl', 'rsds', 'pr', 'sfcWind', 'vpd'] #field names
	
rows_g = [Day_g, Month_g, Year_g, Tmax_g, Tmin_g, RHmean_g, evspsbl_g, rsds_g, pr_g, sfcWind_g, vpd_g] # data rows of csv file, using the list defined in the lines 26-35

export_data_g = zip_longest(*rows_g, fillvalue = '')

with open("Climate_hisafe_knmircp85_daily_from_01-01-2006_to_31-12-2100_NEW.csv", 'w', encoding = "ISO-8859-1", newline = '') as g:
    
    write = csv.writer(g)
    write.writerow(fields_g)
    write.writerows(export_data_g)
f.close()
