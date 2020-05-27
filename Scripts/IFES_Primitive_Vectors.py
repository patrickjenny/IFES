# -*- coding: utf-8 -*-
"""
Created on Mon May  4 22:48:01 2020

@author: paddy
"""


from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from itertools import product, combinations


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

r = [0, 1]
for s, e in combinations(np.array(list(product(r, r, r))), 2):
    if np.sum(np.abs(s-e)) == r[1]-r[0]:
        ax.plot3D(*zip(s, e), color="black", alpha=0.3)


base = np.zeros((3,3))
base[0] = [1,1,0]
base[1] = [0,1,1]
base[2] = [1,0,1]

base = (1/2)*base
points = np.zeros((100,3))
points[1] = base[0]
points[2] = base[1]
points[3] = base[2]

n = 0

for i in range(0,2):
    for j in range(0,2):
        for k in range(0,2):
            points[n] = base[0]*i+base[1]*j+base[2]*k
            n = n+1
            
points[n] = [1,1,1]
n=n+1
points[n] = [1,1,0]
n=n+1
points[n] = [1,0,1]
n=n+1
points[n] = [1,0,0]
n=n+1
points[n] = [0,1,1]
n=n+1
points[n] = [0,1,0]
n=n+1
points[n] = [0,0,1]
n=n+1


for i in range(n):
    ax.scatter(points[i][0], points[i][1], points[i][2], marker='o',color='black',alpha=0.7)



# Plot the 3 base vectors
ax.quiver(0,0,0,base[0][0],base[0][1],base[0][2], label='u', color='black')
ax.quiver(0,0,0,base[1][0],base[1][1],base[1][2], label='v', color='black')
ax.quiver(0,0,0,base[2][0],base[2][1],base[2][2], label='w', color='black')



# Be sure to only pick integer tick locations.
for axis in [ax.xaxis, ax.yaxis, ax.zaxis]:
    axis.set_major_locator(ticker.MaxNLocator(integer=True))


ax.set_xlabel('X [a]')
ax.set_ylabel('Y [a]')
ax.set_zlabel('Z [a]')

ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.set_zlim(0,1)

plt.show()