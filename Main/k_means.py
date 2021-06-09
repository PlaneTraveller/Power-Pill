# -*- coding: utf-8 -*-
from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = (16, 9)
# the biggest size of my chart
plt.style.use('ggplot')
# a different style

# Draw the initial chart
data = pd.read_csv()
f1 = data['V1'].values
f2 = data['V2'].values
X = np.array(list(zip(f1, f2)))
plt.scatter(f1, f2, c='black', s=6)

# Calculate the distance
def dist(a, b, ax=1):
    return np.linalg.norm(a - b, axis=ax)


# Pick out three lucky points
k = 3
C_x = np.random.randint(0, np.max(X)-20, size=k) #(min,max,size)
C_y = np.random.randint(0, np.max(X)-20, size=k)
C = np.array(list(zip(C_x, C_y)), dtype=np.float32)
# Plot the random 3 points on initial chart
plt.scatter(f1, f2, c='black', s=7)
plt.scatter(C_x, C_y, marker='*', s=200, c='red')


# Used to save the center points before updating
C_old = np.zeros(C.shape)
clusters = np.zeros(len(X))
iteration_flag = dist(C, C_old, 1)


tmp = 1
# If the center points don't change any more or tmp = 20
while iteration_flag.any() != 0 and tmp < 20:
    for i in range(len(X)):
        distances = dist(X[i], C, 1)
        cluster = np.argmin(distances) 
        clusters[i] = cluster
        
    C_old = deepcopy(C)
    for i in range(k):
        points = [X[j] for j in range(len(X)) if clusters[j] == i]
        C[i] = np.mean(points, axis=0)
        
    tmp = tmp + 1
    iteration_flag = dist(C, C_old, 1)
    
    
# Final results
colors = ['r', 'g', 'b', 'y', 'c', 'm']
fig, ax = plt.subplots()
# Give different colors to different group
for i in range(k):
        points = np.array([X[j] for j in range(len(X)) if clusters[j] == i])
        ax.scatter(points[:, 0], points[:, 1], s=7, c=colors[i])
ax.scatter(C[:, 0], C[:, 1], marker='*', s=200, c='black')