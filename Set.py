# Sets are python collection arrays for storing data
# Sets are unchangeable*,unordered,unindexed.
fruits = {"apple","guava","kiwi"}
print(type(fruits)) # Checking the data type. Output-------> <class 'set'>
print(fruits) # Output---------> {'apple', 'guava', 'kiwi'}

# loooping through set items
for x in fruits:
    print("I love",x)

# Output--------v
"""
I love kiwi
I love apple
I love guava
"""

# sets do not allow duplicates
names = {"chege","chege","josiah","waweru"}
print(names) # Output-----> {'waweru', 'josiah', 'chege'}

# Note that 1 and the value True are treated as one, therefore yuh can eitherhave 1 or True
thisset = {"me",True,1,"junior"}
print(thisset) # Output-----> {True, 'me', 'junior'}

#  At the same time we can add or remove items from a set
names.add("moon")
print(names) # Output-----> {'moon', 'waweru', 'josiah', 'chege'}
names.remove("waweru")
print(names) # Output-----> {'josiah', 'moon', 'chege'}

