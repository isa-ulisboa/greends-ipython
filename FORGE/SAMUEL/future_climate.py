import sys
# (Facultative) setting path to get your myfunctions 
sys.path.append('../FORGE/SAMUEL') # This adds your modules if your module is somewhere else not script folder or subfolders

import pandas as pd
import myFunctions
Current = pd.read_csv('Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv', skiprows=[0])
Future = pd.read_csv('Climate_hisafe_knmircp85_daily_from_01-01-2006_to_31-12-2100.csv', skiprows=[0])
#print(Current)
# Calculate VPD with pandas (your vpd function should work with numpy instead math library)
# The following creates an additional column called "VPD" where your function is used
Current["VPD"] = myFunctions.calculate_vpd_7(Current["tasmax"],Current["tasmin"],Current["hurs"] )
Future["VPD"] = myFunctions.calculate_vpd_7(Future["tasmax"],Future["tasmin"],Future["hurs"] )
#print(Current["tasmax"])

#Current.insert(10,column="VPD",value=Current["VPD"])
#Future.insert(10,column="VPD",value=Future["VPD"])