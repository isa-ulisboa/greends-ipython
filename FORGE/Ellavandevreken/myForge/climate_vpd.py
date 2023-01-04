#assignment 6
#zie bestand JOHANNA onderaan deze file
"""
#zelf wat probeersle maar NB, vraag iemand anders 
f = open("Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv") 

# import csv
# with open('Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv') as csvfile:
#     csvbest = csv.reader(csvfile, delimiter=',')
#     for row in csvbest:
#         print(row)

geg = f.readlines()
l=len(geg)
names=geg[1]
val = geg[2:l-1]
f.close()

import pandas as pd
gegevens = pd.read_csv('Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv', header = 1) 

#gegevens is een list, header = 1 moet je doen omdat de kolomtitels op de 2e lijn staan in het excelbestand
"""
#johanna
# Assignment #6
import csv
import myFunctions as mF      

# Open the file "Climate_hisafe_kmnievaluation_..."
# Store the climate information at your will (e.g in one list, several lists, explore the module csv, etc)
with open("Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv", 'r') as file:
    climate_info = csv.reader(file)
   

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
    vpd = round(vpd,4)                          #eigen keuze, afronden gewoon omdat het overzichtelijker is 
    # populate the list
    lst_vpd.append(vpd)

# Create, in your FORGE/YourName a new file named "Climate_hisafe_kmnievaluation_..._vpd.csv". The result will be a identical file with an extra column with VPD values
with open("FORGE/Ellavandevreken/Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010_vpd.csv", "w", newline='') as newfile:
    for i in range(nLines):
        newfile_write = csv.writer(newfile, doublequote=False, escapechar=None, quotechar=None)  #eerst hadden we gewoon csv.writer(newfile) maar dan kreeg jij bij eerste lijn met link te veel aanhaaltekens hier niet meer, dit komt van discord van johanne in opmerking, ik moet nog checken of het dan nu wel werkt
        climate_info[i].append(lst_vpd[i])
        newfile_write.writerow(climate_info[i])

# Repeat for the other file
climate_info.clear()
lst_vpd.clear()

# Open the file "Climate_hisafe_knmircp85_..."
# Store the climate information at your will (e.g in one list, several lists, explore the module csv, etc)
with open("Climate_hisafe_knmircp85_daily_from_01-01-2006_to_31-12-2100.csv", 'r') as file2:
    climate_info= csv.reader(file2)

# Remember: You need to avoid reading the header in the calculations
# Create a new list called lst_vpd
lst_vpd = ['', 'vpd']    #ik denk eerste 2 lijnen met dit vullen want waarden starten 

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
with open("FORGE/Ellavandevreken/Climate_hisafe_knmircp85_daily_from_01-01-2006_to_31-12-2100_vpd.csv", "w", newline='') as newfile2:
    for i in range(nLines):
        newfile_write = csv.writer(newfile2, doublequote=False, escapechar=None, quotechar=None) #ipv csv.writer(newfile2)
        climate_info[i].append(lst_vpd[i])
        newfile_write.writerow(climate_info[i])

climate_info.clear()
lst_vpd.clear()