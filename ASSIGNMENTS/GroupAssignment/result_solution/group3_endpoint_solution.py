import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import numpy as np
#import material, group1_solution, group2_solution
import group1_solution, group2_solution
import pandas


#Group 3 develops an this API to collect data from user and applies user data to run group1 and group2 output:
#  a function called get_pF that receives the arguments Theta_withoutRunoff, alpha, Thetar, Thetas and nSoil. 
#  Check what you need. For example, Theta_withoutRunoff can be calculated with dummy.material.get_Theta_withoutRunoff
#  alpha, Thetar, Thetas and nSoil are parameters of the Van Genuchten equation, provided in dummy_material.soils dictionary


###################################################### VISUALIZATION ################################################
# An API is made to collect data from USER

# Group 3 transforms tis step into an API
res = group1_solution.getHourlyWeatherForescast(37.64,-7.66)
#theta_3_9 = group1.get_ThetaForecast(0.25,[],[],[],60, "3")
#theta_9_27 = group1.get_ThetaForecast(0.25,[],[],[],180, "3")
pFCritical = 3.1
vpd_treshold = 0.5
next24h_rain_treshold = 2


dates = res['hourly']['time']
dates = list(map(lambda x: x[-8:-3], dates))
temp = res['hourly']['temperature_2m']
vpd = res['hourly']['vapor_pressure_deficit']
rh = res['hourly']['relativehumidity_2m']
ETo = res['hourly']['et0_fao_evapotranspiration']
precipitation = res["hourly"]['precipitation']
SoilMoisture_3_9 = res["hourly"]['soil_moisture_3_9cm']
SoilMoisture_9_27 = res["hourly"]['soil_moisture_9_27cm']
pF_3_9 = group2_solution.get_pF_forecast(SoilMoisture_3_9,"3")
pF_9_27 = group2_solution.get_pF_forecast(SoilMoisture_9_27,"3")

#Decision to irrigate ( 3-9 cm)
plan_3_9 = [0] * len(vpd) # create list with same elements fille with zero
plan_9_27 = [0] * len(vpd) # create list with same elements fille with zero
plan_3_9_dates = []
plan_9_27_dates = []

# Create the decision algorithm to trigger irrigation event
# Create a list of same size as, e.g. SoilMoisture_3_9, and add the value 1 for advise the irrigation event
# Rules: 1) soil tension is higher than pFCritical, 2) VPD is higher than vpd_treshold, 3) the sum of rain in the next 24 hours is less than 1 liter per m2
for idx,i in enumerate(vpd):
    next24_rain = sum(precipitation[idx:idx+24])
        
    if pF_3_9[idx]>=pFCritical and vpd[idx] > vpd_treshold and next24_rain < next24h_rain_treshold:
        if sum(filter(None, plan_3_9))<1:
            plan_3_9[idx] = 1
            plan_3_9_dates.append(dates[idx])
    if pF_9_27[idx]>=pFCritical and vpd[idx] > vpd_treshold and next24_rain < next24h_rain_treshold:
         if sum(filter(None, plan_9_27))<1:
            plan_9_27[idx] = 1
            plan_9_27_dates.append(dates[idx])

   
        
        
fig, axs = plt.subplots(2,2,sharex=True)
fig.suptitle('Green DS Master - Decision Support tool for irrigation needs. Current weather & soil retrieved from open-meteo.com\n'+
             'Irrigation criteria: pF > ' + str(pFCritical) + ", VPD > " + str(vpd_treshold)+ ", no rain next day that allows pF < " + str(pFCritical) + "\n"+
             "Next irrigation event for early rooting (3-9cm):" + str(plan_3_9_dates[0]) + "\n"+
             "Next irrigation event for established roots (9-27cm):" + str(plan_9_27_dates[0]) )
fig.set_size_inches(12,5)
axs[0,0].set_title('Temperature / VPD')
axs[0,0].plot(dates, temp, color='orange', label='Temp')
axs[0,0].set_ylabel('Celsius', color='orange')
secax_0_0 = axs[0,0].twinx()  # instantiate a second axes that shares the same x-axis
secax_0_0.plot(dates, vpd, color='blue')
secax_0_0.set_ylabel('VPD (kPa)', color='blue')
secax_0_0.fill_between(dates, vpd, vpd_treshold,  where=(np.array(vpd) >= np.array([vpd_treshold] * len(vpd))),
                 alpha=0.30, color='blue', label='VPD > '+str(vpd_treshold))
axs[0,0].legend(loc='upper left', frameon=False)

axs[0,1].set_title('EvapoTranspiration/Rain/Rel Hum')
axs[0,1].plot(dates, ETo, color='red',label='ETo')
axs[0,1].bar(dates, precipitation, color='blue',label='Rain')
axs[0,1].set_ylabel('ETo,Rain (mm)', color='black')
axs[0,1].legend(loc='upper right', frameon=False)
secax_0_1 = axs[0,1].twinx()  # instantiate a second axes that shares the same x-axis
secax_0_1.plot(dates, rh, color='magenta',label='RH')
secax_0_1.set_ylabel('Rel Hum (%)', color='magenta')
secax_0_1.legend(loc='upper right', frameon=False)

axs[1,0].set_title('Soil Moisture 3 to  9cm')
axs[1,0].plot(dates, SoilMoisture_3_9 , color='black', label='Soil moisture (3-9)')
secax_1_0 = axs[1,0].twinx()  # instantiate a second axes that shares the same x-axis
secax_1_0.plot(dates, pF_3_9, color='orange',label='pF')
secax_1_0.bar(dates, [x * pFCritical for x in plan_3_9], color='red',label='Next irrigation', linewidth=3)
secax_1_0.set_ylabel('pF log(-h)', color='orange')
secax_1_0.tick_params(axis='y', colors='orange')
secax_1_0.plot(dates, [pFCritical] * len(dates), color='orange',label='Critical pF', linestyle='dashed')
secax_1_0.set_ylim([min(pF_3_9)*0.97, max(pF_3_9)*1.03]) # just for scale purposes
axs[1,0].set_ylabel('% vol', color='black')
axs[1,0].legend(loc='upper right', frameon=False)



axs[1,1].set_title('Soil Moisture, 9 to 27 cm')
axs[1,1].plot(dates, SoilMoisture_9_27, color='black', label='Soil moisture (9-27)')
axs[1,1].set_ylabel('% / % ', color='black')
axs[1,1].legend(loc='upper right', frameon=False)
secax_1_1 = axs[1,1].twinx()  # instantiate a second axes that shares the same x-axis
secax_1_1 .plot(dates, pF_9_27, color='orange',label='pF')
secax_1_1.set_ylabel('pF log(-h)', color='orange')
secax_1_1 .plot(dates, [pFCritical] * len(dates), color='orange',label='Critical pF', linestyle='dashed')
secax_1_1.bar(dates, [x * pFCritical for x in plan_9_27] , color='red',label='Next irrigation', linewidth=3)
secax_1_1.set_ylim([min(pF_9_27)*0.97, max(pF_9_27)*1.03]) # just for scale purposes

secax_1_1.legend(loc='upper left', frameon=False)

axs[1,0].tick_params(axis='x', labelrotation=60)
axs[1,0].xaxis.set_major_locator(MultipleLocator(12))
axs[1,0].set_xlabel('DayHour')
axs[1,1].tick_params(axis='x', labelrotation=60)
axs[1,1].xaxis.set_major_locator(MultipleLocator(12))
axs[1,1].set_xlabel('DayHour')

# adding Label to the y-axis
#plt.autoscale(enable=True, axis='both', tight=True)
plt.tight_layout()
# adding legend to the curves
plt.legend()
plt.show()