import requests as req
import json
import pandas as pd

# Obtaining date csv
'''
fl = pd.read_csv('./Main/Output/California.csv')
d = list(fl.iloc[:, 0])
ds = pd.Series(d)
ds.to_csv('./Main/input/Date.csv')
'''

#===
#=== Retrieving Input data
#===
with open('./Main/input/state_name.json') as fl:
    stateStr = fl.read()
stateDict = json.loads(stateStr)

dateDF = pd.read_csv('./Main/input/Date.csv')
date = dateDF.iloc[:, 1]


#===
#=== Main Crawler: Changing State Abbr. in URL
#===
def getDF(siteFrame):
    # Initialization
    ret = {}
    # Obtaining data as dictionary

    for k in stateDict:

        site = siteFrame.format(k)
        reqResp = req.get(site, timeout=10)
        datDic = reqResp.json()

        # Rudementary Data Structuring
        ret[k] = datDic

        if '{}' not in siteFrame:
            break

    return ret


#===
#=== Data Crawling
#===

urlDict = {
    'rawPost':
    'https://jhucoronavirus.azureedge.net/api/v1/timeseries/us/cases/{}.json',
    'D&C':
    'https://coronavirus.jhu.edu/datasets/state_timeline.json',
    'Vaccination':
    'https://jhucoronavirus.azureedge.net/api/v1/timeseries/us/vaccines/{}.json'
}

rawDat = urlDict

for k in urlDict:
    rawDat[k] = getDF(urlDict[k])

#===
#=== Outputting
#===

rawJson = json.dumps(rawDat, indent=4)
with open('./Main/input/rawJson.json', 'w') as fl:
    fl.write(rawJson)
