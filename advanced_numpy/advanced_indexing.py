""" 2. ADVANCED INDEXING """

import numpy as np

arr1 = np.arange(24).reshape((6, 4))


#fancy indexing --> use to print none pattern indexing
print(arr1[[0, 2, 3]])        #print 0th, 2nd, 3rd rowth of arr

print(arr1[[0, 2, 3, 5]])     #print 0th, 2nd, 3rd, & 5th rowth of arr




#boolean indexing
arr2 = np.random.randint(1, 100, 24).reshape(6, 4)
print(arr2)

#ques 1. find all numbers greater than 50
print(arr2 > 50)
print(arr2[arr2 > 50])

#ques 2. find all number greater than 50
print(arr2 % 2 == 0)
print(arr2[arr2 % 2 == 0])

#ques3. find all number greater than 50 and are even
print((arr2 > 50) & (arr2 % 2 == 0))                   # bit wise AND operator -> &
print(arr2[(arr2 > 50) & (arr2 % 2 == 0)])

#ques4. find allnumber not divisible by 7
print(arr2 % 7 != 0)
print(~(arr2 % 7 == 0))                                # bit wise NOT operator -> ~
print(arr2[~(arr2 % 7 == 0)])                          #[69 23 82 95 76  2 40  4 46]