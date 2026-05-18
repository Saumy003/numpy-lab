""" Numpy Functions Part 2 """

import numpy as np


#np.percentile
a = np.random.randint(1, 100, 15)
print(np.percentile(a, 80))


#np.histogram
a = np.random.randint(1, 100, 15)
print(np.histogram(a, bins=[0, 20, 40, 60, 80, 100]))


#np.corrcoef
salary = np.array([20000, 40000, 25000, 35000, 40000])
experience = np.array([1, 4, 2, 3, 5])

print(np.corrcoef(salary, experience))


#np.isin
arr = np.array([43, 35, 49, 50, 78, 95, 76, 30, 12, 68])
items = [10 ,20, 30 ,40 ,50 ,60, 70, 80, 90, 100]

print(np.isin(arr, items))
print(arr[np.isin(arr, items)])                             #[50 30]


#np.flip
arr = np.array([43, 35, 49, 50, 78, 95, 76, 30, 12, 68])
print(np.flip(arr))      #[68 12 30 76 95 78 50 49 35 43]


#np.put
arr = np.array([43, 35, 49, 50, 78, 95, 76, 30, 12, 68])
np.put(arr, [2, 4], [75, 66])
print(arr)


#np.delete
arr = np.array([43, 35, 49, 50, 78, 95, 12, 68])
print(np.delete(arr, 3))            #3 index h.