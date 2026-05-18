""" 1. COMPARISION OF NUMPY ARRAY vs PYTHON LIST"""
import numpy as np
import time
import sys

# i.speed

#list
a = [i for i in range(10000000)]
b = [ i for i in range(10000000, 20000000)]

c = []
start = time.time()
for i in range(len(a)):
    c.append(a[i] + b[i])

print(time.time() - start)                  #1.1906752586364746 sec


#numpy
a = np.arange(10000000)
b = np.arange(10000000, 20000000)

start = time.time()
c = a + b

print(time.time() - start)                    #0.019815444946289062 sec





# ii. memory

#list
a = [i for i in range(10000000)]
print(sys.getsizeof(a))                         #89095160 bytes

#numpy
b = np.arange(10000000, dtype=np.int32)
print(sys.getsizeof(b))                           #40000112 bytes




# iii. convenience