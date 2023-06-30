
#In python we have the numbers and operators
#we have float or the decimal numbers, integers or the whole numbers
#For exaample lets build a simple calculator

integers = [12, 3, 67, 78, 9190];
print("The following are examples of integers: ", integers);

floating_numbers = [0.897, 89.7, 3.14, 19.897];
print("The following are examples of float numbers in python: ", floating_numbers);

num1 = int(float(input("Enter you first number: ")));
num2 = int(float(input("Enter your second number: ")));

operation_1 = num1 * num2;
print("The product of the two numbers is: ", + operation_1);

operation_2 = num1 ** num2;
print("The power form of the number is: ", + operation_2);

operation_3 = num1 / num2;
print("The division of the two number is: ", + operation_3);

operation_4 = num1 + num2;
print("The sum of the two numbers is: ", + operation_4);

operation_5 = num1 - num2;
print("The difference of the two numbers is: ", + operation_5);

operation_6 = num1 % num2;
print("The modulus of the two numbers is: ", + operation_6);






#calculate the total time taken to travel from New York to Baltimore and from Baltimore to Pittsburg hence
#find the total time taken for the whole journey. Assuming no breaks are taken.


Distance_NY_Balt = 188
Distance_Balt_Pitts = 247
Total_Distance = 435
speed_Mph= 65
time_1 = Distance_NY_Balt / speed_Mph;
print("The time taken to travel from New York to Baltimore is: ", + round(time_1, 2));

time_2 = Distance_Balt_Pitts / speed_Mph;
print("The time taken to travel from Baltimore to Pittsburg is: ", + round(time_2, 2));

#Therefore the total time taken to travel the whole journey from New York to Pittsburg is as follows
Total_time = (time_1 + time_2);

#Another alternative of finding the total time taken for whole journey is as follows

Total_time = Total_Distance / speed_Mph;
print("The total time taken for the whole journey is: ", + round(Total_time, 2));

