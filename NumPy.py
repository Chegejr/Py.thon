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


# datatypes in numpy

import numpy as np
arr1 = np.array(["chege","array","moon","terminal"])
print(arr1.dtype)

# we can only change the dtype of an array by only copying the same array into another
# variable array and specifying the new data type as follows
arr3 = np.array([23,98,56,19,37])
print(arr3.dtype)

arr2 = arr3.astype('f') #also we can do this----->arr2 = arr3.astype(float)
print(arr2.dtype)

#  the numpy view vs copy
# The "copy" owns the data meaning that any changes made to the data in the copy 
# does not affect the original array and vice versa
#  the opposite is the case for "view"; any changes made to the "view" array affects the original array and viceversa

# "COPY"
import numpy as np
ar1 = np.array(["chege","terminal","jesus",12,23,556,78])

ar2 = ar1.copy()
ar1[3] = "moon"

print(ar1)
print(ar2)
# Note that the changes made on the original array does not affect the copy


# "VIEW"
import numpy as np
ar3 = np.array(["chege","terminal","jesus",12,23,556,78])

ar4 = ar3.view()
ar3[3] = "CRISTIANO"

print(ar3)
print(ar4)
# Note that the changes made on the original array affects even the "view"

# An array that owns the data returns the value "none" when the " base" is run 
# and returns the original array if it does not won the data
print(ar1.base) 
print(ar3.base)
print(ar4.base)
