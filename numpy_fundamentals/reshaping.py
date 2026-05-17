"""Topic 8. Reshaping NumPy Arrays"""

import numpy as np


a1 = np.arange(9).reshape((3, 3))

# reshape    --> give correct possible order of the matrix for your wish
print(a1)

#transpose --> do transpose of a matrix

print(np.transpose(a1))
print(a1.T)


#ravel --> convert multi dimensons array to one dimension

print(np.ravel(a1))