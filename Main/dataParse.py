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
#===
#=== Inputting rawJson
#===
with open('./Main/input/rawJson.json') as fl:
    rawDat = json.loads(fl)

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
