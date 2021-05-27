import requests 
import pandas
import json
with open('C:/Users/86183/Documents/Tencent Files/907881557/FileRecv/state_name.json') as state:    #read in the state name file
    state=json.load(state)  #change the .json into a dict
for key in state:   #go through every element(state)
    vaccinations=requests.get('https://jhucoronavirus.azureedge.net/api/v1/timeseries/us/vaccines/{}.json'.format(key))   #fill the .json name automatically
    vaccinations=vaccinations.json()  #change the .json into a list
    data=pandas.DataFrame({},index=['doses_admin_daily','7_day_avg'])   #summon an empty dataframe
    for i in range(0,len(vaccinations)):    #go through every element(date)
        v=vaccinations[i]   #pick out an element(dict)
        columns=pandas.DataFrame.from_dict(v,orient=('index'))  #change the dict into a column of a datafrane
        data[v['date']]=columns #add the column to the dataframe
    output=pandas.DataFrame(data,index=['doses_admin_daily','7_day_avg'])   #change the dict into a .csv
    output.to_csv('C:/Git/Power-Pill/Main/output/{}_vaccinations.csv'.format(state[key])) #generate a .csv whose name can be filled with the state name automatically