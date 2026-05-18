""" 3. BROADCASTING """

import numpy as np

#ques1. 
a = np.arange(12).reshape(4, 3)
b = np.arange(3)

print(a)
print(b)

print(a + b)


#ques2.
c = np.arange(12).reshape(3, 4)
d = np.arange(3)

try:
    print(c + d)
except:
    print("Value error, can't use broadcasting")


#ques3.
p = np.arange(3).reshape(1, 3)
q = np.arange(3).reshape(3, 1)

try:
    print(p + q)
except:
    print("Value error, can't use broadcasting")


#ques4.
x = np.arange(12).reshape(3, 4)
y = np.arange(12).reshape(4, 3)

try:
    print(x + y)
except:
    print("Value error, can't use broadcasting")
    

#ques5.
arr1 = np.arange(16).reshape(4, 4)
arr2 = np.arange(4).reshape(2, 2)

try:
    print(arr1 + arr2)
except:
    print("Value error, can't use broadcasting")
