import pandas as pd
import myFunctions_7 as mf7
import matplotlib.pyplot as plt


#Read CSV file 
current= pd.read_csv('Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv',skiprows=[0])
future= pd.read_csv('Climate_hisafe_knmircp85_daily_from_01-01-2006_to_31-12-2100.csv',skiprows=[0])


#Creat a new column with the VPD values 
current['VPD']= mf7.calculate_vpd(current['tasmax'],current['tasmin'],current['hurs'])
future['VPD']= mf7.calculate_vpd(future['tasmax'],future['tasmin'],future['hurs'])


#Monthly average - VPD
c_vpd_m= current.groupby('Month').mean()
f_vpd_m= future.groupby('Month').mean()

#Adding VPD mean values to the plot
c_vpd_m['VPD'].plot(label='c_VPD 1981-2010',color='green')
f_vpd_m['VPD'].plot(label='f_VPD 2006-2100', color='orange')

 
   #Legenda
plt.title('VPD Analysis')
plt.xlabel('Month')
plt.ylabel('VPD_mean')
plt.legend()


#Show plot
plt.show()
