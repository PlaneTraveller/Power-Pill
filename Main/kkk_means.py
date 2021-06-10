import json
import numpy as np
import pandas
from matplotlib import pyplot


def euclDistance(vector1, vector2):
    return pow((sum(pow(vector2 - vector1, 2))), 0.5)


k = 3
# f1 = np.array([44, 16, 57, 61, 10, 42, 9, 68, 62, 35, 7, 48])
# f2 = np.array([44, 4, 13, 18, 10, 34, 15, 10, 6, 40, 5, 36])

with open('./Main/input/paramDict.json') as fl:
    dat = fl.read()
    rawDat = json.loads(dat)

listK = []
listB = []

for key in rawDat:
    listK.append(rawDat[key][0])
    listB.append(rawDat[key][1])
f1 = np.array(listK)
f2 = np.array(listB)
data = np.array(list(zip(f1, f2)))


def Make_Centroids(data, k):
    hang, lie = data.shape
    centroids = np.zeros((k, lie))
    for i in range(k):
        n = int(np.random.uniform(0, hang))
        centroids[i, :] = data[n, :]
    return centroids


def Euclidean_Distance(x, y):
    return (pow(sum(pow(y - x, 2)), 0.5))


def kmeans(data, k):
    hang = data.shape[0]
    output = np.mat(np.zeros((hang, 2)))
    change = True
    centroids = Make_Centroids(data, k)
    while change:
        change = False
        for i in range(hang):
            min_distance = 99999999
            cluster = k
            for j in range(k):
                distance = Euclidean_Distance(centroids[j, :], data[i, :])
                if distance < min_distance:
                    min_distance = distance
                    cluster = j
            if output[i, 0] != cluster:
                change = True
                output[i, :] = cluster, min_distance ** 2
        for i in range(k):
            point = data[np.nonzero(output[:, 0].A == i)[0]]
            centroids[i, :] = np.mean(point, axis=0)
    return (centroids, output)


def plot(data, k, centroids, output):
    hang = data.shape[0]
    mark = ['Dr', 'Db', 'Dg']
    for i in range(hang):
        n = int(output[i, 0])
        pyplot.plot(data[i, 0], data[i, 1], mark[n])
    for i in range(k):
        pyplot.plot(centroids[i, 0], centroids[i, 1], mark[i], ms=12)
    pyplot.show()


centroids, output = kmeans(data, k)
print(centroids, output)
plot(data, k, centroids, output)
