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
