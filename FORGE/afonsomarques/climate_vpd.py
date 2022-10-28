

import csv

with open("Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv", "r") as climate_data:
    climate_data_reader = csv.DictReader(climate_data)
    climate_data.close

    next(climate_data_reader)

    with open ("FORGE/afonsomarques/climate_vpd.csv", "w") as climate_file:
        fieldnames = ["Day", "Month", "Year", "tasmax", "tasmin", "hurs", "evspsbl", "rsds", "pr", "sfcWind", "vpd"]

        climate_file_writer = csv.DictWriter(climate_data, fieldnames=fieldnames)

        climate_file_writer.writeheader()

        for line in climate_data_reader:
            climate_file_writer.writerow(line)
            

