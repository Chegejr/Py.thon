# JSON is an acronym for Javascript Object Notation
# It is a data exchange format just like xml
# compared to XML JSON is more lightweight 

# The problem
# Creat an address book and add some records in it
# Create a program that reads this book
# A tip! The address book will be inform a dictionary

addressBook = {}
addressBook["Malone"] = {
    "name": "Past Malone",
    "Address": "Baltimore34",
    "Pager": 73108243
}

addressBook["michael"] = {
    "name": "Michael Scofield",
    "Address": "Fox River",
    "Pager": 73164243
}

addressBook["ragnar"] = {
    "name": "Ragnar Lothbrok",
    "Address": "Kattegart",
    "Pager": 38108463
}

addressBook["leo"] = {
    "name": "Lionel Messi",
    "Address": "Nou Camp",
    "Pager": 10180243
}

# import the JSON module
import json

# What the below " json.dumps(addressBook) " does is. It takes in the " addressBook " as input which is in form of a dictionary and dumps it as 
# a string. Thats the use of "s" in the dumps function.
# As the json module dumps the input into a string in a variable name "addresses", it converts the input in a json format
addresses= json.dumps(addressBook) 
print(addresses)

# Next is to write the json formated code in file
with open("C://Users//user//Desktop// Py.thon//addressbook.txt", "w") as f:
    f.write(addresses)
    
# After the above we need now to create a python program that will open and read the contents of the json file
# We first need to open the file
file = open("C://Users//user//Desktop//Py.thon//addressbook.txt", "r")
addresses = file.read()
print(addresses)

# Lets say we need to print out the pager number for scofield.
# First we need to convert the dictionary that was convrted to string back to dictionary
import json
book = json.loads(addresses) #loads the string "addresses" and converts it to a dictionary
print("The contents of the address book are:", book)
print(type(addresses)) # The "addresses" is a string
print(type(book)) # The "book"  is a dictionary after conversion

print(book) # The only difference from " print(addresses) " is that "addresses" is string type while book is a "dictionary"

# Back to our question of printing michael`s pager
print(book["michael"]) # Prints out michael`s` entire information
print(book["michael"]["Pager"]) #prints out michael`s pager number

#  Our Final task is to print out the entire contents of the addressbook
for x in book:
  print("The following is "+x+"`s personal details",book[x]) # Prints out the personal details of each person in a new row

# We can parse the following into json string
import json
print(json.dumps({"name": "John", "age": 30})) # A dictionary
print(json.dumps(["apple", "bananas"])) # A list
print(json.dumps(("apple", "bananas"))) # A tuple
print(json.dumps("hello")) # A string
print(json.dumps(42)) # An integer
print(json.dumps(31.76)) # Float
print(json.dumps(True)) # Boolean 
print(json.dumps(False)) # Boolean
print(json.dumps(None)) # Nonetype
