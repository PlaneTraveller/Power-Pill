import requests as req
import json
import pandas as pd

# Retrieving Input data
with open('./Main/input/state_name.json') as fl:
    stateStr = fl.read()
stateDict = json.loads(stateStr)


# Main Crawler
def getDF(siteFrame):
    # Initialization
    ret = pd.Series()

    # Obtaining data as dictionary
    for k in stateDict:
        site = siteFrame.format(k)
        reqResp = req.get(site, timeout=10)
        datDic = reqResp.json()

        # Data Structuring
        datDF = pd.DataFrame.from_dict(datDic, orient='index')
        ret.add()

    return ret


rawPost = 'https://jhucoronavirus.azureedge.net/api/v1/timeseries/us/cases{}.json'
datDF.to_csv(outPath)
# Data Output
outPath = './Main/output/' + stateDict[k] + '.csv'
