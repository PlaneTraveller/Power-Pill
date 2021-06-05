import json
import csv
from gpiozero import LED
from time import sleep

with open('../Main/input/state_name.json') as fl:
    stateStr = fl.read()
stateDict = json.loads(stateStr)

#Data reader
with open('../Main/oldOut/California.csv') as fl:
    CARaw = csv.reader(fl)
    DatList = []
    for row in CARaw:
        DatList.append(row[1])
DatList.pop(0)

blue = LED(19)
red = LED(26)

# basic code
for i in range(len(DatList)):
    if DatList[i + 1] > DatList[i]:
        red.on()
        sleep(1)
        red.off()
        sleep(1)
    else:
        sleep(2)

# bonus code
