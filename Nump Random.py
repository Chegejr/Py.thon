# Pseudo Random and True Random.
# Computers work on programs, and programs are definitive set of instructions. So it means there must be some algorithm to generate a random number as well.
# If there is a program to generate random number it can be predicted, thus it is not truly random.
# Random numbers generated through a generation algorithm are called pseudo random.
# Can we make truly random numbers?
# Yes. In order to generate a truly random number on our computers we need to get the random data from some outside source.
# This outside source is generally our keystrokes, mouse movements, data on network etc.
# We do not need truly random numbers, unless it is related to security (e.g. encryption keys) or 
# the basis of application is the randomness (e.g. Digital roulette wheels).
# In this tutorial we will be using pseudo random numbers.


# Generating a random integer
from numpy import random
x = random.randint(100)
print(x)

# The randint() method takes a size parameter where you can specify the shape of an array.
# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
from numpy import random
x = random.randint(100,size=(3,5))
print(x)


# Generating a random float
from numpy import random
x = random.rand()
print(x)

# The rand() method also allows you to specify the shape of the array.
from numpy import random
x = random.rand(5)
print(x)

# Generate a 2-D array with 3 rows, each row containing 5 random float numbers from 0 to 100:
from numpy import random
x = random.rand(3,5)
print(x.round(4)) #Rounding of the random generated number to 4 decimal places

# Generate Random Number From Array
# The choice() method allows you to generate a random value based on an array of values.
# The choice() method takes an array as a parameter and randomly returns one of the values.
import numpy as np
from numpy import random
y = np.array([1,2,3,4,5])
print("This is how array Y looks like",y)
x = random.choice(y,size=(3,3))
print("The random number generated from array Y is",x)



