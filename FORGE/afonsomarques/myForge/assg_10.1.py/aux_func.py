
import pandas as pd
import datetime

data= pd.read_csv('Climate_hisafe_knmircp85_daily_from_01-01-2006_to_31-12-2100_vpd.csv',skiprows=1)

def validate(data):
    wrk_y = data['Year']
    wrk_m = data['Month']
    wrk_d = data['Day']
    wrk_vpd = data['vpd']

    size = wrk_y.size
    try:
        for index in range(size):
            date = datetime.date(wrk_y[index],wrk_m[index],wrk_d[index])
            #print(date, wrk_vpd[index])
            #print (date)
        return True
    except ValueError:
        return False

validate (data)





#x = datetime.datetime(wrk_y, 5, 17)
#
#print(size)




