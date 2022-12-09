#ASSIGNMENT 6 
#create code to open the file "Climate_hisafe_Kminevaluation_..." and store info at a list
import csv
import math
import myFunctions as mf

with open ("Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv", 'r') as ch:
    csvreader = csv.reader(ch)

    header1 = next(csvreader)

    lst = []
    i=0
    for row in csvreader:
        lst.append(row)
#print(lst[0])           #se quiser ver o que existe na 1.ª linha


#create a new list called "lst_vpd" and populate the list with result function "calculate_vpd"
lst_vpd = []
i=0



for row in range(1, len(lst)):
    lst_vpd.append(mf.calculate_vpd(Tmax=float(lst[row][3]), Tmin=float(lst[row][4]), RHmean=float(lst[row][5])))

#lst_h.append("VPD")
lst[0].append("VPD")


for i in range(1,len(lst)-1):
    lst_vf = []
    lst_vf.append(lst_vpd[i])
    lst[i] = lst[i] + lst_vf


with open ("FORGE/SAMUEL/Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010_vpd.csv", 'w') as ch:
    ch.write(header1[0]+"\n")
    #ch.write(header2[0] + ", vpd")    #falta aparecer ",vpd" no cabeçalho ficheiro!!! Como se faz?
   
    for row in lst:
        for i in range(0, len(row)):
            ch.write(str(row[i]) + ",")  
        ch.write("\n")  
            #print(row[i])



