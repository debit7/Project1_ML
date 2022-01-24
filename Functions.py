def calculateMean(arr):
 size=len(arr)
 sumOfElements = 0
 for i in range(size):
    sumOfElements += arr[i]
 return sumOfElements/size

def linspace(a, b, n=100):
    diff = (b - a)/(n - 1)
    return [ round(diff,8) * i + a  for i in range(n)]

def SUM_List(list):
   return sum(list)

def SUM_of_Pair(list1,list2):
   res_list = []
   for i in range(0, len(list1)):
    res_list.append(list1[i] * list2[i])
   print(res_list)
   return sum(res_list)

def SUM_of_square(list):
   res_list = []
   for i in range(0, len(list)):
    res_list.append(list[i] * list[i])
   return sum(res_list)