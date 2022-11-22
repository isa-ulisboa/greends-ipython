import sys
sys.path.append(r'c:\Users\inesb\.ipython\greends-ipython\FORGE')
import pandas as pd
import myfunctions
import csv
import numpy as np

#open with pandas and skip first row
current = pd.read_csv('Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv', skiprows=[0])
future = pd.read_csv('Climate_hisafe_knmircp85_daily_from_01-01-2006_to_31-12-2100.csv', skiprows=[0])


#insert column in position 10, named VPD with value calculated by the function ....
current.insert(10, column = "VPD", value = myfunctions.VPdef(current["tasmax"], current["tasmin"], current["hurs"]))
future.insert(10, column = "VPD", value = myfunctions.VPdef(future["tasmax"], future["tasmin"], future["hurs"]))


#Create a subset (new dataset)
current1981_2010 = current[(current["Year"] >= 1981) & (current["Year"] <= 2010)]
future2031_2060 = future[(future["Year"] >=2031) & (future["Year"] <= 2060)]

#Calculating monthly averages
c_mean = current1981_2010.groupby(['Month']).mean()
f_mean = future2031_2060.groupby(['Month']).mean()
print(c_mean['VPD'])

#plot graph
import matplotlib.pyplot as plt

c_mean['VPD'].plot(label='VPD', color='black')
f_mean['VPD'].plot(label='VPD', color='black')

plt.show()
