import pyecharts
import json
import pandas

#===
#=== Retrieving Input data
#===
with open('./Main/input/state_name.json') as fl:
    stateStr = fl.read()
stateDict = json.loads(stateStr)

dateDF = pd.read_csv('./Main/input/Date.csv')
date = dateDF.iloc[:, 1]

#===
#=== Demo
#===
