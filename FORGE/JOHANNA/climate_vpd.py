# Assignment #6
import csv
import myFunctions as mF      

# Open the file "Climate_hisafe_kmnievaluation_..."
# Store the climate information at your will (e.g in one list, several lists, explore the module csv, etc)
with open("Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv", 'r') as file:
    climate_info = list(csv.reader(file)) #list that contains lists (each inner list = one row of the csv-file)
    
nLines = len(climate_info) # total number of rows

# Populate the list with the result of your function "calculate_vpd"
for i in range(nLines-2): #-2 iterations. Use below always i+2 to avoid the header but include the last 2 rows
    tmax = float(climate_info[i+2][3]) # get tmax from 4th column and convert to number
    tmin = float(climate_info[i+2][4])
    rh = float(climate_info[i+2][5]) 
    vpd = round( mF.calculate_vpd(tmax, tmin, rh), 2)  # calculate vpd, round to 2 decimal places
    climate_info[i+2].append(vpd) # append the calculated vpd to the matching list in climate_info

climate_info[1].append('vpd') #add title 'vpd' for vpd-value column

# Create in your FORGE/YourName a new file named "Climate_hisafe_kmnievaluation_..._vpd.csv". The result will be a identical file with an extra column with VPD values
with open("FORGE/JOHANNA/Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010_vpd.csv", "w", newline='') as newfile:
    for i in range(nLines):
        csv.writer(newfile, doublequote=False, escapechar='', quotechar=None).writerow(climate_info[i])

### Repeat for the other file
climate_info.clear()

with open("Climate_hisafe_knmircp85_daily_from_01-01-2006_to_31-12-2100.csv", 'r') as file:
    climate_info = list(csv.reader(file))

nLines = len(climate_info)
for i in range(nLines-2):
    tmax = float(climate_info[i+2][3])
    tmin = float(climate_info[i+2][4])
    rh = float(climate_info[i+2][5])
    vpd = mF.calculate_vpd(tmax, tmin, rh)
    vpd = round(vpd,2)
    climate_info[i+2].append(vpd)

climate_info[1].append('vpd')

with open("FORGE/JOHANNA/Climate_hisafe_knmircp85_daily_from_01-01-2006_to_31-12-2100_vpd.csv", "w", newline='') as newfile:
    for i in range(nLines):
        csv.writer(newfile, doublequote=False, escapechar='', quotechar=None).writerow(climate_info[i])

climate_info.clear()