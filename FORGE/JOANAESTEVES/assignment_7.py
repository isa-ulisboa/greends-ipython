import sys
sys.path.append('c:/Users/joana/Desktop/GDS/INTPY/greends-ipython-1/FORGE/JOANAESTEVES')

# We need pandas and myfunctions file for this exercise
import pandas as pd
import myFunctions as mf

Current = pd.read_csv('c:/Users/joana/Desktop/GDS/INTPY/greends-ipython-1/Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv', skiprows=[0])
Future = pd.read_csv('c:/Users/joana/Desktop/GDS/INTPY/greends-ipython-1/Climate_hisafe_knmircp85_daily_from_01-01-2006_to_31-12-2100.csv', skiprows=[0])

# To add a new column at the end of the table we use the [] operator
Current['VPD'] = mf.calculate_vpd(Current['tasmax'], Current['tasmin'], Current['hurs'])
Future['VPD'] = mf.calculate_vpd(Future['tasmax'], Future['tasmin'], Future['hurs'])

# We just want an average from 1981 to 2010 in the Current function, and from 2031 to 2060 in the Future function
new_current = Current[(Current['Year'] >= 1981) & (Current['Year'] <= 2010)]
new_future = Future[(Future['Year'] >= 2031) & (Future['Year'] <= 2060)]

# To calculate the monthly average
mean_current = new_current.groupby(['Month']).mean()
mean_future = new_future.groupby(['Month']).mean()

"""
print(mean_current['VPD'])
print(mean_future['VPD'])
"""

# Plot a graph with matplotlib of VPD current and future climate

import matplotlib.pyplot as plt
mean_current['VPD'].plot(label='VPD')
mean_future['VPD'].plot(label='VPD')
plt.show()