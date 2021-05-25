import requests as req
import json
import pandas as pd

#=== Pending: Obtaining website URL

#=== Requesting data

#--- Demo: CA, raw positive
reqResp = req.get(
    'https://jhucoronavirus.azureedge.net/api/v1/timeseries/us/cases/CA.json')
datDic = reqResp.json()
datDF = pd.DataFrame.from_dict(datDic, orient='index')
datDF.to_csv('./Main/output/DemoOut.csv')

#--- Demo Finish
