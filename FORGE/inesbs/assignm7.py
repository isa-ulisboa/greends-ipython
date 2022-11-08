import sys
#sys.path.append(r'c:\Users\inesb\.ipython\greends-ipython\FORGE')
import pandas as pd
import myfunctions


current = pd.read_csv('Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv', header=1)
future = pd.read_csv('Climate_hisafe_knmircp85_daily_from_01-01-2006_to_31-12-2100_vpd.csv', header=1)


current.insert(10, column = "VPD", value = myfunctions.VPdef(current["tasmax"], current["tasmin"], current["hurs"]))
future.insert(10, column = "VPD", value = myfunctions.VPdef(future["tasmax"], future["tasmin"], future["hurs"]))

#print(current)

#current["VPD"] = myfunctions.VPdef(current["tasmax"], current["tasmin"], current["hurs"])
#future["VPD"] = myfunctions.VPdef(future["tasmax"], future["tasmin"], future["hurs"])




#Create a subset (new dataset)
#current1981_2010 = current[(current["Year"] >= 1981) & (Current["Year"] <= 2010)]
#future2031_2060 = future[(future["Year"] >=2031) & (future["Year"] <= 2060)]

#Calculating monthly averages
#avg_y=Current1981_2010.groupby(['Day','Month']).mean()
#print (avg_y.to_string()) 

#avg_m=Current1991_2010.groupby(['Month']).mean()
#print (avg_m.to_string()) 