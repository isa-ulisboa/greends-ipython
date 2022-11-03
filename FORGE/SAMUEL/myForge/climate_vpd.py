import csv
import math
#from myFunctions import calculate_vpd
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

def calculate_vpd (Tmax, Tmin, RHmean):
    val1 = 0.6108
    val2 = math.exp((17.27*Tmax)/(Tmax + 273.3))
    val3 = val1
    val4 = math.exp((17.27*Tmin)/(Tmin + 273.3))
    Es = (val1*val2+val3*val4)/2

    Ea = RHmean/100*Es
  
    VPD = Es - Ea

    return(VPD)
for row in lst:
    lst_vpd.append(calculate_vpd(Tmax=float(row[3]), Tmin=float(row[4]), RHmean=float(row[5])))
print(lst_vpd[0])


#retirar da linha 19-30 e ativar a linha 3 (pq o commit n estava a funcioinar)
lst_final = []
for i in range(0,len(lst)):
    lst_final.append(lst[i])
    lst_final.append(lst_vpd[i])
print(lst_final[0])
with open ("Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010_vpd.csv", 'w') as ch:
    
    for row in lst_final:
        ch.write(str(row))
    
