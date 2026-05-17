"""Topic 4. Array Operations"""

import numpy as np

# Scaler Operations
arr1 = np.arange(10)
arr2 = np.arange(12, dtype=float).reshape(3, 4)
arr3 = np.arange(8).reshape(2, 2, 2)

# 1. arithmetic operations

print(arr1 * 2)              #[ 0  2  4  6  8 10 12 14 16 18]
print(arr1 ** 3)             #[  0   1   8  27  64 125 216 343 512 729]
print(arr2 + 1)

# 2. relational operations

print(arr3 > 3)              #[[[False False] , [False, False] , [True, True], [True, True]]]

# 3. vectors operations

arr4 = np.array([1, 2, 3, 4])
arr5 = np.array([5, 6, 7, 8])

print(arr4 + arr5)
