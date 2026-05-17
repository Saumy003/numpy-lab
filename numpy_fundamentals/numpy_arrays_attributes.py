"""Topic 2. NumPy Arrays Attributes"""

import numpy as np

arr1 = np.arange(10)
arr2 = np.arange(12, dtype=float).reshape(3, 4)
arr3 = np.arange(8).reshape(2, 2, 2)

# 1. ndim
print(arr3.ndim)       #3

# 2. shape
print(arr2.shape)      #(3,4)
print(arr1.shape)      #(10,)

# 3. size
print(arr3.size)       #8
print(arr2.size)       #12

# 4. iteamsize
print(arr3.itemsize)   #8 bytes

# 5. dtypes
print(arr1.dtype)      #int64
print(arr2.dtype)      #float64
