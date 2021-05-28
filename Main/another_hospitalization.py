<<<<<<< HEAD
import requests 
import pandas
import json

with open('C:/Users/86183/Documents/Tencent Files/907881557/FileRecv/state_name.json') as state:
    state=json.load(state)
# read in the state name file and change the .json into a dict

for key in state:
    hospitalization=requests.get('https://jhucoronavirus.azureedge.net/api/v1/timeseries/us/hospitalization/{}.json'.format(key))
    hospitalization=hospitalization.json()
    hospitalization=hospitalization[0]
# change the .json into a dict

    data=pandas.DataFrame.from_dict(hospitalization,orient=('index'))
    data.to_csv('C:/Git/Power-Pill/Main/output/{}_hospitalization.csv'.format(state[key]))
# generate a .csv whose name can be filled with the state name automatically
=======
#hospitalization for all states which, compared with the previous one, show earlier but less detailed data
import requests
import pandas
import json
with open(
        'C:/Users/86183/Documents/Tencent Files/907881557/FileRecv/state_name.json'
) as state: #read in the state name file
    state = json.load(state) #change the .json into a dict
for key in state: #go through every element
    hospitalization = requests.get(
        'https://jhucoronavirus.azureedge.net/api/v1/timeseries/us/hospitalization/{}.json'
        .format(key)) #fill the .json name automatically
    hospitalization = hospitalization.json(
    ) #change the .json into a list whose element number is one
    hospitalization = hospitalization[0] #change the list into a dict
    data = pandas.DataFrame.from_dict(
        hospitalization, orient=('index')) #change the dict into .csv
    data.to_csv(
        'C:/Git/Power-Pill/Main/output/{}_hospitalization.csv'.format(
            state[key])
    ) #generate a .csv whose name can be filled with the state name automatically
#'https://jhucoronavirus.azureedge.net/jhucoronavirus/testing/jh-covid-tool.v3.json'(TESTING OVERVIEW). Perhaps necessary
>>>>>>> 92ec19a89621524288f5de777d303045fd7877c5
