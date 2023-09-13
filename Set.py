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

