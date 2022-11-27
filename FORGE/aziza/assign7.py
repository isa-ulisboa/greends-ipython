import sys
import pandas as pd
import myfunctions as f
import matplotlib.pyplot as plt
#(Facultative) setting path to get your myfunctions 
sys.path.append('../FORGE/aziza')
# Open the file "Climate_hisafe_knmievaluation_daily..." as Current
Current = pd.read_csv("Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv", skiprows = [0])
# Open the file "Climate_hisafe_knmircp85_daily..." as Future
Future = pd.read_csv("Climate_hisafe_knmircp85_daily_from_01-01-2006_to_31-12-2100.csv", skiprows = [0])
# Calculate VPD with pandas (your vpd function should work with numpy instead math library)
# The following creates an additional column called "VPD" where your function is used
Current["VPD"] = f.calculate_vpd(Current["tasmax"], Current["tasmin"], Current["hurs"])
Future["VPD"] = f.calculate_vpd(Future["tasmax"], Future["tasmin"], Future["hurs"])
print(Current)
print(Future)
#calculate the monthly average from 1981 to 2010 (file with current climate)
avg_1981_2010=Current.groupby(["Month"]).mean()
print (avg_1981_2010)
#calculate the monthly average from 2031 to 2060
New_future=Future[(Future["Year"] >= 2031) & (Future["Year"] <= 2060)]
avg_2031_2060= New_future.groupby(["Month"]).mean()
print(avg_2031_2060)
#plot a simple graph with Maptplotlib of VPD from current and future climate
avg_1981_2010["VPD"].plot(label = "Current vpd", color = "black")
avg_2031_2060["VPD"].plot(label = "Future vpd", color = "red")
plt.show()
