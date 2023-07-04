#  A function is a block of code that runs only when it is called.
#  A function can take in parameters and give data as its results
#  A function is defined using the "def" keyword.

#  below is how a function is created by use of the def keyword
def myfunction():
    print("I am a function")
    # Then after creating a function we call it inorder for it to run
myfunction()

# Below is function when called prints out the square of an odd number and for an even number prints out "even number"
def forloop():
    for i in range(1,6):
        if i%2 !=0:
            square = i*i
            print("The square of",i,"is",square)
        else:
            print("even number")
forloop()

# An argument is the value passed in the brackets when a fucntion is called
# A parameter refers to the variable passed in the brackets when defining a function

def helloworld(first_name, last_name):
    print(first_name,"",last_name)
helloworld("Hello", "World!")

