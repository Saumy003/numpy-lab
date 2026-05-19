""" Topic 4. Random Functions """

import numpy as np

# working with random function


#randint
arr1 = np.random.randint(2, 20, 6).reshape(2, 3)
print(arr1)


#seed
np.random.seed(0)
arr2 = np.random.randint(2, 20, 6)

print(arr2)


#shuffle
arr3 = np.array([12, 23, 67, 87, 55, 333])
print(arr3)

np.random.shuffle(arr3)
print(arr3)


#choice
arr4 = np.random.randint(1, 100, 14)
print(arr4)

print(np.random.choice(arr4, 5))