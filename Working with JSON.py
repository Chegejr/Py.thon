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
