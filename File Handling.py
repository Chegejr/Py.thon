"""
There are four different methods (modes) for opening a file:
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
"""
# Below is how to create a file 

file = open("C:\\Users\\user\\Desktop\\Py.thon\\file.txt", "w") # I have created my file called "file". 
# The "w" implies that  I want to write on it
file.write("Hey there, welcome home") #  Writing on the ne created file
file.close() # Once the file is created, it needs to be closed. 
# By doin` so the operating system frees up the memory that was allocated for the file 
# Lets say i change the contents to "I love python"
# This will overwrite the existing "Hey there, welcome home" to "I love python"
# If I dont want to keep the existing text even after I change, below is how

file2 = open("C:\\Users\\user\\Desktop\\Py.thon\\file2.txt", "a") # The "a" is for append. 
# This allows to make modifications to the already existing text buits still keep the previous text without overwriting
file2.write("I am Chegejr" ) #when i change from "Hello, welcome home" to "I am Chegejr" the previous txt remains when you the file
file2.close


# Reading the entire content of a file

file2 = open("C:\\Users\\user\\Desktop\\Py.thon\\file2.txt", "r") #make sure to include the read mode "r"
print(file2.read())
file2.close()

# Reading the content of a file line by line
file2 = open("C:\\Users\\user\\Desktop\\Py.thon\\file2.txt", "r") #make sure to include the read mode "r"
for line in file2:
    wordCount = line.split(" ")
    print(len(wordCount))
    print(line)
file2.close()

for x in demofile: # This loops through the file "demofile" and it prints each line everytime it loops through 
    #the file till all the content is printed
    print(x)
# Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.
