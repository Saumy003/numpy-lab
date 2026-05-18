""" Topic 4. Working with mathematical formulas """

import numpy as np

#sigmoid
a = np.arange(10)

def sigmoid(array):
    return 1/(1 + np.exp(-(array)))

print(sigmoid(a))



#mean squared error
actual = np.random.randint(1, 50, 25)
predicted = np.random.randint(1, 50, 25)

def mse(actual, predicted):
    return np.mean((actual - predicted)**2)

print(mse(actual, predicted))