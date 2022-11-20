import csv
import myFunctions as mf

#Open the file "Climate_hisafe_kmnievaluation
#Store the climate information at your will (e.g in one list, several lists, explore the module csv, etc) 

with open("Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv", 'r') as file:
    file_read = csv.reader(file)
    climate_info = list(file_read)

#Create a new list called lst_vpd

 lst_vpd=['', 'vpd']

#Populate the list with the result of your function "calculate_vpd

total_lines = len(climate_info)
for i in range(total_lines-2):
    tmax = float(climate_info[i+2][3])
    tmin = float(climate_info[i+2][4])
    rh = float(climate_info[i+2][5])
    
    vpd = mf.calculate_vpd(tmax, tmin, rh)
    vpd = round(vpd,4)
    
    lst_vpd.append(vpd)

#Create, in your FORGE/YourName a new file named "Climate_hisafe_kmnievaluation_..._vpd.csv
with open("Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010_vpd.csv", "w", newline='') as newfile:
    for i in range(total_lines):
        newfile_write = csv.writer(newfile)
        climate_info[i].append(lst_vpd[i])
        newfile_write.writerow(climate_info[i])

#Do the same process to the file "Climate_hisafe_knmircp85_..."

climate_info.clear()
lst_vpd.clear()

with open("Climate_hisafe_knmircp85_daily_from_01-01-2006_to_31-12-2100.csv", 'r') as second_file:
    file_read = csv.reader(second_file)
    climate_info = list(file_read)

lst_vpd=['', 'vpd']

total_lines = len(climate_info)
for i in range(total_lines-2):
    tmax = float(climate_info[i+2][3])
    tmin = float(climate_info[i+2][4])
    rh = float(climate_info[i+2][5])
    
    vpd = mf.calculate_vpd(tmax, tmin, rh)
    vpd = round(vpd,4)
    
    lst_vpd.append(vpd)

with open("Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010_vpd.csv", "w", newline='') as newfile:
    for i in range(total_lines):
        newfile_write = csv.writer(newfile)
        climate_info[i].append(lst_vpd[i])
        newfile_write.writerow(climate_info[i])

climate_info.clear()
lst_vpd.clear()
    
    

    
        
    


    