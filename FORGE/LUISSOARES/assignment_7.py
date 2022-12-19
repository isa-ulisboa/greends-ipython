import sys
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import myFunctions as mf

# (Facultative) setting path to get your myfunctions 
# sys.path.append('../FORGE/JOAOPALMA') # This adds your modules if your module is somewhere else not script folder or subfolders

Current = pd.read_csv('Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv', skiprows=[0])
Future = pd.read_csv('Climate_hisafe_knmircp85_daily_from_01-01-2006_to_31-12-2100.csv', skiprows=[0])

# Calculate VPD with pandas (your vpd function should work with numpy instead math library)
# The following creates an additional column called "VPD" where your function is used
Current["VPD"] = mf.calculate_vpd(Current["tasmax"],Current["tasmin"],Current["hurs"] )
Future["VPD"] = mf.calculate_vpd(Future["tasmax"],Future["tasmin"],Future["hurs"] )

# Calculate monthly averages
#Create a subset from 2031 to 2060
Future_2031_2060 = Future[(Future["Year"] >= 2031) & (Future["Year"] <= 2060)]

#Calculate monthly VPD averages

Current_monthly_avg = Current.groupby(["Month"]).mean()
Future_monthly_avg = Future_2031_2060.groupby("Month").mean()

#Plot a graph with Matplotlib

plt.figure()
Current_monthly_avg["VPD"].plot(label="1981-2010 VPD", color="orange")
Future_monthly_avg["VPD"].plot(label="2031-2060 VPD", color="blue")

#Add a title to the plot

plt.title("Avg VPD from 1981-2010 and prediction for 2031-2060")

#Add lable to the x-axis and y-axis

plt.xlabel("Month")
plt.ylabel("VPD (kPa)")

#Adding a legend to the curves

plt.legend()


plt.show()