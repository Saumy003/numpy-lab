""" Topic 5. Working with missing values """

import numpy as np

#working with missing values -> np.nan

arr = np.array([1, 2, 3, 4, np.nan, 6])

print(np.isnan(arr))
print(arr[np.isnan(arr)])
print(arr[~np.isnan(arr)])