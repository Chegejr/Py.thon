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
# When you convert python to json, python objects are converted  to json(javascript) equivalent.
# Example 1
import json

print(json.dumps({"name": "John", "age": 30})) # A python "dictionary" to a json "object"
print(json.dumps(["apple", "bananas"])) # A python "list" to a json "array"
print(json.dumps(("apple", "bananas"))) # A python "tuple" to a json "array"
print(json.dumps("hello")) # A python "string" to a json "string"
print(json.dumps(42)) # A python "integer" to a json "number"
print(json.dumps(31.76)) # A python "Float" to a json "number"
print(json.dumps(True)) # A python Boolean "True" to a json boolean "true"
print(json.dumps(False)) # A python Boolean "False" to a json boolean "false"
print(json.dumps(None)) # A python "Nonetype" to a json "null" 

#  Example 2
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
# Note also that when you print "Example 1" which is a json string it is difficult to read its contents since theres no identation
# or line breaks, you can improve readability by specifying an indentation when parsing the json string.
y = json.dumps(x, indent=4) # specifying an indentation when parsing the json string


# the result is a JSON string:
print(y)
