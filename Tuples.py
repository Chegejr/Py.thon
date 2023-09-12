"""
Tuples are special kind of lists
The main difference between lists and tuples is that lists are mutable while tuples are not
Also, tuples items are contained in circle brackets while lists are enclosed in square brackets
Indexing in both tuples and lists is similar
Tuples are ordered and the order does not change
Tuples also allow duplicate elements as in lists
"""
Tuple1 = ("Future", 21, "Mia", "Ugali", "Banana", "Ugali", 78);
tuple2 = ("Chege", "Menengai", 89, ("Einstein", 78, "Ugali"));

print(Tuple1); # Output-------->('Future', 21, 'Mia', 'Ugali', 'Banana', 'Ugali', 78)
print(tuple2); # Output-------->('Chege', 'Menengai', 89, ('Einstein', 78, 'Ugali'))
print(Tuple1 + tuple2); # Output-------->('Future', 21, 'Mia', 'Ugali', 'Banana', 'Ugali', 78, 'Chege', 'Menengai', 89, ('Einstein', 78, 'Ugali'))

print(Tuple1[0]);  # Output--------> Future
print(tuple2[-1][2]); # slicing a tuple inside another tuple.  # Output--------> Ugali
print((Tuple1).count("Ugali")); # Counts how many times a specified item appears in the list.  # Output--------> 2

print(type(Tuple1)); # Checking if indeed what we have is a tuple.  # Output--------> <class 'tuple'>
tuple3  = print(("Ugali, ")* 4);  # Output--------> Ugali, Ugali, Ugali, Ugali,


#  example of appending an element to a tuple by first changing the tuple into a list and back to tuple
# we first convert the tuple into a list beacuse  a tuple does not allow any modification once created compared to list
tuple4 = ("Arsenal", "Me", 56, "Anorld", "Guava")
print(tuple4); # Output-------> ('Arsenal', 'Me', 56, 'Anorld', 'Guava')
print(type(tuple4)); # Output-------> <class 'tuple'>

jr = list(tuple4); # converting the tuple into  a list
print(jr); # Output-------> ['Arsenal', 'Me', 56, 'Anorld', 'Guava']
print(type(jr)); # Output-------> <class 'list'>. Our tuple is now a list
jr.append("junior"); # appending the new item to our newly converted list
print(jr) # Output-------> ['Arsenal', 'Me', 56, 'Anorld', 'Guava', 'junior']

tuple4 = tuple(jr); # reconverting our list back to tuple
print(type(tuple4)); # Output-------> <class 'tuple'>
print(tuple4); # Output-------> ('Arsenal', 'Me', 56, 'Anorld', 'Guava', 'junior')


tuple2 = ("Chege", "Menengai", 89, ("Einstein", 78, "Ugali"));
tuple4 = ("Arsenal", "Me", 56, "Anorld", "Guava")
# Manipulating tuples using "For Loops"
for x in (tuple2):
    print(x); # Output-------> 
    """
Chege
Menengai
89
('Einstein', 78, 'Ugali')
    """
    
for y in tuple4:
    print(y); # Output------->
    """
Arsenal
Me
56
Anorld
Guava
    """
    

