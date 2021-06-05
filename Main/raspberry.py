import json
import csv
'''
from gpiozero import LED
from time import sleep
'''

with open('../Main/input/state_name.json') as fl:
    stateStr = fl.read()
stateDict = json.loads(stateStr)

#Data reader
with open('../Main/oldOut/California.csv') as fl:
    CARaw = csv.reader(fl)
    DatList = []
    check = True
    for row in CARaw:
        if check == True:
            check = False
            continue
        DatList.append(int(float(row[1])))
DatList.pop(0)

'''
# basic code
blue = LED(19)
red = LED(26)
for i in range(len(DatList)):
    if DatList[i + 1] > DatList[i]:
        red.on()
        sleep(1)
        red.off()
        sleep(1)
    else:
        sleep(2)
'''

# bonus code
RevList = []
for i in range(len(DatList)):
    RevList.append(DatList[len(DatList) - i - 1])

BinList= []
for Rev in RevList:
    Bin = bin(Rev)
    Bin = Bin[2:]
    BinList.append(Bin)

big = '0'
for bin in BinList:
    if len(bin) > len(big):
        big = bin
print(len(big))


