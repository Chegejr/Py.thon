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

# Shape of an array refers to the number of elements in each dimension
import numpy as np
ar5 = np.array([1,2,3,4], ndmin=5)
print(ar5)
print("The shape of the",ar5,"is",ar5.shape)

# Array reshaping
# Reshape the below array into a 2D array
ar6 = np.array([1,2,3,4,5,6])
print(ar6)
newarr = ar6.reshape(2,3)
print(newarr)

# Flattening an array "Reshaping into 1D array"
ar7  = np.array([[1,2,3,4,5,11],[6,7,8,9,10,12]])
print(ar7)
newarr2 = ar7.reshape(-1)
print(newarr2)

#  iterating arrays -------> using basic python for loop
# 1D array iteration
import numpy as np
ar8 = np.arange(10)
print(ar8)
for i in ar8:
    print(i)
    
# ietrating over 2D array
import numpy as np
ar9 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(ar9)
for i in ar9:
    print(i)


# to print out the exact scalars of a 2D array 
import numpy as np
ar9 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
for x in ar9:
    for y in x:
        print(y)

# The simplest way of printing out the scalar values of the array using------> ".nditer()" function
import numpy as np
ar9 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
for x in np.nditer(ar9):
    print(x)

#  To print out the exact values of a 3D array
import numpy as np
ar10 = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
print(ar10.ndim) # Checking what dimension is the array
for x in ar10:
    for y in x:
        for z in y:
            print(z)
            
# The simplest way of printing out the scalar values of the array using------> ".nditer()" function
import numpy as np
ar10 = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
for x in np.nditer(ar10):
    print(x)

# Iterating the array with different datatypes using-------> "op_dtypes"
# NumPy does not change the data type of the element in-place (where the element is in array) 
# so it needs some other space to perform this action, that extra space is called buffer, 
# and in order to enable it in nditer() we pass flags=['buffered']
import numpy as np
ar11 = np.array([1,2,3,4,5,6])
for x in np.nditer(ar11,flags=['buffered'],op_dtypes=['S']):
    print(x)

# iterating by use of steps
# iterate the below array skipping one element
import numpy as np
ar12 = np.array([1,2,3,4,5,6])
for x in np.nditer(ar12[::2]):
    print(x)

# Enumerate on following 1D arrays elements:
import numpy as np
arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
  print(idx, x)

# Enumerate on following 2D array's elements:
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
  print(idx, x)

# # joining arrays
# # 1. Using the concatenate function
import numpy as np
ar12 = np.array([1,2,3,4])
ar13 = np.array([5,6,7,8])
newarr12 = np.concatenate((ar12,ar13),axis=0)
print(newarr12)

# # Stcaking along the rows
import numpy as np
ar12 = np.array([1,2,3,4])
ar13 = np.array([5,6,7,8])
newarr12 = np.hstack((ar12,ar13))
print(newarr12)

# Stcaking along the columns
import numpy as np
ar12 = np.array([1,2,3,4])
ar13 = np.array([5,6,7,8])
newarr12 = np.vstack((ar12,ar13))
print(newarr12)

# Stcaking along the height or depth
import numpy as np
ar12 = np.array([1,2,3,4])
ar13 = np.array([5,6,7,8])
newarr12 = np.dstack((ar12,ar13))
print(newarr12)

# Array splitting is the oppositye of array joining
# Using------> array_split()
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)

# Split the array in 4 parts:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr)
# Note: We also have the method split() available but it will not adjust the elements when elements are 
# less in source array for splitting like in example above, array_split() worked properly but split() would fail.

# Access the splitted arrays:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr[0])
print(newarr[1])
print(newarr[2])

# Split the 2-D array into three 2-D arrays.
import numpy as np
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)

# Split the 2-D array into three 2-D arrays.
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3)
print(newarr)

# Split the 2-D array into three 2-D arrays along rows.
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)

# Use the hsplit() method to split the 2-D array into three 2-D arrays along rows.
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)
print(newarr)
# Note: Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().

# Searching Arrays
# You can search an array for a certain value, and return the indexes that get a match.
# To search an array, use the where() method.
import numpy as np
arr21= np.array([1,2,3,4,5,6,6,8,1,2])
x= np.where(arr21== 1)
print(x)

# Find the indexes where the values are even:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)

# Find the indexes where the values are odd:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 1)
print(x)

# Search sorted
# Find the indexes where the value 7 should be inserted:
import numpy as np
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)

# Find the indexes where the value 7 should be inserted, starting from the right:
import numpy as np
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)

# Find the indexes where the values 2, 4, and 6 should be inserted:
import numpy as np
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)

# Sorting arrays
# Sort the array:
import numpy as np
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))
# Note: This method returns a copy of the array, leaving the original array unchanged.

# Sort the array alphabetically:
import numpy as np
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))

# Sort a boolean array:
import numpy as np
arr = np.array([True, False, True])
print(np.sort(arr))

# Sort a 2-D array:
import numpy as np
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))

# Filtering arrays
# Getting some elements out of an existing array and creating a new array out of them is called filtering.
# In NumPy, you filter an array using a boolean index list.
# A boolean index list is a list of booleans corresponding to indexes in the array.
# If the value at an index is True that element is contained in the filtered array,
# if the value at that index is False that element is excluded from the filtered array.

# Create an array from the elements on index 0 and 2:
import numpy as np
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)

# Create a filter array that will return only values higher than 42:
import numpy as np
arr = np.array([41, 42, 43, 44])
# Create an empty list
filter_arr = []
# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

# Create a filter array that will return only even elements from the original array:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
# Create an empty list
filter_arr = []
# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

