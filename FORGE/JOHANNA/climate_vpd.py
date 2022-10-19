# Assignment #6
import csv
import myFunctions as mF      

# Open the file "Climate_hisafe_kmnievaluation_..."
# Store the climate information at your will (e.g in one list, several lists, explore the module csv, etc)
with open("Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv", 'r') as file:
    file_read = csv.reader(file)
    climate_info = list(file_read)

# Remember: You need to avoid reading the header in the calculations
# Create a new list called lst_vpd
lst_vpd = ['', 'vpd']

# Populate the list with the result of your function "calculate_vpd" (Tip: search for the list method append() )
nLines = len(climate_info)
for i in range(nLines-2):
    tmax = float(climate_info[i+2][3])
    tmin = float(climate_info[i+2][4])
    rh = float(climate_info[i+2][5])
    # calculate vpd
    vpd = mF.calculate_vpd(tmax, tmin, rh)
    vpd = round(vpd,4)
    # populate the list
    lst_vpd.append(vpd)

# Create, in your FORGE/YourName a new file named "Climate_hisafe_kmnievaluation_..._vpd.csv". The result will be a identical file with an extra column with VPD values
with open("Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010_vpd.csv", "w", newline='') as newfile:
    for i in range(nLines):
        newfile_write = csv.writer(newfile)
        climate_info[i].append(lst_vpd[i])
        newfile_write.writerow(climate_info[i])

# Repeat for the other file
climate_info.clear()
lst_vpd.clear()

# Open the file "Climate_hisafe_knmircp85_..."
# Store the climate information at your will (e.g in one list, several lists, explore the module csv, etc)
with open("Climate_hisafe_knmircp85_daily_from_01-01-2006_to_31-12-2100.csv", 'r') as file2:
    file_read = csv.reader(file2)
    climate_info = list(file_read)

# Remember: You need to avoid reading the header in the calculations
# Create a new list called lst_vpd
lst_vpd = ['', 'vpd']

# Populate the list with the result of your function "calculate_vpd" (Tip: search for the list method append() )
nLines = len(climate_info)
for i in range(nLines-2):
    tmax = float(climate_info[i+2][3])
    tmin = float(climate_info[i+2][4])
    rh = float(climate_info[i+2][5])
    # calculate vpd
    vpd = mF.calculate_vpd(tmax, tmin, rh)
    vpd = round(vpd,4)
    # populate the list
    lst_vpd.append(vpd)

# Create, in your FORGE/YourName a new file named "Climate_hisafe_kmnievaluation_..._vpd.csv". The result will be a identical file with an extra column with VPD values
with open("Climate_hisafe_knmircp85_daily_from_01-01-2006_to_31-12-2100_vpd.csv", "w", newline='') as newfile2:
    for i in range(nLines):
        newfile_write = csv.writer(newfile2)
        climate_info[i].append(lst_vpd[i])
        newfile_write.writerow(climate_info[i])

climate_info.clear()
lst_vpd.clear()