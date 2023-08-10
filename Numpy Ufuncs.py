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

# Cummulative sum
# cummulative sum means adding partial elements of the array .Below is how
import numpy as np
arr1 = np.arange(1,4) #output-------->[1 2 3]
newarr = np.cumsum(arr1)
print(newarr) #output-------->[1 3 6]

# Numpy products
import numpy as np
arr1 = np.arange(1,4) #output-------->[1 2 3]
arr2 = np.arange(4,7) #output-------->[4 5 6]
newarr = np.prod(arr1)
print(newarr) #output-------->[6]
newarr = np.prod(arr2)
print(newarr) #output-------->[120]
newarr = np.prod([arr1,arr2])
print(newarr) #output-------->[720]

# product over the axis
import numpy as np
arr1 = np.arange(1,4) #output-------->[1 2 3]
arr2 = np.arange(4,7) #output-------->[4 5 6]
newarr = np.prod([arr1,arr2],axis=1) # product is done row wise when the axis is 1
print(newarr) #output-------->[6 120] we have two answer values because the product is done row wise and we have two rows

import numpy as np
arr1 = np.arange(1,4) #output-------->[1 2 3]
arr2 = np.arange(4,7) #output-------->[4 5 6]
newarr = np.prod([arr1,arr2],axis=0) # product is done column wise when the axis is 0
print(newarr) #output-------->[ 4 10 18] we have three answer values because the product is done column wise and we have three columns

# cummmulative product
import numpy as np
arr1 = np.arange(1,4) #output-------->[1 2 3]
arr2 = np.arange(4,7) #output-------->[4 5 6]
newarr = np.cumprod(arr1)
print(newarr) #output--------> [1 2 6]
newarr = np.cumprod(arr2)
print(newarr) #output--------> [  4  20 120]
newarr = np.cumprod([arr1,arr2])
print(newarr) #output--------> [  1   2   6  24 120 720]

# Numpy discrete difference
# discrete difference means subr=tracting successive elements
import numpy as np
arr1 = np.array([5,10,15,20,25,30])
newarr = np.diff(arr1)
print(newarr) # Output--------->[5 5 5 5 5]

# We can also specify the number of times we want the subtraction to take place
import numpy as np
arr1 = np.array([5,10,15,20,25,30])
newarr = np.diff(arr1,n=2)
print(newarr) # 1st iteration of subtraction Output--------->[5 5 5 5 5]. 2nd iteration of subtraction Output--------->[0 0 0 0]

# Numpy GCD Greatest common divisor
import numpy as np
arr1 = np.arange(1,6)
print(arr1) # Output-------> [1 2 3 4 5]
newarr = np.gcd.reduce(arr1)
print(newarr) # Output-------> 1

# Numpy Trigonometric Functions
# Numpy provides the ufuncs i.e cos(), tan() and sin()
# They take in values in radians form and produces the corresponding cos(), sin() or tan() depending on the request
import numpy as np
arr1 = np.array([np.pi/2,np.pi/3,np.pi/4,np.pi/5])
print(arr1) # Output---------> [1.57079633 1.04719755 0.78539816 0.62831853]
y = np.sin(arr1)
print(y)  # Output---------> [1.         0.8660254  0.70710678 0.58778525]

# Converting radians to degrees
import numpy as np
arr1 = np.array([np.pi/2,np.pi/3,np.pi/4,np.pi/5])
y = np.rad2deg(arr1)
print(y) # Output---------> [90. 60. 45. 36.]

# Converting degrees to radians
import numpy as np
arr1 = np.array([124,78,98,345])
y = np.deg2rad(arr1)
print(y) # Output---------> [2.16420827 1.36135682 1.71042267 6.02138592] reconverting the output should give you the above degrees

# Finding the hypotenuse
import numpy as np
base = 10
height = 45
hypotenuse = np.hypot(base,height)
print(hypotenuse.round(4)) # Output---------> 46.0977

# numpy hyperbolic functions
# numpy provides the ufunc  i.e cosh(), sinh() and tanh() that take in radian values and produce the corresponding hyperbolic values
import numpy as np
arr1 = np.array([1.234,4.6474,8.5353,1.273])
x = np.cosh(arr1)
print(x) # Output---------> [1.86303380e+00 5.21615022e+01 2.54567943e+03 1.92577077e+00]

# finding angles
import numpy as np
arr = np.array([0.1, 0.2, 0.5])
x = np.arctanh(arr)
print(x)  # Output---------> [0.10033535 0.20273255 0.54930614]

