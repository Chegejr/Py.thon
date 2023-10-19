# pandas is a python library that is used to analyze data "working with data sets"
# pandas allows us to clean and analyze big data and draw conclusions based on the statistical theories
# cleaning of data in pandas include deleting wrong values, removing empty cells or null values
# Pandas gives you answers about the data. Like:
# Is there a correlation between two or more columns?
# What is average value?
# Max value?
# Min value?
# A series is like a column in a table
import pandas as pd
players = ["cristiano","messi","trossard","neymar","benzo"] # a list of players
vplayers = pd.Series(players, index=["x","y","w","v","d"]) # Creating a pandas series and labels using the "index=" keyword. Indexing helps in accesing specific elements from the created pandas series or "column"
# function that takes in a list
print(vplayers["d"]) #accessing element at index "d" using the newly create labels. Output----->benzo

topscorers = {"Pele":45,"robinho":37,"maradona":48,"messi":53,"ibrahimovic":46,"cristiano":56,"lewandowski":49} # We can also pass a dictionary to a series function to create a series "column"
wplayers = pd.Series(topscorers)
print(topscorers["cristiano"]) # note that the dictionary keys becomes our new labels and we can now access their value through indexing. Output------>56

#  Datasets in pandas are multi deminsional tables called Dataframes.
#  Series is like a single column from a table , A DataFrame is the entire table
#  Create a DataFrame from two series

data = {
  "topgol": [63, 85, 59, 34, 46],
  "topass": [77, 45, 35, 79, 56]
}
xplayers =pd.DataFrame(data, index=["messi","cristiano","kevo","szcobolszai","neymar"])
print(xplayers) # Output below----->
"""
            topgol  topass
messi           63      77
cristiano       85      45
kevo            59      35
szoboszlai      34      79
neymar          46      56
"""

#  Reading data in a csv file. "comma separated files"
#  Data in a csv file is stored in plaint readable text
#  You can load data from a csv file into a dataframe object by use of pd.read_csv(name of the file with followed by ".csv" extension)
#  Check for the maximum number rows the system is currently set at using "print(pd.options.display.max_rows)" #Output--------> 60

import pandas as pd
print(pd.options.display.max_rows) #Output--------> 60
data = pd.read_csv("data.csv") #loading the data in our csv file into the dataframe object
print(data) # because our number of rows in our data is more(169) than the system set number of rows(60), 
# the output will only be the first and last 5 rows of the dataframe.
# Output below----->
"""
     Duration  Pulse  Maxpulse  Calories
0          60    110       130     409.1
1          60    117       145     479.0
2          60    103       135     340.0
3          45    109       175     282.4
4          45    117       148     406.0
..        ...    ...       ...       ...
164        60    105       140     290.8
165        60    110       145     300.0
166        60    115       145     310.2
167        75    120       150     320.4
168        75    125       150     330.4

"""

print(data.to_string()) # we can print out the entire data in the dataframe using the ".to_string()",
# function even when the number of system set number of rows is less(60) than the the data(169) in the dataframe

# another way of printing out the entire table without using the  ".to_string()" function is by setting the number of
#  system set rows to a number higher than the number of rows in the csv file lets say mayb 1000
# Run the following 4 lines of code separately
import pandas as pd
pd.options.display.max_rows = 1000
data = pd.read_csv("data.csv") 
print(data)

# Cleaning of empty or null values. 
# one way of dealing with null values is removing the rows containing the null values
# Use the "dropna()" to remove rows containing empty cells
# Also, instead of deleting or removing the row(s) we can replace  them with values
# this values can either be mean, max and or min
import pandas as pd
data = pd.read_csv("data.csv")
print(pd.options.display.max_rows) # Output---->60
pd.options.display.max_rows = 1000
print(pd.options.display.max_rows)# Output------>1000
print(data)
newdata = data.dropna() #by default the .dropna() returns a new dataframe and does not alter the original one
print(newdata.to_string())
# if by chance you dont want to return a new dataframe and want to make changes to the original dataframe then set "inplace = true"
data.dropna(inplace=True) #removing rows with empty cells by making changes to the original dataframe
print(data.to_string())
# Want to clean data by getting rid of empty and (or) null values? Use the ".dropna()" function to remove rows containing empty cells and (or) null values


import pandas as pd
# below is a football players dataset
data = {
    "Goals":{
        "Pele":677,
        "maradona":743,
        "cantona":432,
        "gaucho":333,
        "messi":834,
        "cristiano":850
    },
    "Assists":{
        "Pele":89,
        "maradona":112,
        "cantona":56,
        "gaucho":67,
        "messi":432,
        "cristiano":254
    },
    "Matches":{
        "Pele":867,
        "maradona":845,
        "cantona":654,
        "gaucho":340,
        "messi":1012,
        "cristiano":1115
    },
    "Age":{
        "Pele":72,
        "maradona":76,
        "cantona":54,
        "gaucho":45,
        "messi":36,
        "cristiano":37
    },
    "Scoring Frequency per min":{
        "Pele":"",
        "maradona":34,
        "cantona":"",
        "gaucho":23,
        "messi":"",
        "cristiano":8
    }
}
playerlibrary = pd.DataFrame(data)#loading the dataset into a pandas dataframe object
print(playerlibrary)# output below----->        
"""
          Goals  Assists  Matches  Age  Scoring Frequency per min
Pele         677       89      867   72                         
maradona     743      112      845   76                         34
cantona      432       56      654   54                         
gaucho       333       67      340   45                         23
messi        834      432     1012   36                         
cristiano    850      254     1115   37                          8
"""
playerlibrary.fillna("Brazil",inplace=True)
print(playerlibrary)
# also you can chose to replace the empty cells with the mean, median or mode of the column
# Median-------->The value at the centre when the values are arranged in Ascending order
# Mean---------->The average value "Add all values then divide by the number of values"
# Mode---------->The most occuring value in the data set column


# Run the following 7 lines of code separately.----->May not run if you dont have the csv file 'data.csv'
import pandas as pd
data = pd.read_csv('data.csv') #Loading the data in the csv file into a Pandas dataframe object
print(data.to_string()) #Printing out the entire dataset
x = data["Calories"].mean() #Calculating the mean of the calories column
print("The mean for the Calories column is:",x) #The mean is --------->375.79024390243904
data["Calories"].fillna(x.round(4),inplace=True) #Replacing the empty cells in the "Calories column" with the mean
print(data.to_string()) #checkout row "141" among other rows and note the empty or the null value "NaN" has been replaced by the mean(375.7902)

# Run the following 7 lines of code separately.----->May not run if you dont have the csv file 'data.csv'
import pandas as pd
data = pd.read_csv('data.csv') #Loading the data in the csv file into a Pandas dataframe object
print(data.to_string()) #Printing out the entire dataset
x = data["Calories"].median() #Calculating the median of the calories column
print("The median for the Calories column is:",x) #The median for the Calories column is: 318.6
data["Calories"].fillna(x,inplace=True) #Replacing the empty cells in the "Calories column" with the median
print(data.to_string()) #checkout row "141" among other rows and note the empty or the null cells "NaN" have been replaced by the median(318.6)

# Run the following 7 lines of code separately.----->May not run if you dont have the csv file 'data.csv'
import pandas as pd
data = pd.read_csv('data.csv') #Loading the data in the csv file into a Pandas dataframe object
print(data.to_string()) #Printing out the entire dataset
x = data["Calories"].mode()[0] #Calculating the mode of the calories column
print("The mode for the Calories column is:",x) #The mode for the Calories column is: 300
data["Calories"].fillna(x,inplace=True) #Replacing the empty cells in the "Calories column" with the mode
print(data.to_string()) #checkout row "141" among other rows and note the empty or the null cells "NaN" have been replaced by the mode(300.0)

# cleaning data of wrong format
# there are only two ways to deal with data of wrong format; remove the rows containing wrong format or convert all the values in the column in one same format
import pandas as pd
data = pd.read_csv("data.csv")
print(data.to_string())

# dealing with wrong data
# one is by replacing the wrong data by another value
for x in data.index:
    if data.loc[x,"Duration"]>120:
        data.loc[x,"Duration"] = 120
        
# another way of dealing with wrong data is through removing them
for x in data.index:
    if data.loc[x,"Duration"] > 120:
       data.drop(x,inplace=True)

# dealing with duplicates
import pandas as pd
data = pd.read_csv("data.csv")
print(data.duplicated) #checking if our dataset has duplicates. returns a boolean value for every row
# if there are any duplicates we have to remove them
data.drop_duplicates(inplace=True)#removing duplicates

import pandas as pd
data = pd.read_csv('data.csv')
print(data.corr()) #checking the relationship between the columns 
"""
          Duration     Pulse  Maxpulse  Calories
Duration  1.000000 -0.155408  0.009403  0.922717
Pulse    -0.155408  1.000000  0.786535  0.025121
Maxpulse  0.009403  0.786535  1.000000  0.203813
Calories  0.922717  0.025121  0.203813  1.000000
"""
# "Duration" and "Duration" has a perfect correlation which makes sense as a each column has a perfect relationship to itself
