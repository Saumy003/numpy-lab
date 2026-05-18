"""  Topic 6.Plotting Graphs """

import numpy as np
import matplotlib.pyplot as plt

# plotting a 2d plot


# x = y
x = np.linspace(-10, 10, 100)
y = x                             #shape of array must be same

plt.plot(x, y)
plt.show()



# y = x^2
a = np.linspace(-50, 50, 100)
b = a**2

plt.plot(a, b)
plt.show()



# y =xlogx
p = np.linspace(-30, 30, 100)
q = p * (np.log(p))

plt.plot(p, q)
plt.show()