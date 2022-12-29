
import myFunctions_6 as mf6
import pandas as pd
import csv

#Read csv and skip the first row
data= pd.read_csv('Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv',skiprows=1)

'''print(data.columns) - identifica as colunas'''

#Match the columns value to Variab
Tmax=data['tasmax']
Tmin=data['tasmin']
RHmean=data['hurs']

#Create a new csv file with an extra column: VPD Values
data_vpd= data.copy()


data_vpd['VPD Values']= round(mf6.calculate_vpd(Tmax,Tmin,RHmean),4)



data_vpd.columns
print(data_vpd)

data_vpd.to_csv(r'/Users/diogopinto/Documents/VScode/greends-ipython/FORGE/DIOGOPINTO/myForge/Assignments/#6/Climate_vpd.csv')



'''
print(data_vpd.loc[data_vpd["VPD Values"]>0.4])
print(data_vpd.describe())
print(data_vpd.info())
'''
