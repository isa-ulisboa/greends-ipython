import csv
from myfunctions import calculate_vpd 
# First File traitement
#open the first file and change into a list      
with open("Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv", 'r') as rowdata_1981_2010:
    climate1 = list(csv.reader(rowdata_1981_2010)) 
#lenght of the file
nLines1 = len(climate1) 
# Populate the list with the result of your function "calculate_vpd"
for i in range(nLines1-2): # -2 because we want to avoid the header
    tmax= float(climate1[i+2][3]) 
    tmin = float(climate1[i+2][4])
    rh = float(climate1[i+2][5])
    vpd = round( calculate_vpd(tmax, tmin, rh), 2)  
    climate1[i+2].append(vpd) 
climate1[1].append('vpd') 
 
# Create in your FORGE/YourName a new file named "Climate_hisafe_kmnievaluation_..._vpd.csv"
with open("FORGE/aziza/Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010_vpd.csv", "w", newline='') as newfile_1981_2010:
    for i in range(nLines1):
        csv.writer(newfile_1981_2010, doublequote=False, escapechar='', quotechar=None).writerow(climate1[i])
# 2nd file traitement
# open the 2nd file and change into a list 
with open("Climate_hisafe_knmircp85_daily_from_01-01-2006_to_31-12-2100.csv", 'r') as rowdata_2006_2100:
    climate2 = list(csv.reader(rowdata_2006_2100))
#lenght of the file
nLines2 = len(climate2)
# Populate the list with the result of your function "calculate_vpd"
for i in range(nLines2-2): # -2 because we want to avoid the header 
    tmax = float(climate2[i+2][3])
    tmin = float(climate2[i+2][4])
    rh = float(climate2[i+2][5])
    vpd = calculate_vpd(tmax, tmin, rh)
    vpd = round(vpd,2)
climate2[i+2].append(vpd)
climate2[1].append('vpd')
# Create in your FORGE/YourName a new file named "Climate_hisafe_kmnievaluation_..._vpd.csv" 
with open("FORGE/aziza/Climate_hisafe_knmircp85_daily_from_01-01-2006_to_31-12-2100_vpd.csv", "w", newline='') as newfile_2006_2100:
    for i in range(nLines2):
        csv.writer(newfile_2006_2100, doublequote=False, escapechar='', quotechar=None).writerow(climate2[i])
 


