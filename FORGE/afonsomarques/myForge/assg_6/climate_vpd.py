from csv import DictReader, DictWriter
import function as f
from typing import List, Dict

path_assg_6 = "FORGE/afonsomarques/myForge/assg_6/"
file = "Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv"

file_handle = open(file)        ###open the file
next(file_handle)       ###skip the first line (url)
csv_reader = DictReader(file_handle)        ###read as a dictionary
table: List[Dict[str, float]] = []      ###set a variable, 'table' with dict within a list

for row in csv_reader:  
    float_row: dict[str, float] = {}        ###set variable 'float_row' as dict with str and float
    for column in row: 
        float_row[column] = float(row[column])       ###set the first row as the key value (str) and the rest as (float)
    vpd = f.vap_pres_def(float_row['tasmax'],
     float_row['tasmin'], float_row['hurs'])        ### calculate vpd
    float_row['vpd'] = vpd      ###add vpd collumn to the 'float_row'
    table.append(float_row)     ###append 'float_row' to variable table


        ###create a csv file with table information
with open(path_assg_6+"climate_dict.csv", "w", newline='') as infile:
    var = ('Day','Month','Year','tasmax','tasmin','hurs','evspsbl','rsds','pr','sfcWind', 'vpd')
    csv_wrt = DictWriter(infile, fieldnames=var)
    csv_wrt.writeheader()
    for line in table:
        csv_wrt.writerow(line)

file_handle.close()