"""Topic 6. Indexing and Slicing"""


# INDEXING #

import numpy as np

arr1 = np.arange(10)
arr2 = np.arange(12, dtype=float).reshape(3, 4)
arr3 = np.arange(27).reshape(3, 3, 3)

# indxing in 1D array
print(arr1[0])                   #0
print(arr1[-1])                  #9

# indexing in 2D array
print(arr2[1, 2])                #6.0
print(arr2[2, 1])                #9.0

#indexing in 3D array
print(arr3)
print(arr3[1, 1, 0])             #6
print(arr3[0, 0, 0])             #0
print(arr3[1, 0, 1])             #5



# SLICING #

# slicing in 1D array
print(arr1[2:5])                #[2 3 4]

# slicing in 2D array
print(arr2)
print(arr2[1:,])
print(arr2[:,2])                #[ 2.  6. 10.]
print(arr2[1:,1:3])
print(arr2[::2, 1::2])
print(arr2[::2, ::3])

# slicing in 3D array
print(arr3)
print(arr3[1])
print(arr3[::2])

print(arr3[2,1:,1:])
print(arr3[::2, 0, ::2 ])