# string refers to a sequence of characters
# They are stored in different specific memory addresses therefore we can be able to access a specific character by use of index
# A string is found within quotation marks
# Keep in mind that strings are immutable, once created they cannot be changed
 
Text = "Ice cream"
print("Through indexing, the character at memory location one is ", Text[1]);
print("Through indexing we can still print out a specific sequence of the string or portion", Text[0:4]);
print("Through indexing we can still print out a specific sequence of the string or portion", Text[4:9]);
print("Through indexing we can still print out a specific sequence of the string or portion", Text[0:]);

Name = "Chege"
Sur_name = "Waweru"

print("Welcome "+ Name + " to Data Science road map: CodeBasics");

# python string formating
# we can use placeholders to hold where the value should be placed
# the .format()
intro = "My name is {}. Learning Data Science".format("chege") #Using an empty placeholder 
print(intro) #Output------>My name is chege. Learning Data Science

# also we can use index inside of the placeholders
Player = "The best player in the world is {1} after {0}".format("Cristiano","Messi") #using index to fill in the placeholders
print(Player)#Output------>The best player in the world is Messi after Cristiano

# Also we can use named indexes
favfruits = "I love {ffruit},{sfruit} but most of the times i prefer {tfruit}"
print(favfruits.format(ffruit="Apple",sfruit="Mango",tfruit="Pineapple"))#Output------>I love Apple,Mango but most of the times i prefer Pineapple

