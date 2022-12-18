#ASSIGNMENT 7

import sys
# (Facultative) setting path to get your myfunctions 
sys.path.append('../FORGE/SAMUEL') # This adds your modules if your module is somewhere else not script folder or subfolders

import pandas as pd
import myFunctions
Current = pd.read_csv('Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv', skiprows=[0])
Future = pd.read_csv('Climate_hisafe_knmircp85_daily_from_01-01-2006_to_31-12-2100.csv', skiprows=[0])
#print(Current)
# Calculate VPD with pandas (your vpd function should work with numpy instead math library)
# The following creates an additional column called "VPD" where your function is used
Current["VPD"] = myFunctions.calculate_vpd_7(Current["tasmax"],Current["tasmin"],Current["hurs"] )
Future["VPD"] = myFunctions.calculate_vpd_7(Future["tasmax"],Future["tasmin"],Future["hurs"] )
#print(Current["tasmax"])

#Current.insert(10,column="VPD",value=myFunctions.calculate_vpd_7(Current["tasmax"],Current["tasmin"],Current["hurs"] ))
#Future.insert(10,column="VPD",value=myFunctions.calculate_vpd_7(Future["tasmax"],Future["tasmin"],Future["hurs"] ))


#calcular média mensal
current_1981_2010=Current[(Current["Year"]>=1981)&(Current["Year"]<=2010)]
future_2031_2060=Future[(Future["Year"]>=2031)&(Future["Year"]<=2060)]

#calcular um novo dataset para ter a média mensal
mean_current=current_1981_2010.groupby(["Month"]).mean()
mean_current["VPD"]
print(mean_current["VPD"]) #queremos imprimir a coluna VPD com a média já calculada

mean_future=future_2031_2060.groupby(["Month"]).mean()
mean_future["VPD"]
print(mean_future["VPD"]) 

#criar gráfico
import matplotlib as mp #mat e não Mapt...

mean_current["VPD"].plot(label="VPD", color="blue") #label é o nosso Y e queremos que tenha cor blue
mp.pyplot.suptitle("VPD_current_mean") # para escrever o título
mp.pyplot.show()

mean_future["VPD"].plot(label="VPD", color="blue") #label é o nosso Y e queremos que tenha cor blue
mp.pyplot.suptitle("VPD_future_mean") # para escrever o título
mp.pyplot.show()

