import requests 
import pandas
import json

a=requests.get('https://jhucoronavirus.azureedge.net/jhucoronavirus/state_vaccination_rates.json')
a=a.json()
name=globals()
global c
for i in range(0,len(a)):
    b=a[i]
    c=b['state']
    d=b['data']
    e=d['raw_full_vac']
    f=d['percent_full_vac']
# pick out date used for caculate population

    population=dict(state=int(100*e/f))
    population[c]=population.pop('state')
    g=pandas.DataFrame.from_dict(population,orient=('index'))
    g.columns=['population']
    name['g'+str(i)]=g
# population for evert state is named differently

for i in range(0,len(a)-1):
    g0=pandas.concat([g0,name['g'+str(i+1)]])
g0.to_csv('C:/Git/Power-Pill/Main/output/population.csv')
# all populations are combined and output

a=requests.get('https://jhucoronavirus.azureedge.net/jhucoronavirus/hospitalization_by_state.json')
a=a.json()
with open('C:/Users/86183/Documents/Tencent Files/907881557/FileRecv/state_name.json') as state:
    state=json.load(state)
# preparation

for i in range(0,len(a)):
    b=a[i]
    if b['state']=='VI':
        name['rate'+str(i)]=None
# an unknown data, removed

    else:
        b=b['data']
        b=b['inpatient']
        b=b['covid']
        rate=dict(state=b)
        rate=pandas.DataFrame.from_dict(rate,orient=('index'))
        name['rate'+str(i)]=rate
for i in range(0,len(a)-1):
    rate0=pandas.concat([rate0,name['rate'+str(i+1)]])
# hospitalizaton rate for every state for this week is picked out

i=0
for key in state:
    a=requests.get('https://jhucoronavirus.azureedge.net/api/v1/timeseries/us/hospitalization/{}.json'.format(key))
    a=a.json()
    a=a[0]
    a=pandas.DataFrame.from_dict(a,orient=('index'))
    b=a[-1:]
    b.index=[state[key]]
    b=b.loc[state[key],'7_day_avg']
    value=dict(state=b)
    value=pandas.DataFrame.from_dict(value,orient=('index'))
    name['value'+str(i)]=value
    n=i
    i=i+1
    a=a.loc[:,['inpatient_beds_used_covid']]    # hospitalization value for all dates
for i in range(0,n):
    value0=pandas.concat([value0,name['value'+str(i+1)]])
# hospitalization value for every state for this week is picked out

rate_and_value=pandas.concat([rate0,value0],axis=1)
beds=value0.div(rate0)
beds.columns=['beds']
# the beds' number is caculated

beds=beds.multiply(100)
# can be deleted to make the result combined with %

for key in state:
    i=0
    value=beds[i:i+1]
    i=i+1
    value=value.loc['state','beds']
    hospitalization=a.div(value)
    hospitalization.to_csv('C:/Git/Power-Pill/Main/output/{}_hospitalization.csv'.format(state[key]))
# the final rate