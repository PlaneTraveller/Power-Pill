import requests 
import pandas

timeline=requests.get('https://coronavirus.jhu.edu/datasets/state_timeline.json')
timeline=timeline.json()
# change the .json into a dict

for key in timeline:
    data=pandas.DataFrame({},index=['new_confirmed_cases_average','new_confirmed_cases_value','new_confirmed_cases_cumulative','new_deaths_average','new_deaths_value','new_deaths_cumulative'])
# summon an empty dataframe

    data_with_events=timeline[key]
    values=data_with_events['values']
    new_confirmed_cases=values['new-confirmed-cases']
    new_deaths=values['new-deaths']
# pick out useful data

    for i in range(0,len(new_confirmed_cases)):
        new_confirmed_cases_date=new_confirmed_cases[i]
        new_deaths_date=new_deaths[i]
# every element, in form of a dict, in the list is the data for a certain date

        new_confirmed_cases_date['new_confirmed_cases_average']=new_confirmed_cases_date.pop('average')
        new_confirmed_cases_date['new_confirmed_cases_value']=new_confirmed_cases_date.pop('value')
        new_confirmed_cases_date['new_confirmed_cases_cumulative']=new_confirmed_cases_date.pop('cumulative')
        new_deaths_date['new_deaths_average']=new_deaths_date.pop('average')
        new_deaths_date['new_deaths_value']=new_deaths_date.pop('value')
        new_deaths_date['new_deaths_cumulative']=new_deaths_date.pop('cumulative')
#keep the column name of the dataframe and the column name of the .csv the same

        new_confirmed_cases_columns=pandas.DataFrame.from_dict(new_confirmed_cases_date,orient=('index'))
        new_deaths_columns=pandas.DataFrame.from_dict(new_deaths_date,orient=('index'))
        new_deaths_columns=new_deaths_columns.drop(index='dt')
        columns=pandas.concat([new_confirmed_cases_columns,new_deaths_columns])
        data[new_deaths_date['dt']]=columns
#combine the two dataframe and then add the column to the dataframe

    output=pandas.DataFrame(data)
    output=output.T
    output.to_csv('C:/Git/Power-Pill/Main/output/{}_timeline.csv'.format(key))
# generate a .csv whose name can be filled with the state name automatically