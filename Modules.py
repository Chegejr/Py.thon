# Modules is way to recycle a code written by someone else
#  One can also refer module as a code library
# Below is an exmple of importing a module for reuse, "Created by Chege Jr, may not run"
import mymodule as me
name = me.greetings("Chege Jr")
print(name)

# lets say I want to print out the month of December 1900
# Below is how
import calendar
December_1900 = calendar.month(1900,12)
print(December_1900)

# Lets say i want to find the square root of a number
# Below is how
import math
result = math.sqrt(91725)
print(result)

# the dir() function is used to list all the function names that can be used within the module
import platform
x = platform.system()
print(x)

import platform
x = dir(platform)
print(x)

def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

from mymodule import person1
print (person1["age"])

