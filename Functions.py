def calculateMean(arr):
 size=len(arr)
 sumOfElements = 0
 for i in range(size):
    sumOfElements += arr[i]
 return sumOfElements/size

def linspace(a, b, n=100):
    diff = (b - a)/(n - 1)
    return [ round(diff,8) * i + a  for i in range(n)]