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