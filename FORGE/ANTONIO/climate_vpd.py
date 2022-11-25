import csv
import myFunctions as mf


with open("Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv", 'r') as file:
    file_read = csv.reader(file)
    climate_info = list(file_read)

lst_vpd = ['', 'vpd']

nLines = len(climate_info)
for i in range(nLines-2):
    tmax = float(climate_info[i+2][3])
    tmin = float(climate_info[i+2][4])
    rh = float(climate_info[i+2][5])
    
    vpd = mf.calculate_vpd(tmax, tmin, rh)
    vpd = round(vpd,4)
    
    lst_vpd.append(vpd)

with open("Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010_vpd.csv", "w", newline='') as newfile:
    for i in range(nLines):
        newfile_write = csv.writer(newfile)
        climate_info[i].append(lst_vpd[i])
        newfile_write.writerow(climate_info[i])

climate_info.clear()
lst_vpd.clear()