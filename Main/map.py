import json
import pandas
import imageio
from pyecharts import options
from pyecharts.charts import Map
from snapshot_phantomjs import snapshot
from pyecharts.render import make_snapshot

with open('C:/Users/86183/Documents/Tencent Files/907881557/FileRecv/state_name.json') as state:
    state=json.load(state)
state_name=list(state.values())
name=globals()
data_dict={}
population=pandas.read_csv('C:/Git/Power-Pill/Main/oldOut/population.csv',encoding='utf-8')
population.columns=['state_name','population']
for i in range(0,len(state_name)):
    data=pandas.read_csv('C:/Git/Power-Pill/Main/oldOut/{}.csv'.format(state_name[i]),encoding='utf-8')
    data=data['raw_positives']
    name['data'+str(i)]=data
for j in range(0,len(data)-1):
    name['data_dict_'+str(j)]=[]
    for i in range(0,len(state_name)):
        p=population[population.state_name==state_name[i]]
        p=p['population']
        if state_name[i]=='Puerto Rico':
            pass
        else:
            name['data_dict_'+str(j)].append([state_name[i],100*int(name['data'+str(i)].iloc[j])/int(p.iloc[0])])
# data processing

for j in range(0,len(data)-1):
    html=(
        Map()
        .add('',name['data_dict_'+str(j)],maptype='美国')
        .set_global_opts(
            visualmap_opts=options.VisualMapOpts(max_=max([x[1] for x in name['data_dict_'+str(j)]]),min_=min([x[1] for x in name['data_dict_'+str(j)]])),
            title_opts=options.TitleOpts(title=j)
            )
    )
# turn the data into .html

    make_snapshot(snapshot,html.render(),'{}.png'.format(j))
# turn the .html into .png

png=[]
for j in range(0,len(data)-1):
    png.append(imageio.imread('C:/Users/86183/{}.png'.format(j)))
imageio.mimsave('gif.gif',png,'GIF',duration=10/(len(data)))
# turn the .png into .gif
