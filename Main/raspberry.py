import json
import csv

with open('./Main/input/state_name.json') as fl:
    stateStr = fl.read()
stateDict = json.loads(stateStr)

# Data reader
with open('./Main/oldOut/California.csv') as fl:
    CARaw = csv.reader(fl)
    DatList = []
    for row in CARaw:
        DatList.append(row[1])
        DatList.pop(0)
