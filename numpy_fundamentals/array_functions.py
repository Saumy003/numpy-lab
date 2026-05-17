"""Topic 5. Array Functions"""

import numpy as np

array = np.random.random((3, 3))
array = np.round(array * 100)
print("Ye raha apna 3x3 ka array:",array)

# max/min/sum/prod

print(np.max(array))
print(np.min(array))
print(np.sum(array))
print(np.prod(array))

# row & column wise max/min/sum/prod

print(np.max(array, axis=1))      #for row axis is 1
print(np.min(array, axis=1))      #for column axis is 0

# mean/median/std/var

print(np.var(array, axis = 1))
print(np.std(array, axis = 1))

#triginometric functions

print(np.sin(array))

# dot product
array2 = np.arange(12).reshape((3, 4))
array3 = np.arange(12, 24).reshape((4, 3))

print(np.dot(array2, array3))

# log & exponents
print(np.log(array))
print(np.exp(array))

# round/floor/ceil
array4 = np.random.random((2,2))
array4 = np.round(array4*10)
print(array4)

array4 = np.random.random((2,2))
array4 = np.floor(array4*10)
print(array4)

array4 = np.random.random((2,2))
array4 = np.ceil(array4*10)
print(array4)