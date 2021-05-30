import requests 
import pandas
import json

with open('C:/Users/86183/Documents/Tencent Files/907881557/FileRecv/state_name.json') as state_name:
    state_name=json.load(state_name)
# read in the state name file and change the .json into a dict

def url(json):
    url=requests.get(json)
    return url.json()
for name in state_name:
    timeline=url('https://coronavirus.jhu.edu/datasets/state_timeline.json')
    hospitalization1=url('https://jhucoronavirus.azureedge.net/api/v1/timeseries/us/hospitalization/{}.json'.format(name))
    hospitalization1=hospitalization1[0]
    vaccinations=url('https://jhucoronavirus.azureedge.net/api/v1/timeseries/us/vaccines/{}.json'.format(name))
    hospitalization2=url('https://jhucoronavirus.azureedge.net/jhucoronavirus/hospitalization_by_state.json')
# change the .json into a dict

    data=pandas.DataFrame({},index=[])
    basic_data=pandas.DataFrame({},index=['new_confirmed_cases_average','new_confirmed_cases_value','new_confirmed_cases_cumulative','new_deaths_average','new_deaths_value','new_deaths_cumulative'])
    vaccinations_data=pandas.DataFrame({},index=['doses_admin_daily','7_day_avg'])

# summon an empty dataframe

    state_timeline=timeline[state_name[name]]
    state_timeline=state_timeline['values']
    new_confirmed_cases=state_timeline['new_confirmed_cases']
    new_deaths=state_timeline['new_deaths']
# pick out useful data

def date(data):
    i=0
    name=globals()
    while not data==[]:
        name[data+'_date_'+i]=data[0]
        i=i+1
        del data[0]
date(new_confirmed_cases)
n=globals()
n=0
while name['new_confirmed_cases_date_'+n]:
    name['new_confirmed_cases_date_'+n]['new_confirmed_cases_average']=name['new_confirmed_cases_date_'+n].pop('average')
    name['new_confirmed_cases_date_'+n]['new_confirmed_cases_value']=name['new_confirmed_cases_date_'+n].pop('value')
    name['new_confirmed_cases_date_'+n]['new_confirmed_cases_cumulative']=name['new_confirmed_cases_date_'+n].pop('cumulative')
    n=n+1
n=0
while name['new_deaths_date_'+n]:
    name['new_deaths_date_'+n]['new_deaths_average']=name['new_deaths_date_'+n].pop('average')
    name['new_deaths_date_'+n]['new_deaths_value']=name['new_deaths_date_'+n].pop('value')
    name['new_deaths_date_'+n]['new_deaths_cumulative']=name['new_deaths_date_'+n].pop('cumulative')    
date(new_deaths)
date(vaccinations)

# 
while name['new_confirmed_cases_date_'+n]:
    name['new_confirmed_cases_columns_'+n]=pandas.DataFrame.from_dict(name['new_confirmed_cases_date_'+n],orient=('index'))
while name['new_deaths_date_'+n]:
    name['new_deaths_columns_'+n]=pandas.DataFrame.from_dict(name['new_deaths_date_'+n],orient=('index'))
    name['new_deaths_columns_'+n]=name['new_deaths_columns_'+n].drop(index='dt')
    name['basic_data_columns_'+n]=pandas.concat([name['new_confirmed_cases_columns_'+n],name['new_deaths_columns_'+n]])





break
#useless
    for i in range(0,len(state_name)):
        new_confirmed_cases_date=new_confirmed_cases[i]
        new_deaths_date=new_deaths[i]
        new_confirmed_cases_date['new_confirmed_cases_average']=new_confirmed_cases_date.pop('average')
        new_confirmed_cases_date['new_confirmed_cases_value']=new_confirmed_cases_date.pop('value')
        new_confirmed_cases_date['new_confirmed_cases_cumulative']=new_confirmed_cases_date.pop('cumulative')
        new_deaths_date['new_deaths_average']=new_deaths_date.pop('average')
        new_deaths_date['new_deaths_value']=new_deaths_date.pop('value')
        new_deaths_date['new_deaths_cumulative']=new_deaths_date.pop('cumulative')
        vaccinations_date=vaccinations[i]
        state_hospitalization2=hospitalization2[i]
        state_hospitalization2=state_hospitalization2['data']
        inpatient=state_hospitalization2['inpatient']
        icu=state_hospitalization2['icu']
# every element in the list is the data for a certain date

        new_confirmed_cases_columns=pandas.DataFrame.from_dict(new_confirmed_cases_date,orient=('index'))
        new_deaths_columns=pandas.DataFrame.from_dict(new_deaths_date,orient=('index'))
        new_deaths_columns=new_deaths_columns.drop(index='dt')
        basic_data_columns=pandas.concat([new_confirmed_cases_columns,new_deaths_columns])
        basic_data[new_deaths_date['dt']]=basic_data_columns
        vaccinations_columns=pandas.DataFrame.from_dict(vaccinations_date,orient=('index'))
        vaccinations_data[vaccinations_date['date']]=vaccinations_columns
    basic_data_output=pandas.DataFrame(basic_data)
    basic_data_output=basic_data_output.T
    hospitalization1_output=pandas.DataFrame.from_dict(hospitalization1,orient=('index'))
    vaccinations_output=pandas.DataFrame(vaccinations_data)
    vaccinations_output=vaccinations_output.T
    


