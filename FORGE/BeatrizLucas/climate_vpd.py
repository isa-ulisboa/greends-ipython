# assignment 6

import csv
import myFunctions as fun

## File "Climate_hisafe_kmnievaluation_..."

# Create a code to open the file "Climate_hisafe_kmnievaluation_..."

with open("Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv") as f:
    reader = csv.reader(f)
    climate_data = list(reader) # Store the information in the file f in a list called climate_data

# Storage of the number of lines of the file f - determined with the function "len" - in a variable called "count"

count = len(climate_data)

# Creation of an empty list to sotre the calculations of vpd (these calculations are stored in the variable vpd)

lst_vpd = ["", "vpd"] 

#Creation of a loop in order to ignore the first 2 lines of the file f in the calculations of vpd

for i in range(count):
    if i <= 1:
        pass
    else:
        tmax = float(climate_data [i][3])
        tmin = float(climate_data [i][4])
        rhmean = float(climate_data [i][5])
        vpd = fun.calculate_vpd(tmax, tmin, rhmean)
        vpd = round(vpd, 4)
        lst_vpd.append(vpd) # Populate the list lst_vpd with the result of your function "calculate_vpd"

# Creation in my FORGE/BeatrizLucas a new file named "Climate_hisafe_kmnievaluation_..._vpd.csv" with an extra column with vpd calculated values
# "doublequote = False, escapechar = None, quotechar = None" are used so the 1st row doesn't appear with extra doublequotes. escapechar and quotechar must be set as None so any error occurs.

with open("FORGE/BeatrizLucas/Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010_vpd.csv", "w", newline = "") as new_file:
    for i in range(count):
        new_file_write = csv.writer(new_file, doublequote = False, escapechar = None, quotechar = None)
        climate_data[i].append(lst_vpd[i])
        new_file_write.writerow(climate_data[i])

## File "Climate_hisafe_knmircp85_..."

# Create a code to open the file "Climate_hisafe_knmircp85_..."

with open("Climate_hisafe_knmircp85_daily_from_01-01-2006_to_31-12-2100.csv") as f2:
    reader = csv.reader(f2)
    climate_data = list(reader) # Store the information in the file f in a list called climate_data

# Storage of the number of lines of the file f - determined with the function "len" - in a variable called "count"

count = len(climate_data)

# Creation of an empty list to sotre the calculations of vpd (these calculations are stored in the variable vpd)

lst_vpd = ["", "vpd"] 

#Creation of a loop in order to ignore the first 2 lines of the file f in the calculations of vpd

for i in range(count):
    if i <= 1:
        pass
    else:
        tmax = float(climate_data [i][3])
        tmin = float(climate_data [i][4])
        rhmean = float(climate_data [i][5])
        vpd = fun.calculate_vpd(tmax, tmin, rhmean)
        vpd = round(vpd, 4)
        lst_vpd.append(vpd) # Populate the list lst_vpd with the result of your function "calculate_vpd"

# Creation in my FORGE/BeatrizLucas a new file named "Climate_hisafe_knmircp85_..._vpd.csv" with an extra column with vpd calculated values
# "doublequote = False, escapechar = None, quotechar = None" are used so the 1st row doesn't appear with extra doublequotes. escapechar and quotechar must be set as None so any error occurs. 

with open("FORGE/BeatrizLucas/Climate_hisafe_knmircp85_daily_from_01-01-2006_to_31-12-2100_vpd.csv", "w", newline = "") as new_file2:
    for i in range(count):
        new_file2_write = csv.writer(new_file2, doublequote = False, escapechar = None, quotechar = None)
        climate_data[i].append(lst_vpd[i])
        new_file2_write.writerow(climate_data[i])