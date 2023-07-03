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

# Use of continue in while loop
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# Use of while loop in conjuction with else

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# Breaking out of a while loop when a certain condition is met

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
