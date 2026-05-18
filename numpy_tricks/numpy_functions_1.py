""" Numpy Functions Part 1"""

import numpy as np


#np.sort
a = np.random.randint(1, 100, 15)
print(np.sort(a))

b = np.random.randint(1, 100, 16).reshape(4, 4)
print(np.sort(b, axis=0))                          #axis -> 1 (row wise) & axis -> 0 (column wise)


#np.append
print(np.append(a, 200))

print(np.append(b, np.random.random((b.shape[0], 1)), axis=1))


#np.concqtenate
c = np.arange(6).reshape(2, 3)
d = np.arange(6, 12).reshape(2, 3)

print(np.concatenate((c, d), axis=1))


#np.unique
e = np.array([1, 2, 3, 4, 4, 5,4, 2, 1, 8, 9])
print(np.unique(e))


#np.expand_dims
f = np.array([1, 2, 3, 4, 5, 6, 7])
print(np.expand_dims(f, axis = 0))


#np.where
g = np.random.randint(1, 100, 10).reshape(1, 10)

"""ques1. find all incidies with value grater than 50"""
print(np.where(g > 50))

"""ques2. replace all value > 50 with 0"""
print(np.where(g > 50, 0, g))                     #[[ 0  0 48  0  0 31 13  0  1 13]]


#np.argmax
h = np.random.randint(1, 100, 10).reshape(1, 10)
print(np.argmax(h))                              #8 index

b = np.random.randint(1, 100, 16).reshape(4, 4)
print(np.argmax(b, axis= 1))


#np.argmin
i = np.random.randint(1, 100, 10).reshape(1, 10)
print(np.argmin(i))


#np.cumsum
b = np.random.randint(1, 100, 16).reshape(4, 4)
print(np.cumsum(b, axis= 1))


a = np.random.randint(1, 100, 15)
print(np.cumprod(a))