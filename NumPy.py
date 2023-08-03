# NumPy stands for Numerical Python
# Serves the same role as the traditional python list but are much faster 
# The are stored in continous memory locations therefore the accessability is much efficient;
# this is what makes numpy arrays faster than traditional python lists(upto 50x)

import numpy

arr = numpy.array([1,2,3,4,5,6,7])
print(arr)
print(arr[0])

# Checking what dimension is the array

print("Number of dimensions is :",arr.ndim)

# specifiying the number of dimensions in an array

ar = numpy.array([1,2,3,4,5],ndmin= 3)
print(ar)
print("Number of dimensions is :",ar.ndim)
print(ar[0,0,4])# indexing elelments in an array"3D"

# Array slicing
import numpy as np
arr = np.array([12,27,39,67,88])
print(arr[:3]) #prints out the first three contents of the array
# we can also specify the step by adding a third parameter
print(arr[0:5:2])

# slicing 2d arrays
import numpy as np
arr = np.array([[1,2,3,4,5,66,92,73],[45,43,221,56,3,22,12,67]])
print(arr[1,3:6])
# from both arrays return index 2
print(arr[0:2,2])