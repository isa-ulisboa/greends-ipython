import sys
sys.path.append(r'C:/Users/gast/Documents/LISSABON/newIP/greends-ipython/FORGE/Ellavandevreken')

import pandas as pd
import myFunctions as mf
import matplotlib.pyplot as plt

#read csv files and skip first row
Current = pd.read_csv('../../Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv', skiprows=[0])
Future = pd.read_csv('../../Climate_hisafe_knmircp85_daily_from_01-01-2006_to_31-12-2100.csv', skiprows=[0])


# create additional vpd column
Current["VPD"] = mf.calculate_vpd(Current["tasmax"],Current["tasmin"],Current["hurs"] )
Future["VPD"] = mf.calculate_vpd(Future["tasmax"],Future["tasmin"],Future["hurs"] )

##future starts at 2006 and ends at 2100 but we only want from 2031 until 2060 => select these years

Future = Future[(Future["Year"] >= 2031) & (Future["Year"] <= 2060)]

# calculate monthly averages
monthly_av_past = Current.groupby(['Month']).mean()
monthly_av_future = Future.groupby(['Month']).mean()

#graph
monthly_av_past["VPD"].plot(label = "Current (1981-2010)", color = "blue")
monthly_av_future["VPD"].plot(label = "Future (2031-2060)", color = "red")

#aesthetics
plt.title("Current and future climate: monthly averages of vapor pressure deficit")

plt.xlabel("Month")
plt.ylabel("VPD (kPa)")

plt.legend()

plt.show()

