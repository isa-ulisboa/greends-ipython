import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator)
import numpy as np
import material
import argparse
import group1_output
import group2_output

parser = argparse.ArgumentParser()
parser.add_argument ("--latitude", type = float, required = True)
parser.add_argument ("--longitude", type = float, required = True)
parser.add_argument ("--soiltype", type = int, required = True) 
parser.add_argument ("--pFCritical", type = float, required = True)
parser.add_argument ("--next24rain_treshold", type = float, required = True)
parser.add_argument ("--vpd_treshold", type = float, required = True)

args = parser.parse_args()

#The endpoint (Group 3) develops an API to collect data from user with argparse:
#Latitude - in decimal degrees
#Longitude - in decimal degrees
#Soiltype - an integer 1-5 corresponding to the 5 FAO soil textural classes 1-5 FAO class (1-coarse, 2-Medium, 3-Medium-Fine, 4-Fine, 5-Very Fine)
#pFCritical - the soil tension from which there is plant specific stress (pF at field capacity:2.3, pF at wilting point:4.2)
#Next24Rain_treshold - the ammount of rain forecasted in the next 24h, that could prevent the irrigation event
#VPD_treshold - Vapour Pressure Deficit, below which transpiration is unlikely to occur 

#test your application with
#Latitude - 37.64
#Longitude - -7.66
#Soiltype - 3
#pFCritical - 3.1
#Next24Rain_treshold - 2
#VPD_treshold - 0.5

# 1 -Organize your user input data for easier reading

inLat                     = args.latitude # replace this value with what you collect with your API
inLon                     = args.longitude # replace this value with what you collect with your API
inSoilType                = args.soiltype # replace this value with what you collect with your API
inpFCritical              = args.pFCritical # replace this value with what you collect with your API
invpd_treshold            = args.vpd_treshold # replace this value with what you collect with your API
innext24h_rain_treshold   = args.next24rain_treshold # replace this value with what you collect with your API

# 2 - Create a dictionary of weather forecast with the group1 work. In the meantime you can use material.Output1Group1 as a mockup result
Forecast = group1_output.getHourlyWeatherForescast(inLat,inLon)

# 3 - Organize your data series
dates = Forecast['hourly']['time']
dates = list(map(lambda x: x[-8:-3], dates))# just to get the Day and Hour
#... continue to create the following lists and populate them with forecasted data
temp = list(Forecast['hourly']['temperature_2m']) # replace the empty list with result of group1 work
vpd = list(Forecast['hourly']['vapor_pressure_deficit']) # replace the empty list with result of group1 work
rh = list(Forecast['hourly']['relativehumidity_2m']) # replace the empty list with result of group1 work
ETo = list(Forecast['hourly']['et0_fao_evapotranspiration']) # replace the empty list with result of group1 work
precipitation = list(Forecast['hourly']['precipitation']) # replace the empty list with result of group1 work
SoilMoisture_3_9 = list(Forecast['hourly']['soil_moisture_3_9cm']) # replace the empty list with result of group1 work
SoilMoisture_9_27 = list(Forecast['hourly']['soil_moisture_9_27cm'])# replace the empty list with result of group1 work

SoilMoisture_3_9 = SoilMoisture_3_9[:]
SoilMoisture_9_27 = SoilMoisture_9_27[:]

# 4 Use group2 function to create the soil tension (pF) dataseries for the two soil layers. 

pF_3_9= group2_output.get_pF_forecast(SoilMoisture_3_9, str(inSoilType)) # replace the empty list with result of group2 work
pF_9_27= group2_output.get_pF_forecast(SoilMoisture_9_27, str(inSoilType)) # replace the empty list the list with result of group2 work

#Decision to irrigate ( 3-9 cm)
plan_3_9 = [0] * len(dates) # replace the empty list with a list with same nr elements as 'dates', but filled with zeros
plan_9_27 = [0] * len(dates) # replace the empty list with a list with same nr elements as 'dates', but filled with zeros
plan_3_9_dates = [] # leave as is. This list will store the irrigation event for this soil layer
plan_9_27_dates = [] # leave as is. This list will store the irrigation event for this soil layer

# Decision algorithm to trigger irrigation event - Improve if you feel it nees improvement
# Rules: 1) soil tension is higher than pFCritical, 2) VPD is higher than vpd_treshold, 3) the sum of rain in the next 24 hours is less than 1 liter per m2

for idx,i in enumerate(vpd):
    next24_rain = sum(precipitation[idx:idx+24])
    if pF_3_9[idx]>=inpFCritical and vpd[idx] > invpd_treshold and next24_rain < innext24h_rain_treshold:
        if sum(filter(None, plan_3_9))<1:
            plan_3_9[idx] = 1
            plan_3_9_dates.append(dates[idx])
    if pF_9_27[idx]>=inpFCritical and vpd[idx] > invpd_treshold and next24_rain < innext24h_rain_treshold:
         if sum(filter(None, plan_9_27))<1:
            plan_9_27[idx] = 1
            plan_9_27_dates.append(dates[idx])





            # you don't want to worry about this section - only that it needs the variables
###################################################### VISUALIZATION ################################################
       
fig, axs = plt.subplots(2,2,sharex=True)
fig.suptitle('Green DS Master - Decision Support tool for irrigation needs. Current weather & soil retrieved from open-meteo.com\n'+
             'Irrigation criteria: pF > ' + str(inpFCritical) + ", VPD > " + str(invpd_treshold)+ ", no rain next day that allows pF < " + str(inpFCritical) + "\n"+
             "Next irrigation event for early rooting (3-9cm):" + str(plan_3_9_dates[0]) + "\n"+
             "Next irrigation event for established roots (9-27cm):" + str(plan_9_27_dates[0]) )
fig.set_size_inches(12,5)
axs[0,0].set_title('Temperature / VPD')
axs[0,0].plot(dates, temp, color='orange', label='Temp')
axs[0,0].set_ylabel('Celsius', color='orange')
secax_0_0 = axs[0,0].twinx()  # instantiate a second axes that shares the same x-axis
secax_0_0.plot(dates, vpd, color='blue')
secax_0_0.set_ylabel('VPD (kPa)', color='blue')
secax_0_0.fill_between(dates, vpd, invpd_treshold,  where=(np.array(vpd) >= np.array([invpd_treshold] * len(vpd))),
                 alpha=0.30, color='blue', label='VPD > '+str(invpd_treshold))
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
secax_1_0.bar(dates, [x * inpFCritical for x in plan_3_9], color='red',label='Next irrigation', linewidth=3)
secax_1_0.set_ylabel('pF log(-h)', color='orange')
secax_1_0.tick_params(axis='y', colors='orange')
secax_1_0.plot(dates, [inpFCritical] * len(dates), color='orange',label='Critical pF', linestyle='dashed')
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
secax_1_1 .plot(dates, [inpFCritical] * len(dates), color='orange',label='Critical pF', linestyle='dashed')
secax_1_1.bar(dates, [x * inpFCritical for x in plan_9_27] , color='red',label='Next irrigation', linewidth=3)
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