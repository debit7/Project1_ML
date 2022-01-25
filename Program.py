import Hits
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import operator
import Functions as func
import seaborn as sns
from array import array

#create scatterplot with regression line
#The file project1-hits.txt is opened using using open function from python, and all the lines are inside the file  as a seprate list.
#further , the data hour and hits seprated by comma again seprated in two different list . hour[] and list[].
# at the same time "nan" values are ignored while appending in the list.
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

##########################################docs

# The function are created to do a good programming practice . SUM_List can return the overall sum of Data inside the list.
#Sum_of_Pair function receives two list and can perform cross multiplication between two list of data, having same index. And return the overall sum.
#Similarly, the function Sum_of_square return the sum of square of data inside the list.
sum_of_x=func.SUM_List(hour)
sum_of_y=func.SUM_List(hits)

sum_of_pair=func.SUM_of_Pair(hour,hits)

sum_of_square_x=func.SUM_of_square(hour)
sum_of_square_y=func.SUM_of_square(hits)

N=len(hour)

slope=((N*sum_of_pair)-(sum_of_x*sum_of_y))/((N*sum_of_square_x)-(sum_of_x*sum_of_x))

intercept=(sum_of_y-(slope*sum_of_x))/N
print(slope,intercept)

Y=intercept+slope*700
print(Y)
###########################################
max_x = max(hour) + 400
min_x = min(hits) - 400
x = func.linspace (min_x, max_x, 100)

# linespace function  is used to create an evenly spaced sequence in a specified interval.
# to get values for y we need to convert the numpy array for the list, thats why numpy library is used in our code.
y=intercept+slope*np.array(x)
plt.plot(x, y, color='#58b970', label='Regression Line')
# plt.regplot(hour, hits, ci=None,label='Regression Line')
plt.scatter(hour, hits, c='#ef5423', label='data points')


plt.xlabel('Hours')
plt.ylabel('Hits')

plt.legend()
plt.show()
