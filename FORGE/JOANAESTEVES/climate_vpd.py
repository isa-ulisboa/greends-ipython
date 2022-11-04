# We will need myFunctions file
import myFunctions as mf

# To parse out all the information, we use the csv module
import csv

# Read the csv file and store climate information
with open("Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv", "r") as csv_file:
    csvreader = csv.reader(csv_file)
    clim_info = list(csvreader)

# Create a new list and avoid reading the header
lst_vpd = ["", "vpd"]

# Populate the list with the vpd function's results
lst_lines = len(clim_info)
for i in range(lst_lines - 2):
    Tmax = float(clim_info[i+2][3])
    Tmin = float(clim_info[i+2][4])
    RHmean = float(clim_info[i+2][5])

    vpd = mf.calculate_vpd(Tmax, Tmin, RHmean)

# Create a new csv file in our folder - it will have an extra column with the vpd values
with open("Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010_vpd.csv", "w") as new_csvfile:
    for i in range(lst_lines):
        f = csv.writer(new_csvfile)
        clim_info[i].append(lst_vpd[i])
        f.writerow(clim_info[i])
        