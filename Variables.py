# Python Variables
#variables are containers thatcan hold any data type eg. Text, numerical data
x = str(3)
y = int(3)
z = float(3)

if type(x) is str:
	print("Variable x is a string")
else:
	print("Variable x is not a string")
print(y)

if isinstance(y,int):
	print("Variable y is an integer")
else:
	print("Variable y is not an integer")
print(type(z))
print(z)

Fruits = ["Mango", "Orange", "Apple"]
print("My favorite fruits are", Fruits)

#Unpacking 
x, y, z = Fruits
print(x)
print(y)
print(z)

# Assigning one value to multiple variables

a = b = c = "Guava"
print(a)
print(b)
print(c)

# Calculate the total monthly expenses 
# the below : rent, groceries, gas ...are varibales or containers used to hold the amount of each spend for a given month 

rent = int(input("Enter the monthly rent fee: "));
airtime = int(input("Enter the monthly spend on airtime: "));
groceries = int(input(" Enter the monthly spend on groceries: "));
gas = int(input("Enter the monthly spend on gasoline: "));
water = int(input("Enter the monthly spend on water supply: "));
Others = int(input("Enter the amount spent on other unclassifiable items: "));

Total_Monthly_Spend = int(rent + airtime + groceries + gas + water + Others);

print("The total monthly expense for this month is ", + Total_Monthly_Spend);


#calculate the total time taken to travel from New York to Baltimore and from Baltimore to Pittsburg hence
#find the total time taken for the whole journey. Assuming no breaks are taken.

Distance_NY_Balt = 188
Distance_Balt_Pitts = 247
Total_Distance = 435
speed_Mph= 65
time_1 = Distance_NY_Balt / speed_Mph;
print("The time taken to travel from New York to Baltimore is: ", + time_1);

time_2 = Distance_Balt_Pitts / speed_Mph;
print("The time taken to travel from Baltimore to Pittsburg is: ", + time_2);

#Therefore the total time taken to travel the whole journey from New York to Pittsburg is as follows
Total_time = (time_1 + time_2);

#Another alternative of finding the total time taken for whole journey is as follows

Total_time = Total_Distance / speed_Mph;
print("The total time taken for the whole journey is: ", + Total_time)

