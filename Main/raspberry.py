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
    check = True
    for row in CARaw:
        if check == True:
            check = False
            continue
        DatList.append(int(float(row[1])))
DatList.pop(0)

# basic code
green = LED(19)
red = LED(26)


def flash():
    red.on()
    green.on()
    sleep(0.2)
    red.off()
    green.off()
    sleep(0.5)


def sig(r, g):
    if r == '1':
        red.on()
    if g == '1':
        green.on()
    sleep(0.7)
    red.off()
    green.off()
    sleep(0.5)


def fastFlash():
    for i in range(3):
        red.on()
        green.on()
        sleep(0.1)
        red.off()
        green.off()
        sleep(0.2)


def compareRaw():
    for i in range(len(DatList)):
        if DatList[i + 1] > DatList[i]:
            red.on()
            sleep(1)
            red.off()
            sleep(1)
        else:
            sleep(2)


# bonus code
RevList = []
for i in range(len(DatList)):
    RevList.append(DatList[len(DatList) - i - 1])

BinList = []
for Rev in RevList:
    Bin = bin(Rev)
    Bin = Bin[2:]
    BinList.append(Bin)

big = '0'
for bin in BinList:
    if len(bin) > len(big):
        big = bin

digitedBin = []
for bin in BinList:
    tempBin = bin
    while (len(tempBin) < len(big)):
        tempBin = '0' + tempBin
    digitedBin.append(tempBin)

# Outputting digitedBin with the data at the most digit.


# Controling the Diodes: <red><green>
def weirdCode():
    for bin in digitedBin:
        tempBin = list(bin)
        while tempBin != []:
            sig(tempBin.pop(0), tempBin.pop(0))
            flash()
        fastFlash()
