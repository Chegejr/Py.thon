# run each code separately after the comment upto to the start of the next comment
# A "For" Loop is used to repeat a specific block of code a known number of times
# Calculating the total monthly expenses using for loop

monrthly_expenses = [40800, 45030, 38990, 54230, 43202, 49000, 48650]
total = 0
for x in monrthly_expenses:
    total += x
print(total)

# a program to show each month and its total expense and the final total expense for the given months
monrthly_expenses = [40800, 45030, 38990, 54230, 43202, 49000, 48650]
total = 0
for i in range(len(monrthly_expenses)):
    print("Total expenses for month", i+1, "is", monrthly_expenses[i])
    total += monrthly_expenses[i]
print("Total expenses", total)

# Calculating the total marks and the mean score

marks = [89, 76, 81, 66, 78, 93]
total = 0

for y in marks:
    total += y
print("Total marks for this semester: ", total)

mean = total / 6
print("The mean mark is: ", round(mean, 2))

if mean> 0 and mean<= 64:
    print("FAIL!")
elif mean >= 65 and mean <= 69:
    print("Mean grade is B-")
elif mean >= 70 and mean <= 74:
    print("Mean grade is B")
elif mean >= 75 and mean <=79:
    print("Mean grade is B+")
elif mean >80:
    print("Mean grade is A, PASS!")


# printing all even numbers in a range from 0-100

for x in range(0, 100):
    if x % 2== 0:
        print(x, "is EVEN")
    
