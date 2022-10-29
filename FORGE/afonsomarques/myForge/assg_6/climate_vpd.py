#import myFunctions as mf
#import numpy as np
import csv
#import function as f

with open("Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv", "r") as climate_data:
    climate_data_readear = csv.DictReader(climate_data)

    next(climate_data_readear)

    with open ("FORGE/afonsomarques/assg_6/climate_dict.csv", "w") as outfile:
        vars = ("Day", "Month", "Year", "tasmax", "tasmin", "hurs", "evspsbl", "rsds", "pr", "sfcWind")
        climate_data_writter = csv.DictWriter(outfile, fieldnames=vars, delimiter="\t")
        climate_data_writter.writeheader()
        for i in climate_data_readear:
            climate_data_writter.writerow(i)





