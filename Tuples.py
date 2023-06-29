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

print(Tuple1); #prints contents of tuple1
print(tuple2); # Prints out the contents of tuple2  
print(Tuple1 + tuple2); # Tuple concatenation

print(Tuple1[0]); # Tuple slicing
print(tuple2[-1][2]); # Tuple slicing a tuple inside another tuple
print((Tuple1).count("Ugali")); # Counts how many times a specified item appears in the list

print(type(Tuple1)); # Checking if indeed what we have is a tuple
tuple3  = print(("Ugali, ")* 4);

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

