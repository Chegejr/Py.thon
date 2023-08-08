# Ufuncs stands for universal functions, they opperate on ndarray
# They are used in vectorization where its much faster than iterating over each element in the array
# Ufuncs takes in additional parameters i.e
# where =  boolean array or condition defining where the operations should take place.
# dtype = defining the return type of elements.
# out = output array where the return value should be copied.

# lets say i want to add two lists
# using the traditional python zip() function
x = [1,2,3,4]
y = [5,6,7,8]
z = []
for i,j in zip(x,y):
    z.append(i+j)
print(z)

# lets say i want to add two lists
# using the unfunc add()
import numpy as np
x = [1,2,3,4]
y = [5,6,7,8]
z = np.add(x,y)
print(z)
#  Now we can see that instead of iterating over each element in the array when adding we can simply use the ufunc add()
#  to easily add the two lists together

# creating your own ufuncs
# create a normal function then add it to the numpy ufuncs library using the frompyfunc() method
# the frompyfunc() takes 3 arguments i.e
# function = name of the function
# input = number of inputs
# outpit = number of outputs
def greetings(fname = "moon",sname= "jr"):
    print("My name is",fname,sname)
greetings()

import numpy as np
greetings = np.frompyfunc(greetings,2,1)
print(greetings("moon","jr"))

# 2nd example on creating your on ufunc
def add(x,y):
    sum = x+y
    print("The total sum is:",sum)
add(12,12)

import numpy as np
add = np.frompyfunc(add,2,1)
print(add(12,15))
    
