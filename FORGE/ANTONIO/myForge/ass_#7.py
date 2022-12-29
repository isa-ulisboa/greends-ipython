#Assignment 7

import pandas as pd
import myFunctions as func
import matplotlib.pyplot as plt

# Open the file "Climate_hisafe_knmievaluation_daily..." as Current

Current = pd.read_csv("Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv", skiprows = [0])

# Open the file "Climate_hisafe_knmircp85_daily..." as Future

Future = pd.read_csv("Climate_hisafe_knmircp85_daily_from_01-01-2006_to_31-12-2100.csv", skiprows = [0])

# Calculate VPD with pandas (your vpd function should work with numpy instead math library)
# The following creates an additional column called "VPD" where your function is used

Current["VPD"] = func.calculate_vpd(Current["tasmax"], Current["tasmin"], Current["hurs"])

Future["VPD"] = func.calculate_vpd(Future["tasmax"], Future["tasmin"], Future["hurs"])

#print(Current)

# Create subsets Future file (with data from 2031 to 2060)

Future_2031_2060 = Future[(Future["Year"] >= 2031) & (Future["Year"] <= 2060)]

# Calculate variable monthly averages from Current_1981_2010 and Future_2031_2060 files

avg_Current = Current.groupby(["Month"]).mean()

#print(avg_Current)

avg_monthly_Future = Future_2031_2060.groupby(["Month"]).mean()

#print(avg_monthly_Future)


# Plot a simple graph with Maptplotlib of VPD from current and future climate

#plt.figure()

avg_Current["VPD"].plot(label = "Current vpd", color = "green")
avg_monthly_Future["VPD"].plot(label = "Future vpd", color = "blue")

# Adding title to the plot
plt.title("Average vapor deficit pressure 1981-2010 and 2031-2060 ")

# Adding label to the x-axis
plt.xlabel("Month")

# Adding label to the y-axis
plt.ylabel("vpd (kPa)")

#Adding a legend to the plot
plt.legend()

#Show the plot made previously 

plt.show()