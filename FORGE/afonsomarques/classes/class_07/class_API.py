import urllib.request
import json
import time
import datetime
import pandas as pd


url = 'https://cloud.iot.ativepoint.com/api/auth'
f = urllib.request.urlopen(url)
res = json.loads (f.read().decode('utf-8'))

print (res)
