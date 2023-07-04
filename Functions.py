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

# If one is not sure of how many parameters are required in a function, put a "*" before the name of the parameter
# This way the function will receive a tuple of arguments and will pick the right one accordingly.
# Below is how

def kids(*kid):
    print("The first born in our family is ",kid[2])
    # here we use indexing to access the right argument from the below given tuple
    # note if we dont include the indexing, the function will print all the entire tuple.

kids("mary","kim","junior","anorld")

# keyword arguments
# we can also pass arguments in the function by use of "Key = value" syntax
# Below is how

def players(player1, player2, player3,player4):
    print("The 4th player on the list is ", player4)
    print("The 3rd player on the list is ", player3)
    print("The 2nd player on the list is ", player2)
    print("Finally the best player of all time is ", player1)

players(player1="Cristiano",player2="messi",player3="zlatan",player4="lukaku")

