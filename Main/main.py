import requests as req
import json
import pandas as pd

#--- Demo: Obtaining 52 csv files

# Retrieving Input data
with open('./Main/input/state_name.json') as fl:
    stateStr = fl.read()
stateDict = json.loads(stateStr)

# Main Crawler
# Obtaining data as dictionary
for k in stateDict:
    site = 'https://jhucoronavirus.azureedge.net/api/v1/timeseries/us/cases/' + k + '.json'
    reqResp = req.get(site, timeout=10)
    datDic = reqResp.json()

    # Data Structuring
    datDF = pd.DataFrame.from_dict(datDic, orient='index')

    # Data Output
    outPath = './Main/output/' + stateDict[k] + '.csv'
    datDF.to_csv(outPath)

#--- Demo Finish
