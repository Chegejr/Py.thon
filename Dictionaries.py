"""
Dictionaries in python refers to a collection of items which can be of different types.
These created items forming a dictionary are in form of "key-value" format contained in curly braces.
The "Key" and the "Value" are separated by use of a colon.
like lists in python, dictionaries are mutable; one can add or remove items from the dictionary.
Dictionaries do not allow duplicate elements.
Elements of a dictionary cannot be accessed using indexing method.

"""
Exam_results = {"Maths": 87, "Eng" : 78, "Geo" : 84, "Dynamics" : 94, "Electricity" : 83};
print("My exam results are as follows: ",Exam_results);

# Accessing the elements of a dictionary

print("My Maths score is, ", Exam_results["Maths"]);

# Also we i can use the "get()" method to access elements of the dictionary

print("My score in Maths is, ", Exam_results.get("Maths"));

# Adding an element in a dictionary

Exam_results["Science"] = 88;
print(Exam_results);

# Also, i can add an element in the dictionary using the ".update" method

Exam_results.update([("History", 94)]);
print(Exam_results);

# Updating the elements of a dictionary

Exam_results["History"]= 96;
print(Exam_results);

# Removing an element from a dictionary

del(Exam_results["Science"]);
print(Exam_results);

Exam_results.pop("History");
print(Exam_results);

# Printing out the keys of the dictionary

print(Exam_results.keys());

# printing the values of the dictionary

print(Exam_results.values());

# Printing out the items of the dictionary

print(Exam_results.items());

