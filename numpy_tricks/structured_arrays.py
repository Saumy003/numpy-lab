""" Topic 6. Structured Arrays """

import numpy as np

#still we are not able to make hetrogenous array using numpy arrys.
arr = np.array([1, "hello", True, 1.5])

print(arr)                               #['1' 'hello' 'True' '1.5']
print(type(arr))                         #<class 'numpy.ndarray'>
print(type(arr[0]))                      #<class 'numpy.str_'>
print(type(arr[2]))                      #<class 'numpy.str_'>



#to make hetrogenous array we use --> structured array
#name, iq, cgpa, placed


dt = np.dtype(
    [
        ("name", '<U20'),
        ("iq", np.int64),
        ("cqpa", np.float64),
        ("placed", '<U20')
    ]
)

print(dt)


stu = np.array(
    [
        ("Altman", 100, 7.77, "yes"),
        ("Dario", 120, 8.88, "yes"),
        ("Musk", 80, 9.3, "yes"),
        
    ], dtype=dt
)

print("Hetrogenous Array:", stu)
print(stu[1])                           #('Dario', 120, 8.88, 'yes')
print(stu["placed"])                    #['yes' 'yes' 'yes']