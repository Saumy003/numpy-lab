""" Topic 1. Creating NumPy Arrays"""

import numpy as np

a = np.array([1, 2, 3])
print(a)
print(type(a))          #<class 'numpy.ndarray'>

# 2D array
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

# 3D array
c = np.array([[[9, 8, 7], [4 ,6, 1], [3, 8, 5]]])
print(c)

#dtype
d = np.array([1, 0, 3], dtype=float)
print(d)

# np.arange()

e = np.arange(1, 11)
print(e)

# with reshape
print(np.arange(1, 7).reshape(3 , 2))

#np.ones & np.zeros

initilise_martix_with_one = np.ones((3, 3))
print(initilise_martix_with_one)

initilise_martix_with_zeros = np.zeros((2, 3))
print(initilise_martix_with_zeros)

# np.randoms

initilise_martix_with_random_numbers = np.random.random((3, 4))
print(initilise_martix_with_random_numbers)

# np.linspace
linear_space = np.linspace(-5, 5, 4)
print(linear_space)

#np.identity
identity_matrix = np.identity(3)
print(identity_matrix)
