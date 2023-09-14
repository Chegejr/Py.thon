"""
Dictionaries in python refers to a collection of items which can be of different types.
These created items forming a dictionary are in form of "key-value" format contained in curly braces.
The "Key" and the "Value" are separated by use of a colon.
like lists in python, dictionaries are mutable; one can add or remove items from the dictionary.
Dictionaries do not allow duplicate elements.
Elements of a dictionary cannot be accessed using indexing method.

"""
Exam_results = {"Maths": 87, "Eng" : 78, "Geo" : 84, "Dynamics" : 94, "Electricity" : 83};
print("My exam results are as follows: ",Exam_results); # Output------> My exam results are as follows:  {'Maths': 87, 'Eng': 78, 'Geo': 84, 'Dynamics': 94, 'Electricity': 83}

# Accessing the elements of a dictionary
print("My Maths score is, ", Exam_results["Maths"]); # output------> My Maths score is,  87

# Also we i can use the "get()" method to access elements of the dictionary
print("My score in Maths is, ", Exam_results.get("Maths")); # output------> My score in Maths is,  87

Exam_results = {"Maths": 87, "Eng" : 78, "Geo" : 84, "Dynamics" : 94, "Electricity" : 83};
# Adding an element in a dictionary
Exam_results["Science"] = 88;
print(Exam_results); # Output------> {'Maths': 87, 'Eng': 78, 'Geo': 84, 'Dynamics': 94, 'Electricity': 83, 'Science': 88}

# Also, i can add an element in the dictionary using the ".update" method
Exam_results.update([("History", 94)]);
print(Exam_results); # Output------> {'Maths': 87, 'Eng': 78, 'Geo': 84, 'Dynamics': 94, 'Electricity': 83, 'Science': 88, 'History': 94}

# Updating the elements of a dictionary
Exam_results["History"]= 96;
print(Exam_results); # Output------> {'Maths': 87, 'Eng': 78, 'Geo': 84, 'Dynamics': 94, 'Electricity': 83, 'Science': 88, 'History': 96}

# Removing an element from a dictionary
del(Exam_results["Science"]);
print(Exam_results); # Output------> {'Maths': 87, 'Eng': 78, 'Geo': 84, 'Dynamics': 94, 'Electricity': 83, 'History': 96}
Exam_results.pop("History");
print(Exam_results); # Output------> {'Maths': 87, 'Eng': 78, 'Geo': 84, 'Dynamics': 94, 'Electricity': 83}
# Printing out the keys of the dictionary
Exam_results = {"Maths": 87, "Eng" : 78, "Geo" : 84, "Dynamics" : 94, "Electricity" : 83};
print(Exam_results.keys()); # Output-----> dict_keys(['Maths', 'Eng', 'Geo', 'Dynamics', 'Electricity'])

# printing the values of the dictionary
print(Exam_results.values()); # Output------> dict_values([87, 78, 84, 94, 83])

# Printing out the items of the dictionary
print(Exam_results.items()); # Output-----> dict_items([('Maths', 87), ('Eng', 78), ('Geo', 84), ('Dynamics', 94), ('Electricity', 83)])

# Manipulating dictionary using for loops
for x in Exam_results:
    print(x); # Output----->
    """
Maths
Eng
Geo
Dynamics
Electricity
    """
    
# Generating both keys and their corresponding values using for loops
for x,y in Exam_results.items():
    print(x,y); # Output----->
"""
Maths 87
Eng 78
Geo 84
Dynamics 94
Electricity 83
"""
# When using the dictionary we can update the dictionary by use of the ".update()" method
colorIntensity = {
    "Red":45,
    "Green":33,
    "Blue":27
}
colorIntensity.update({"Yellow":45})
print(colorIntensity) # OUtput------> {'Red': 45, 'Green': 33, 'Blue': 27, 'Yellow': 45}

# We also have the pop() method which removes a specified item
colorIntensity.pop("Red")
print(colorIntensity) # OUtput------> {'Green': 33, 'Blue': 27, 'Yellow': 45}

# Also we have the .popitem() which removes the lastly inserted item which in our case is "Yellow"
colorIntensity.popitem()
print(colorIntensity) # OUtput------> {'Green': 33, 'Blue': 27}

#  the del can del the entire dictionary or a specified key and its value 
del colorIntensity["Blue"]
print(colorIntensity) # OUtput------> {'Green': 33}
# or even the entire dictionary
del colorIntensity
# print(colorIntensity) # Error! Output------> NameError: name 'colorIntensity' is not defined

cars = {
    "Benzo":211,
    "Mustang":964,
    "Chev":233
}
# Also we can empty the entire dictionary by use of the clear method
cars.clear()
print(cars) # Output-----> {}

# Making copies of a dictionary
# One way is the use of the .copy() method
cars = {
    "Benzo":211,
    "Mustang":964,
    "Chev":233
}

newcars = cars.copy()
print(newcars) # Output-------> {'Benzo': 211, 'Mustang': 964, 'Chev': 233}

# Another way is the use of dict keyword
brandnew = dict(cars)
print(brandnew) # Output-------> {'Benzo': 211, 'Mustang': 964, 'Chev': 233}

cars.update({"Mazda":233})
print(cars) # Output------> {'Benzo': 211, 'Mustang': 964, 'Chev': 233, 'Mazda': 233}
print(newcars) # Output------>  {'Benzo': 211, 'Mustang': 964, 'Chev': 233} .Note that the copies do not get updated when there are changes in the original dictionary
print(brandnew) # Output------>  {'Benzo': 211, 'Mustang': 964, 'Chev': 233}

# tranquilo amigos----------> Calm down frinds
#  We can have nested dictionaries as well
cars = {
    "Mercedes":{
    "Model":"A-Class",
    "Make":"Mercedes Benz",
    "Year":2022
    },
    "Ford":{
    "Model":"Mustang",
    "Make":"Ford",
    "Year":2024
    },
    "Lamborghini":{
    "Model":"Aventador",
    "Make":"Lamborghini",
    "Year":2022
    },
    "Bentley":{
    "Model":"Bentayga",
    "Make":"Bentley",
    "Year":2023
    }
}

print(cars["Ford"]) # Output------> {'Model': 'Mustang', 'Make': 'Ford', 'Year': 2024}







