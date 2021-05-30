import requests 
import pandas
import json

with open('C:/Users/86183/Documents/Tencent Files/907881557/FileRecv/state_name.json') as state:
    state=json.load(state)  # read in the state name file and change the .json into a dict
for key in state:
    vaccinations=requests.get('https://jhucoronavirus.azureedge.net/api/v1/timeseries/us/vaccines/{}.json'.format(key))
########## json!!!!!!!!!!

    vaccinations=vaccinations.json()
# change the .json into a list

    data=pandas.DataFrame({},index=['doses_admin_daily','7_day_avg'])
# summon an empty dataframe

    for i in range(0,len(vaccinations)):
        v=vaccinations[i]
# every element, in form of a dict, in the list is the data for a certain date

        columns=pandas.DataFrame.from_dict(v,orient=('index'))
        data[v['date']]=columns
# add the column to the dataframe

    output=pandas.DataFrame(data)
    output=output.T
########## DataFrame!!!!!!!!!!

    output.to_csv('C:/Git/Power-Pill/Main/output/{}_vaccinations.csv'.format(state[key]))
# generate a .csv whose name can be filled with the state name automatically