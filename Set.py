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


names = {"me","you","us"}
luckynumber = {12,23,11}
names.update(luckynumber) #  we can the add the items of another set by use of the ".update" method
print(names) # Output-----> {23, 11, 'you', 12, 'me', 'us'}

networth = [12,23,33]
names.update(networth) #  we can join a set by any other iterable
print(names) # Output-----> {33, 'me', 23, 'us', 11, 'you', 12}

#  Joining sets
counties = {"Nakuru", "Nairobi"}
leaders = {"Kihika","Sakaja"}
countyGov = counties.union(leaders) # Joining two sets
print(countyGov) # Output-----> {'Nairobi', 'Nakuru', 'Kihika', 'Sakaja'}

#  Use of intersecion_update method
#  returns items that are present in both sets
set1 = {"apple",23,True,"Moon","cherry","chege"}
set2 = {"messi","23",23,True,"apple"}
set1.intersection_update(set2)
print(set1) # Output------> {True, 'apple', 23}

#  Use of symmetric_difference
set1 = {"apple",23,True,"Moon","cherry","chege"}
set2 = {"messi","23",23,True,"apple"}
set1.symmetric_difference(set2)
print(set1) # Output-------> {'chege', True, 'apple', 'cherry', 23, 'Moon'}

"""
Method	                Description
add()	                Adds an element to the set
clear()	                Removes all the elements from the set
copy()	                Returns a copy of the set
difference()	        Returns a set containing the difference between two or more sets
difference_update() 	Removes the items in this set that are also included in another, specified set
discard()	            Remove the specified item
intersection()	        Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	        Returns whether two sets have a intersection or not
issubset()	            Returns whether another set contains this set or not
issuperset()	        Returns whether this set contains another set or not
pop()	                Removes an element from the set
remove()	            Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	                Return a set containing the union of sets
update()	            Update the set with the union of this set and others

"""
