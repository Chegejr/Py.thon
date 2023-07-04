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

# If the number of keyword arguments is unkown, add "**" before the parameter name
#  this way the fucntion will receive arguments in a "dictionary" form where it will pick the right argument to display arccodingly
# Below is how

def names(**name):
    print("My last name is ",name["lname"])

names(fname="Josiah",lname="Chege jr",sur_name="Waweru")

# Passing a default argument into a function.
# this helps when the function that needs an argument is called with no argument in it, therefore it prints out the default argument
#  Below is how

def favorite_food(food="Fried chicken"):
    print("My favorite food is ", food)
favorite_food("Ugali")
favorite_food()
favorite_food("Pizza")

# A for loop in a function

def dishes(food):
    for x in food:
        print(x)
food = ["Ugali skuma", "Rice beans","Chapo beans","Pilau"]
dishes(food)

# Just like loops, functions cannot be empty, therefore incase yuh have an empty function use the pass statement
#  so that you don`t get an error when you call the function

def myfunction():
    pass
myfunction()

# Use of return to return a value in a function
def multiples(x):
        return 5*x
print(multiples(6))
print(multiples(5))
print(multiples(7))

# Python also accepts recursion, this means a defined function can call itself
# Recursion is a common mathematical and programming concept which has the benefits of looping through data to get a desired result
# In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). 
# We use the k variable as the data, which decrements (-1) every time we recurse. 
# The recursion ends when the condition is not greater than 0 (i.e. when it is 0)
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
