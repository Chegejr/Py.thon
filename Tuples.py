"""
Tuples are special kind of lists
They main difference between lists and tuples is that lists are mutable while tuples are not
Also tuples items are contained in circle brackets while lists are enclosed in square brackets
Indexing in both tuples and lists is similar
Tuples are ordered and te order does not change
Tuples also allow duplicate elements
"""
Tuple1 = ("Future", 21, "Mia", "Ugali", "Banana", "Ugali", 78);
tuple2 = ("Chege", "Menengai", 89, ("Einstein", 78, "Ugali"));

print(Tuple1);
print(tuple2)
print(Tuple1 + tuple2); # Tuple concatenation

print(Tuple1[0]); # Tuple slicing
print(tuple2[-1][2]); # Tuple slicing a tuple inside another tuple
print((Tuple1).count("Ugali")); # Counts how many times a specified item appears in the list

print(type(Tuple1)); # Checking if indeed what we have is a tuple