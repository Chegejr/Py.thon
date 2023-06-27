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
