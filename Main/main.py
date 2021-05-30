import requests as req
import json
import pandas as pd
'''
Data choice: raw positive, 7-day-avg, * Vaccination, * Hospitalization, new_confirmed_cases_average, new_confirmed_cases_value, new_confirmed_cases_cumulative, new_deaths_average, new_deaths_value, new_deaths_cumulative

Single Data:
- Population
- Totals
- Beds
- Hospitalization 

DateIndexed Data:
- Positive (1/2) per day
- Positive average week
- Positive sum
- Death per day
- Death average week
- Death sum
- Hospitalization percentage per day (ICU/all)


'''

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
#=== Constructing Main Structure File
#===
''' Organizing data with two DataFrames
- States
    - Single
        - Death Total
        - Vaccination Total
    - DateIndexed
        - raw-positive
        - confirmed positvive
        - more
'''

#=== Constructing Single
covSingle = pd.DataFrame(index=stateDict)

#=== Constructing DateIndexed
# Constructing MultiIndex
iterables = [stateDict, date]
stateMuitiInd = pd.MultiIndex.from_product(iterables, names=['State', 'Date'])

# Constructing 3-D DataFrame
covDateIndexed = pd.DataFrame(index=stateMuitiInd)


#===
#=== Main Crawler: Changing State Abbr. in URL
#===
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


#===
#=== Data Structuring and Outputting
#===
rawPost = 'https://jhucoronavirus.azureedge.net/api/v1/timeseries/us/cases{}.json'
datDF.to_csv(outPath)
# Data Output
outPath = './Main/output/' + stateDict[k] + '.csv'
