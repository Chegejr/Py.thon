"""
In python lists are used to store multiple items in a single variable
Lists are mutable, they can be changed
Assuming that I was going to the market, below is how my shopping list will look like
list can hold any type of values from text, Int, Float
"""

Shopping_list = ["soap", "bread", "sugar", "veggies", "salt", "shampoo", "Cooking oil"];
print("My shopping list is as follows",Shopping_list);

"""
In lists, there are several operations that can be done
They include, append, insert, length, checking if a certain item is in the list
Below is an example of each
"""
#Append adds an item at the end of the list

Shopping_list.append("milk");
print(Shopping_list);

#insert addss an item at a specific location
#If i want to insert toothpaste after bread, below is how

Shopping_list.insert(2,"toothpaste");
print(Shopping_list);

#If i want to check how many items are on my list, below is how

print(len(Shopping_list));

#Just like strings we can use indexing to print out specific item or/and items

print(Shopping_list[1]);
print(Shopping_list[0:]);
print(Shopping_list[-1]);

#checking if a certain item is on the list

print("bread" in Shopping_list);
print("milk" in Shopping_list);
print("ethanol" in Shopping_list);

# changing the item through indexing
myfamily = ["Paps","Moms","Jane","Mercy","Mary","Wayne","Maggy"]
myfamily[4]= "Moon"
print(myfamily[4]) #output------->Moon

# Note: The length of the list will change when the number of items inserted does not match the number of items replaced.
# If you insert less items than you want to replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) #Output------->['apple', 'watermelon']

# Appending another list to another list we use the ".extend" method
parents = ["Moms","Paps"]
kids = ["jane","Mercy","Moon","Mary","Maggy"]
parents.extend(kids)
goodFamily = parents
print(goodFamily) #Output------>['Moms', 'Paps', 'jane', 'Mercy', 'Moon', 'Mary', 'Maggy']

# You cannot only append a list to another list but yuh can append a tuple, set, dictionary to a list by use of the ".extend" method
Age = (27,34,43) # A Tuple
goodFamily.extend(Age)
print(goodFamily) #OUtput------->['Moms', 'Paps', 'jane', 'Mercy', 'Moon', 'Mary', 'Maggy', 27, 34, 43]

# Removing items in a list
# ".remove" removes  a specified item in the list and takes one argument therefore yuh can only remove one item at a time
fruits = ["Apple","Guava","Mango","orange"]
print(fruits) #Output------->['Apple', 'Guava', 'Mango', 'orange']
fruits.remove("Mango")
print(fruits) # Output------>['Apple', 'Guava', 'orange']

# Yuh can also delete an item from the list or even delete the entire list using "del" keyword
del fruits[0]
print(fruits) #Output------->['Guava', 'orange']
del fruits #Deletes the entire list

# We can also clear the entire list. This leaves an empty list
players = ["Messi","Pele","Maradona","Cristiano"]
print(players) # Output------->['Messi', 'Pele', 'Maradona', 'Cristiano']
players.clear()
print(players) # Output-------->[]
