from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Selecting data
with open('C:\Git\Power-Pill\Main\oldOut\California.csv') as fl:
    rawDat = pd.read_csv(fl)

date = rawDat.iloc[260:320, 0]
rawPos = rawDat.iloc[260:320, 1]
posDF = rawDat.iloc[260:320, :]

# Data Spliting
date_Trn, date_Tst, rawP_Trn, rawP_Tst = train_test_split(date,
                                                          rawPos,
                                                          test_size=0.3,
                                                          random_state=16)

# Setting Parameters
posDict = dict(rawP_Trn)
tempKeys = list(posDict.keys())
keys = []
for k in tempKeys:
    keys.append(float(k))
k = 0
b = 0
alpha = 0.00001
param = {'k': 0, 'b': 0}


# Cost Function
def computeCost(param, data):
    RRS = 0
    for key in data:
        RRS += (data[key] - param['k'] * key - param['b'])
    return RRS


# Gradiant Descent Function (Once)
def gradDesc(param, data, alpha):
    derivK = 0
    derivB = 0
    ret = param

    # Calculating Sum of Derivitive
    for key in data:
        derivK += 2 * (param['k'] * key + param['b'] - data[key]) * key
        derivB += 2 * (param['k'] * key + param['b'] - data[key])

    # Descending
    ret['k'] = param['k'] - alpha * derivK
    ret['b'] = param['b'] - alpha * derivB
    return ret


# linear Regression
def linReg(paramInit, data):
    tempParam = paramInit
    alpha = 0.00000001
    costChange = [0]
    delta = 100
    while delta > 0.1 or delta < -0.1:
        tempParam = gradDesc(tempParam, data, alpha)
        costChange.append(computeCost(tempParam, data))
        delta = costChange[-1] - costChange[-2]
    return tempParam, costChange


finalParam, cost = linReg(param, posDict)
plt.scatter(list(posDict.keys()), list(posDict.values()))
l = []
for k in keys:
    l.append(finalParam['k'] * k + finalParam['b'])

plt.plot(keys, l, c='r')
plt.show()
