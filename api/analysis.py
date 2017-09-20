import numpy as np
import csv
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans2, whiten

lines = [line.rstrip('\n') for line in open('../kmeansData')]

arr = list()

for line in lines:
  arr.append(map(float, line.split()))

coordinates= np.array(arr)
x, y = kmeans2(whiten(coordinates), 3, iter = 20)  
plt.scatter(coordinates[:,0], coordinates[:,1], c=y);
plt.show()
