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
    
# checking if a function is a ufunc
import numpy as np
print(type(np.add))

# simple arithmetic
# addition
import numpy as np
arr1 = np.array([15,32,38,84,59])
arr2 = np.array([10,20,30,40,50])
arr3 = np.add(arr1,arr2)
print(arr3)

# subtraction
import numpy as np
arr1 = np.array([15,32,38,84,59])
arr2 = np.array([10,20,30,40,50])
arr3 = np.subtract(arr1,arr2)
print(arr3)

# multiplication
import numpy as np
arr1 = np.array([15,32,38,84,59])
arr2 = np.array([10,20,30,40,50])
arr3 = np.multiply(arr1,arr2)
print(arr3)

# divison
import numpy as np
arr1 = np.array([15,32,38,84,59])
arr2 = np.array([10,20,30,40,50])
arr3 = np.divide(arr1,arr2)
print(arr3.round(3))#rounds the quotient to 3 decimal places

# remainder
import numpy as np
arr1 = np.array([15,32,38,84,59])
arr2 = np.array([10,20,30,40,50])
arr3 = np.remainder(arr1,arr2) #if you replace the remainder() with mod() the result is still the same 
print(arr3)

# power
import numpy as np
arr1 = np.array([15,12,3,8,9])
arr2 = np.array([2,3,6,4,5])
arr3 = np.power(arr1,arr2)
print(arr3)

# quotient and remainder
import numpy as np
arr1 = np.array([15,32,38,84,59])
arr2 = np.array([10,20,30,40,50])
arr3 = np.divmod(arr1,arr2) #prints out two arrays, one for quotient and the other for remainder
print(arr3)

# absolute
import numpy as np
arr1 = np.array([-15,32,-38,84,-59])
arr3 = np.absolute(arr1) #If you replace the absolute with abs() the result is still the same but its advised to use absolute()
print(arr3)

# rounding decimals
# there are basically five ways to round of decimal numbers in numpy i.e
# floor = rounds off to the nearest lower integer
# ceil = rounds off to the nearest upper interger
# around = does the normal"obvious" rounding
# fix = removes decimals 
# truncation = removes decimals

# Examples

# truncate
import numpy as np
arr1 = np.array([23.22323,12.15151,6.988,123]) #output-------->[ 23.  12.   6. 123.]
print(np.trunc(arr1))

# fix
import numpy as np
arr1 = np.array([23.22323,12.15151,6.988,123]) #output-------->[ 23.  12.   6. 123.]
print(np.fix(arr1))

# floor
import numpy as np
arr1 = np.array([23.22323,12.15151,6.988,123]) #output-------->[ 23.  12.   6. 123.]
print(np.floor(arr1))

# ceil
import numpy as np
arr1 = np.array([23.22323,12.15151,6.988,123]) #output-------->[ 24.  13.   7. 123.]
print(np.ceil(arr1))

# around
import numpy as np
arr1 = np.array([23.22323,12.15151,6.988,123]) #output-------->[ 23.223  12.152   6.988 123.   ]
print(np.around(arr1,3))

# log
import numpy as np
arr = np.arange(1,10)
for i in arr:
    print(i)
newarr = np.log2(arr)    
print(newarr)
newarr1 = np.log10(arr)
print(newarr1)

# Summations
# The main difference between summation and addition is that addition is done between two arguments 
# while summation is done between n elements

# Example to illustrate the difference

import numpy as np
arr1 = np.arange(1,6)
arr2 = np.arange(6,11)
newarr = np.add(arr1,arr2) #output-------->[ 7  9 11 13 15]
print(newarr)

import numpy as np
arr1 = np.arange(1,6)
arr2 = np.arange(6,11)
newarr = np.sum([arr1,arr2]) #output--------> 55
print(newarr)

# Summation on the axis
import numpy as np
arr1 = np.arange(1,6)
arr2 = np.arange(6,11)
print("This is arr1",arr1) #output-------->[1 2 3 4 5]
print("This is arr2",arr2) #output-------->[ 6  7  8  9 10]
newarr = np.sum([arr1,arr2],axis=1) #output--------> [15 40] sums up the values row wise
print(newarr)

import numpy as np
arr1 = np.arange(1,6)
arr2 = np.arange(6,11)
print("This is arr1",arr1) #output-------->[1 2 3 4 5]
print("This is arr2",arr2) #output-------->[ 6  7  8  9 10]
newarr = np.sum([arr1,arr2],axis=0) #output--------> [ 7  9 11 13 15] sums up the values column wise
print(newarr)
