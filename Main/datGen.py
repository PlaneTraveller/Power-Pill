import numpy as np
import pandas as pd
import json
import sklearn.linear_model as linear_model

# Initialization
path = "./Main/oldOut/{}.csv"
model = linear_model.LinearRegression()

with open('./Main/input/state_name.json') as fl:
    stateStr = fl.read()
stateDict = json.loads(stateStr)

paramDict = {}

for stShort in stateDict:
    with open(path.format(stateDict[stShort])) as fl:
        rawDat = pd.read_csv(fl)

    rawDict = dict(rawDat.iloc[260:320, 1])
    x = list(rawDict.keys())
    x = np.array(x)
    x = x.reshape(-1, 1)
    y = list(rawDict.values())
    y = np.array(y)
    y = y.reshape(-1, 1)

    model.fit(x, y)
    paramDict[stateDict[stShort]] = [model.coef_[0][0], model.intercept_[0]]

# Outputting
out = json.dumps(paramDict)
with open('./Main/input/paramDict.json', "w") as fl:
    fl.write(out)
