import requests 
import pandas

hospitalization=requests.get('https://jhucoronavirus.azureedge.net/jhucoronavirus/hospitalization_by_state.json')
hospitalization=hospitalization.json()
# change the .json into a list

for i in range (0,len(hospitalization)):
    each=hospitalization[i]
# every element, in form of a dict, in the list is the data for a single state

    state=each['state']
    data=each['data']
    inpatient=data['inpatient']
    icu=data['icu']
# the data is separated into two dicts

    inpatient=pandas.DataFrame.from_dict(inpatient,orient='index')
    icu=pandas.DataFrame.from_dict(icu,orient='index')
# dataframe the dict

    inpatient.columns=['percentage']
    icu.columns=['percentage']
# fill the name of the column

    inpatient.to_csv('C:/Git/Power-Pill/Main/output/{}_inpatient.csv'.format(state))
    icu.to_csv('C:/Git/Power-Pill/Main/output/{}_icu.csv'.format(state))
# generate a .csv whose name can be filled with the state name automatically