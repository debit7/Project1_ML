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
max_x = max(hour) + 400
min_x = min(hits) - 400


# calculating line values x and y
x = np.linspace (min_x, max_x, 100)
# x1=func.linspace(min_x, max_x, 100)
# print(isinstance(x))
# print(isinstance(x1))

y = c + m * x
y1=c+m*108
print(y1)
plt.plot(x, y, color='#58b970', label='Regression Line')
plt.scatter(hour, hits, c='#ef5423', label='data points')

plt.xlabel('Hours')
plt.ylabel('Hits')
plt.legend()
plt.show()