"""
In python lists are used to store multiple items in a single variable
Lists are mutable, they can be changed
Assuming that I was going to the market, below is how my shopping list will look like
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

