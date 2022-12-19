
import pandas as pd
import datetime


def validate(file, date):
    wrk_y = file['Year']
    wrk_m = file['Month']
    wrk_d = file['Day']
    wrk_vpd = file['vpd']

    size = wrk_y.size

    for index in range(size):
        wrk_date = datetime.date(wrk_y[index],wrk_m[index],wrk_d[index])
        if wrk_date == date:
            return wrk_vpd[index]

