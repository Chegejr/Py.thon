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

# Random Data Distribution
# Data Distribution is a list of all possible values, and how often each value occurs.
# Such lists are important when working with statistics and data science.
# The random module offer methods that returns randomly generated data distributions.
# A random distribution is a set of random numbers that follow a certain probability density function.
# Probability Density Function: A function that describes a continuous probability. i.e. probability of all values in an array.


# Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.
# The probability for the value to be 3 is set to be 0.1
# The probability for the value to be 5 is set to be 0.3
# The probability for the value to be 7 is set to be 0.6
# The probability for the value to be 9 is set to be 0
    
from numpy import random
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)

# Same example as above, but return a 2-D array with 3 rows, each containing 5 values.
from numpy import random
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x)

# Random Permutations of Elements
# A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
# The NumPy Random module provides two methods for this: shuffle() and permutation().

# Shuffling
import numpy as np
from numpy import random
x= np.array([1,2,33,45,66,12])
random.shuffle(x)#The shuffle() method makes changes to the original array.
print(x)

# Permutation
import numpy as np
from numpy import random
x= np.array([1,2,33,45,66,12])
print(random.permutation(x))#The permutation() method returns a re-arranged array (and leaves the original array un-changed).

# Normal (Gaussian) Distribution
#The Normal Distribution is one of the most important distributions.
# It is also called the Gaussian Distribution after the German mathematician Carl Friedrich Gauss.
# It fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc.
# Use the random.normal() method to get a Normal Data Distribution.
# It has three parameters:
# loc - (Mean) where the peak of the bell exists.
# scale - (Standard Deviation) how flat the graph distribution should be.
# size - The shape of the returned array.

# Generate a random normal distribution of size 2x3:
from numpy import random
x = random.normal(size=(2,3))
print(x)

# Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2:
from numpy import random
y = random.normal(size=(2,3),loc=1,scale=2)
print(y)

# Binomial Distribution
# Binomial Distribution is a Discrete Distribution.
# It describes the outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails.
# It has three parameters:
# n - number of trials.
# p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).
# size - The shape of the returned array.
# Discrete Distribution:The distribution is defined at separate set of events,
# e.g. a coin toss's result is discrete as it can be only head or tails whereas height
# Discrete Distribution:The distribution is defined at separate set of events,
# e.g. a coin toss's result is discrete as it can be only head or tails whereas height of
# people is continuous as it can be 170, 170.1, 170.11 and so on.
from numpy import random
x = random.binomial(n=5,p=0.5,size=12)
print(x)
# The main difference is that normal distribution is continous whereas binomial is discrete

# poisson distribution
# Poisson Distribution is a Discrete Distribution.
# It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what is the probability he will eat thrice?
# It has two parameters
# lam - rate or known number of occurrences e.g. 2 for above problem.
# size - The shape of the returned arr
from numpy import random
x = random.poisson(5,100) # 5=lam and 100=size
print(x)

# uniform distribution
# used where the chances of a certain event occuring is equal to the rest
# it takes three parameters i.e
# a = lower bound
# b = upper bound
# size = shape of the returned array
from numpy import random
y = random.uniform(size=(3,3))
print(y)

# logistic distribution
# ised to describe growth
# takes three parameters i.e
# loc = mean
# scale = standard deviation
# size = shape of the returned array
from numpy import random
y = random.logistic(loc=12,scale=7,size=(3,3))
print(y)

# Multinomila is a generalization of the binomial distribution
# unlike binomial where the outcomes must be either of the two lets say heads or tails for toss of a coin,
# multinomial takes events that has multiple outcomes lets rolling a dice where the number of of possible outcomes is 6

# Example of rolling a dice
# takes three parameters i.e
# n = the number of possible outcomes
# pvals = the probability that a single event occurs
# size = shape of the returned array
from numpy import random
y = random.multinomial(n=6,pvals=(1/6,1/6,1/6,1/6,1/6,1/6),size=(3,3))
print(y)
# Note: Multinomial samples will NOT produce a single value! They will produce one value for each pval.
# Note: As they are generalization of binomial distribution their visual representation and similarity of normal distribution is same as that of multiple binomial distributions.

# exponential distribution
# Used to describe the time till the next occurence of an event
# takes two parameters i.e
# size = shape of the returned array
# scale = inverse of rate
# Draw out a sample for exponential distribution with 2.0 scale with 2x3 size:

from numpy import random
y = random.exponential(scale=2,size=(2,3))
print(y)

# chi square distribution
# Used to verify the hypothesis
# takes in two parameters i.e
# df = degree of freedom
# size = shape of the returned array
from numpy import random
y = random.chisquare(df=3,size=(2,3))
print(y)
