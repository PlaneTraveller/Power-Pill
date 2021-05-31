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


def datStruct_Single(datStruct, parsedSing):
    ret = datStruct
    ret = pd.concat([ret, parsedSing])
    return ret


datList = []
singList = []

#===
#=== Parsing
#===

# Inputting Json
with open('./Main/input/rawJson.json') as fl:
    str1 = fl.read()
    rawDat = json.loads(str1)

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
    #    output = output.T
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
    #    output = output.T
    # Link
    buf = output.to_dict()
    vacOut[key] = buf
# Out: vacOut
datList.append(vacOut)

# Population
a = rawDat['P&H']

#= Code from Snippets
name = globals()
global c
for i in range(0, len(a)):
    b = a[i]
    c = b['state']
    d = b['data']
    e = d['raw_full_vac']
    f = d['percent_full_vac']
    # pick out date used for caculate population

    population = dict(state=int(100 * e / f))
    population[c] = population.pop('state')
    g = pd.DataFrame.from_dict(population, orient=('index'))
    g.columns = ['population']
    name['g' + str(i)] = g
# population for evert state is named differently
for i in range(0, len(a) - 1):
    g0 = pd.concat([g0, name['g' + str(i + 1)]])

#= Code End
PnHOut = g0
singList.append(PnHOut)

# Hospitalization and beds
HospRateOut = {}
a = rawDat['Hosp1']
a2 = rawDat['Hosp2']

#= Code from Snippets

for i in range(0, len(a)):
    b = a[i]
    if b['state'] == 'VI':
        name['rate' + str(i)] = None
# an unknown data, removed

    else:
        b = b['data']
        b = b['inpatient']
        b = b['covid']
        rate = dict(state=b)
        rate = pd.DataFrame.from_dict(rate, orient=('index'))
        name['rate' + str(i)] = rate
for i in range(0, len(a) - 1):
    rate0 = pd.concat([rate0, name['rate' + str(i + 1)]])
# hospitalizaton rate for every state for this week is picked out

i = 0
for key in a2:
    a = a2[key]
    a = a[0]
    a = pd.DataFrame.from_dict(a, orient=('index'))
    b = a[-1:]
    b.index = [stateDict[key]]
    b = b.loc[stateDict[key], '7_day_avg']
    value = dict(state=b)
    value = pd.DataFrame.from_dict(value, orient=('index'))
    name['value' + str(i)] = value
    n = i
    i = i + 1
    a = a.loc[:, ['inpatient_beds_used_covid'
                  ]] # hospitalization value for all dates
for i in range(0, n):
    value0 = pd.concat([value0, name['value' + str(i + 1)]])
# hospitalization value for every state for this week is picked out

rate_and_value = pd.concat([rate0, value0], axis=1)
beds = value0.div(rate0)
beds.columns = ['beds']
# the beds' number is caculated

beds = beds.multiply(100)
# can be deleted to make the result combined with %

for key in stateDict:
    i = 0
    value = beds[i:i + 1]
    i = i + 1
    value = value.loc['state', 'beds']
    hospitalization = a.div(value)
    hospitalization = hospitalization.T

#= Code End
HospRateOut = hospitalization
datList.append(HospRateOut)

beds.reindex_like(hospitalization)
bedCountOut = beds
covSingle.append(bedCountOut)

#===
#=== Outputting
#===

# Feeding into datStruct_Indexed
structIndexed = covDateIndexed
for item in datList:
    structIndexed = datStruct_Indexed(structIndexed, item)

# Feeding into datStruct_Indexed
structSingle = covSingle
for item in singList:
    structSingle = datStruct_Single(structSingle, item)

structIndexed.to_csv('./Main/outPut/StructIndexed.csv')
structSingle.to_csv('./Main/outPut/StructSingle.csv')

#UltiJson = struct.to_json()
#
#rawJson = json.dumps(UltiJson, indent=4)
#
#with open('./Main/outPut/UltiJson.json', 'w') as fl:
#    fl.write(UltiJson)
