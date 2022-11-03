import csv
from myFunctions import calculate_vpd
with open ("Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv", 'r') as ch:
    csvreader = csv.reader(ch)

    header = next(csvreader)
    header2 = next(csvreader)

    lst = []
    i=0
    for row in csvreader:
        lst.append(row)
print(lst[0])

lst_vpd = []
i=0

for row in lst:
    lst_vpd.append(calculate_vpd(Tmax=row[3], Tmin=row[4], RHmean=row[5]))
print(lst_vpd[0])