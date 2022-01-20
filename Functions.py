def calculateMean(arr):
 size=len(arr)
 sumOfElements = 0
 for i in range(size):
    sumOfElements += arr[i]
 return sumOfElements/size