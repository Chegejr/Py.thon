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
# Accessing items of a tuple
# Items of atuple can be accesed through indexing
countries =("Croatia","Belgium","Sweden","England","Slovenia")
print(countries[1]) # Prints out the second item in the tuple. Output--------> Belgium

# Accessing the items using the range of index
countries =("Croatia","Belgium","Sweden","England","Slovenia")
print(countries[2:5]) # Prints the item s from the index 2 to index 4. index 5 is not included. Output-------> ('Sweden', 'England', 'Slovenia')

# negative indexing in range
countries =("Croatia","Belgium","Sweden","England","Slovenia")
print(countries[-4:-1])  # Output------> ('Belgium', 'Sweden', 'England')

# if the starting index is not provided the listing starts from the first one at index 0
countries =("Croatia","Belgium","Sweden","England","Slovenia")
print(countries[:-1]) #  Starts from the frst item to the second last item. Output------> ('Croatia', 'Belgium', 'Sweden', 'England')

# if the ending index is not provided the listing is done from the specified starting index to the last
countries =("Croatia","Belgium","Sweden","England","Slovenia")
print(countries[1:]) # Output---------> ('Belgium', 'Sweden', 'England', 'Slovenia'). starts from index one"Belgium" to the last "Slovenia"

# checing if a certain item exists in a given tuple
countries =("Croatia","Belgium","Sweden","England","Slovenia")
if "slovenia" in countries:
    print("The country 'Slovenia' is in countries")
else:
    print("Not found in countries")
#  Output-------> The country 'Slovenia' is in countries. becuase our country slovenia with a small letter "S" is not in our countries tuple

# python unpacking Tuples
#  when we create a tuple and assign values to it, that is packing a tuple
#  Python alllows us to unpack the same packed values back to variables 
players = ("Messi","Pele","Zidane")
moon,star,universe = players
print(moon) # Output------> Messi
print(star) # Output------> Pele
print(universe) # Output------> Zidane

# if by chance yuh happen to have an instance where the number of variables is less than the number of values use an asterisk "*"
# the rest of the values will be unpacked into one variable as a list
players = ("Messi","Pele","Zidane","Cristiano","Jota","Neves","Fernandes","Felix")
Argentina,Brazil,France,*Portugal = players
print("Argentina have",Argentina) # Output------> Argentina have Messi
print("Brazil have",Brazil) # Output------> Brazil have Pele
print("France have",France) # Output------> France have Zidane
print("Portugal have",Portugal) # Output------> Portugal have ['Cristiano', 'Jota', 'Neves', 'Fernandes', 'Felix']

# its not a must that the asterisk be at the last variable
# it can also be on any other variable so long as it picks the right values accordingly
players = ("Messi","Cristiano","Jota","Neves","Fernandes","Felix","Pele","Zidane")
Argentina,*Portugal,Brazil,France = players
print("Argentina have",Argentina) # Output------> Argentina have Messi
print("Brazil have",Brazil) # Output------> Brazil have Pele
print("France have",France) # Output------> France have Zidane
print("Portugal have",Portugal) # Output------> Portugal have ['Cristiano', 'Jota', 'Neves', 'Fernandes', 'Felix']
