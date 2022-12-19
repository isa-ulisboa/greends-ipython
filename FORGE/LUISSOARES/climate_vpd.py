import sys
import myFunctions as func
import csv


# Open the file "Climate_hisafe_kmnievaluation_..."
# Store the climate information
list_vpd = []

with open("Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv", 'r') as df:
    reader = csv.reader(df)
    climate_list = list(reader)
    climate_list_lenght = len(climate_list)

counter = 0

for i in range(climate_list_lenght):
    if i == 0:
        list_vpd.append(None)
        pass
    elif i == 1:
        list_vpd.append("vpd")
        pass
    else:
        if i == 10956:
            dummy = 0
        Tmax = climate_list[i][3]
        Tmin = climate_list[i][4]
        RHmean = climate_list[i][5]
        Tmax_float = float(Tmax)
        Tmin_float = float(Tmin)
        RHmean_float = float(RHmean)
        list_vpd.append(func.calculate_vpd(Tmax_float, Tmin_float, RHmean_float))
        

list_vpd_lenght = len(list_vpd)

with open("FORGE/LUISSOARES/Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010_vpd.csv", 'w', newline='') as df2:

    for i in range(climate_list_lenght):
        x = csv.writer(df2)
        climate_list[i].append(list_vpd[i])
        x.writerow(climate_list[i])

print("Done")