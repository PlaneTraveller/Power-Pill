import requests
import pandas
import json

with open('./Main/input/state_name.json') as state:
    state = json.load(state)
# read in the state name file and change the .json into a dict

for key in state:
    hospitalization = requests.get(
        'https://jhucoronavirus.azureedge.net/api/v1/timeseries/us/hospitalization/{}.json'
        .format(key))
    hospitalization = hospitalization.json()
    hospitalization = hospitalization[0]
    # change the .json into a dict
    data = pandas.DataFrame.from_dict(hospitalization, orient=('index'))
    data.to_csv('C:/Git/Power-Pill/Main/output/{}_hospitalization.csv'.format(
        state[key]))
# generate a .csv whose name can be filled with the state name automatically
