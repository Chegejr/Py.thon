# If statements in python work in a such a way that, specific task is carried out if
#  the condition in checking evaluates to some value

# Using If statements to check if the input number is even or odd

x = input("Enter any digit: ")
x = int(x)

if x%2 == 0:
    print("The digit is even.");
else:
    print("The digit is odd.")



# A program to check in which country is a given city or county from.

kenya = ["Nairobi", "Nakuru", "Kisumu", "Mombasa", "Siaya"];
u_s_a = ["Ney York", "New Orleans", "California", "Philadephia"]
germany = ["munich", "Bayern", "wolsburg", "Hoffeinheim", "Nakuru"]

city = input("Enter a city, starting letter in Caps: ")

if city in kenya:
    print(city,"is located in Kenya")
elif city in germany:
    print(city,"is located in Germany")
elif city in u_s_a:
    print(city,"is located in United States")
else:
    print("Unable to locate the city due to limited info")

# A program to check if a given year is leap

year = input("Enter the year: ")
year = int(year)

if year%4 == 0:
    print("The year", year,"is a leap year")
else:
    print("The year",year," is not a leap year")