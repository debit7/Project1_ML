import Hits
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import operator
import matplotlib.pyplot as plt
import Functions as func
with open("project1-hits.txt") as f:
    array = f.read().splitlines()

    f.close()
dicts = {}
hits = []
hour = []
for items in array:
    hours = items.split(',')[0]
    views = items.split(',')[1]
    if views != "nan":
        hour.append(int(hours))
        hits.append(int(views))
print(hour)
print(hits)
# calculate mean of x & y using an inbuilt numpy method mean()
# mean_x = np.mean(hour)
# mean_y = np.mean(hits)
mean_x=func.calculateMean(hour)
mean_y=func.calculateMean(hits)
m = len(hour)

print(func.calculateMean(hour))
print(mean_x)

# using the formula to calculate m & c
numer = 0
denom = 0
for i in range(m):
  numer += (hour[i] - mean_x) * (hour[i] - mean_y)
  denom += (hour[i] - mean_x) ** 2
m = numer / denom
c = mean_y - (m * mean_x)

print (f'm = {m} \nc = {c}')

# plotting values and regression line
max_x = np.max(hour) + 100
min_x = np.min(hits) - 100

# calculating line values x and y
x = np.linspace (min_x, max_x, 100)
y = c + m * x

plt.plot(x, y, color='#58b970', label='Regression Line')
plt.scatter(hour, hits, c='#ef5423', label='data points')

plt.xlabel('Head Size in cm')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()