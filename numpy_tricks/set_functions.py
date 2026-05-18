""" Set Functions """

import numpy as np

#creating numpy arrays

m = np.array([1, 2, 3, 4, 5])
n = np.array([3, 4, 5, 6, 7])


#np.union1d
print(np.union1d(m, n))


#np.intersect1d
print(np.intersect1d(m, n))


#np.setdiff1d
print(np.setdiff1d(m, n))


#np.setxor1d
print(np.setxor1d(m, n))



#np.clip
array = np.random.randint(1, 100, 10)

print(np.clip(array, a_min=25, a_max=75))
