""" Topic 8. Stacking & Splitting """

import numpy as np

a1 = np.random.random((4, 4))*10
a1 = np.round(a1)

a2 = np.random.random((4, 4))*10
a2 = np.round(a2)


# STACKING #

#horizontal stack
print(np.hstack((a1 , a2)))

#vertical stack
print(np.vstack((a1 , a2)))


# SPLITTING #

#horizontal stack
print(np.hsplit(a1, 2))

#vertcal stack
print(np.vsplit(a2, 2))