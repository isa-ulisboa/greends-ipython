import pandas as pd

#Read csv and skip the first row
data= pd.read_csv('Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv',skiprows=1)

'''print(lst_vpd.columns) - identifica as colunas'''

#Match the columns value to Variab
d= data['Day']
m = data['Month']
y = data['Year']
Tmax=data['tasmax']
Tmin=data['tasmin']
RHmean=data['hurs']

x = d[2] #and m[3] and y[1988]

print (x)