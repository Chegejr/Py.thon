# like for loops, while loops are used to execute a certain boock of code or statements so long as the condtion holds
# A program to print "Welcome All All All All"

i = 1

while i <= 5:
    print("Welcome", end="")
    x = 1
    while x <= 4:
        print(" All ", end="")
        x +=1

    i +=1
    print()