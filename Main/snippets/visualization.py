import json
import pandas
from pyecharts.charts import Map
from pyecharts import options as opts
from pyecharts.options.global_options import TitleOpts

with open('C:/Users/86183/Documents/Tencent Files/907881557/FileRecv/state_name.json') as state:
    state=json.load(state)
state_name=list(state.values())

name=globals()
data_dict={}
for i in range(0,len(state_name)):
    data=pandas.read_csv('C:/Git/Power-Pill/Main/oldOut/{}.csv'.format(state_name[i]), encoding='utf-8')
    data=data['raw_positives']
    name['data'+str(i)]=data
for j in range(0,len(data)-1):
    name['data_dict_'+str(j)]=[]
    for i in range(0,len(state_name)):
        name['data_dict_'+str(j)].append([state_name[i],name['data'+str(i)].iloc[j]])
for j in range(0,len(data)-1):
    (
        Map()
        .add('',name['data_dict_'+str(j)],maptype='美国')
        .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=max([x[1] for x in name['data_dict_'+str(j)]]), min_=min([x[1] for x in name['data_dict_'+str(j)]])),
            title_opts=opts.TitleOpts(title=j))
        .render('{}.html'.format(j))
    )