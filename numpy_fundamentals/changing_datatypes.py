"""Topic 3. Changing Datatypes"""

import numpy as np


# astype => in NumPy is used to change the data type of elements in a NumPy array.


# Integer --> float
arr = np.array([1, 2, 3, 4])

print(arr)                      #[1, 2, 3, 4]
print(arr.dtype)                #int64

new_arr = arr.astype(float)

print(new_arr)                  #[1. 2. 3. 4.]
print(new_arr.dtype)            #float64

# Float --> Int
arr = np.array([1.9, 2.5, 3.8])

new_arr = arr.astype(int)         

print(new_arr)                  #[1 2 3]
