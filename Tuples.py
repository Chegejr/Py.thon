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

# Appending an item into  an already existing tuple
c = list(tuple2);
c.append("Added");
tuple2 = tuple(c);
print(tuple2);

# Secoond example of appending an element to a tuple by first changing it into a list and back to tuple
tuple4 = ("Arsenal", "Me", 56, "Anorld", "Guava")
print(tuple4);
print(type(tuple4));


jr = list(tuple4);
print(jr);
print(type(jr));
jr.append("junior");
print(jr)

tuple4 = tuple(jr);
print(type(tuple4));
print(tuple4);

# Manipulating tuples using "For Loops"
for x in (tuple2):
    print(x);
    
for y in tuple4:
    print(y);

