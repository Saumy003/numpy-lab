"""Topic 7. Iterating NumPy Arrays"""

import numpy as np

arr1 = np.arange(10)
arr2 = np.arange(12, dtype=float).reshape(3, 4)
arr3 = np.arange(27).reshape(3, 3, 3)


# loop in 1D array  --> print each element
for i in arr1:
    print(i)

# loop in 2D array  --> print each row
for i in arr2:
    print(i)

# loop in 3D array  --> print each 2D array
for i in arr3:
    print(i)

# to print each individual elements from 2D/ 3D array
for i in np.nditer(arr2):
    print(i)

for i in np.nditer(arr3):
    print(i)