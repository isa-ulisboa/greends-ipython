

path_assg_7 = "FORGE/afonsomarques/myForge/assg_7/"
file_2010 = "Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv"
file_2100 = 'Climate_hisafe_knmircp85_daily_from_01-01-2006_to_31-12-2100.csv'

import pandas as pd
import function as f
import csv 
import matplotlib.pyplot as plt
Current = pd.read_csv(file_2010, skiprows=[0], index_col=False)
Future = pd.read_csv(file_2100, skiprows=[0], index_col=False)

# Calculate VPD with pandas (your vpd function should work with numpy instead math library)
# The following creates an additional column called "VPD" where your function is used
Current["VPD"] = f.vap_pres_def(Current["tasmax"],Current["tasmin"],Current["hurs"] )
Future["VPD"] = f.vap_pres_def(Future["tasmax"],Future["tasmin"],Future["hurs"] )


Current.to_csv(path_assg_7+'climate_data+vpd_1981-2010.csv')
Future.to_csv(path_assg_7+'climate_data+vpd_2006-2100.csv')


mean_c_mth = Current.groupby(['Month']).mean()
print(mean_c_mth['VPD'])

mean_f_mth = Future.groupby(['Month']).mean()
print(mean_f_mth['VPD'])

mean_c_mth['VPD'].plot(label='Current vpd', color='red')
mean_f_mth['VPD'].plot(label='Future vpd', color='green')



plt.show()







































