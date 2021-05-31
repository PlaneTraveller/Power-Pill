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
#=== Structuring function
#===


# Takes Json-style Dictionary as input, first keys being states, second being dates
def datStruct_Indexed(datStruct, parsedDF):
    ret = datStruct
    for state in parsedDF:
        iterList = []
        iterList.append(state)
        inp = pd.DataFrame.from_dict(parsedDF[state]).T
        multiInd = pd.MultiIndex.from_product(
            iterables=[iterList, list(inp.index)], names=['State', 'Date'])
        inp.index = multiInd
        ret = pd.concat([ret, inp])

    return ret


#===
#=== Parsing
#===

# Inputting Json
with open('./Main/input/rawJson.json') as fl:
    str = fl.read()
    rawDat = json.loads(str)

datList = []

# rawPositive (CHECK)
rawPositive = rawDat['rawPost']

datList.append(rawPositive)
# D&C
DnCOut = {}
timeline = rawDat['D&C']

#= Code from Snippets
for key in timeline:
    data = pd.DataFrame({},
                        index=[
                            'new_confirmed_cases_average',
                            'new_confirmed_cases_value',
                            'new_confirmed_cases_cumulative',
                            'new_deaths_average', 'new_deaths_value',
                            'new_deaths_cumulative'
                        ])
    # summon an empty dataframe

    data_with_events = timeline[key]
    values = data_with_events['values']
    new_confirmed_cases = values['new-confirmed-cases']
    new_deaths = values['new-deaths']
    # pick out useful data

    for i in range(0, len(new_confirmed_cases)):
        new_confirmed_cases_date = new_confirmed_cases[i]
        new_deaths_date = new_deaths[i]
        # every element, in form of a dict, in the list is the data for a certain date

        new_confirmed_cases_date[
            'new_confirmed_cases_average'] = new_confirmed_cases_date.pop(
                'average')

        new_confirmed_cases_date[
            'new_confirmed_cases_value'] = new_confirmed_cases_date.pop(
                'value')
        new_confirmed_cases_date[
            'new_confirmed_cases_cumulative'] = new_confirmed_cases_date.pop(
                'cumulative')
        new_deaths_date['new_deaths_average'] = new_deaths_date.pop('average')
        new_deaths_date['new_deaths_value'] = new_deaths_date.pop('value')
        new_deaths_date['new_deaths_cumulative'] = new_deaths_date.pop(
            'cumulative')
        #keep the column name of the dataframe and the column name of the .csv the same

        new_confirmed_cases_columns = pd.DataFrame.from_dict(
            new_confirmed_cases_date, orient=('index'))
        new_deaths_columns = pd.DataFrame.from_dict(new_deaths_date,
                                                    orient=('index'))
        new_deaths_columns = new_deaths_columns.drop(index='dt')
        columns = pd.concat([new_confirmed_cases_columns, new_deaths_columns])
        data[new_deaths_date['dt']] = columns
#combine the two dataframe and then add the column to the dataframe

    output = pd.DataFrame(data)
    output = output.T
    #= Code End

    # Link
    buf = output.to_dict()
    short = list(stateDict.keys())[list(stateDict.values()).index(key)]
    DnCOut[short] = buf

# Out: DnCOut
datList.append(DnCOut)

# Vaccination
vacDat = rawDat['Vaccination']
vacOut = {}

#= Code from Snippets

for key in vacDat:
    vaccinations = vacDat[key]

    data = pd.DataFrame({}, index=['doses_admin_daily', '7_day_avg'])
    # summon an empty dataframe
    for i in range(0, len(vaccinations)):
        v = vaccinations[i]
        # every element, in form of a dict, in the list is the data for a certain date

        columns = pd.DataFrame.from_dict(v, orient=('index'))
        data[v['date']] = columns
        # add the column to the dataframe

    output = pd.DataFrame(data)
    output = output.T
    # Link
    buf = output.to_dict()
    vacOut[key] = buf

# Out: vacOut

datList.append(vacOut)

# Hospitalization
pass

# Feeding into datStruct_Indexed

struct = covDateIndexed
for item in datList:
    struct = datStruct_Indexed(struct, item)

#===
#=== Outputting
#===

struct.to_csv('./Main/outPut/Struct.csv')

#UltiJson = struct.to_json()
#
#rawJson = json.dumps(UltiJson, indent=4)
#
#with open('./Main/outPut/UltiJson.json', 'w') as fl:
#    fl.write(UltiJson)
