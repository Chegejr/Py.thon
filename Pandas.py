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
vplayers = pd.Series(players, index=["x","y","w","v","d"]) # Creating a pandas series and labels using the index
# function that takes in a list
print(vplayers["d"]) #accessing values using the newly create labels

topscorers = {"Pele":45,"robinho":37,"maradona":48,"messi":53,"ibrahimovic":46,"cristiano":56,"lewandowski":49} # We can also pass a dictionary to a series function to create a series
wplayers = pd.Series(topscorers)
print(topscorers["cristiano"]) # note that the dictionary keys becomes our new labels and we can now access their value through indexing

#  Datasets in pandas are multi deminsional tables called Dataframes.
#  Series is like a single column from a table , A DataFrame is the entire table
#  Create a DataFrame from two series

data = {
  "topgol": [63, 85, 59, 34, 46],
  "topass": [77, 45, 35, 79, 56]
}
xplayers =pd.DataFrame(data, index=["messi","cristiano","kevo","szcobolszai","neymar"])
print(xplayers)

#  Reading data in a csv file. comma separated files
#  Data in a csv file is stored in plaint readable text
#  You can load a data from a csv file into a dataframe object by use of pd.read_csv("name of the file with .csv extension")
#  Check for the maximum number rows the system is currently set at

import pandas as pd
print(pd.options.display.max_rows) #Output--------> 60
data = pd.read_csv("data.csv") #loading the data in our csv file into the dataframe object
print(data) # because our number of rows in our data is more(169) than the system set number of rows(60), 
# the output will only be the first and last 5 rows of the dataframe

print(data.to_string()) # we can print out the entire data in the dataframe using the to_string(),
# function even when the number of system set number of rows is less(60) than the the data(169) in the dataframe

# another way of printing out the entire table without using the to_string() function is by setting the number of
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
print(pd.options.display.max_rows)
pd.options.display.max_rows = 1000
print(pd.options.display.max_rows)
print(data)
newdata = data.dropna() #by default the .dropna() returns a new dataframe and does not alter the original one
print(newdata.to_string())
# if by chance you dont want to return a new dataframe and want to make changes to the original datframe the set inplace value = true
data.dropna(inplace=True) #removing rows with empty cells by making changes to the original dataframe
print(data.to_string())
# Cleaning of empty or null values. Use the "dropna()" to remove empty rows


import pandas as pd
# below is a player library dataset
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
print(playerlibrary)# output below         
"""
          Goals  Assists  Matches  Age  Scoring Frequency per min
Pele         677       89      867   72                         
maradona     743      112      845   76                         34
cantona      432       56      654   54                         
gaucho       333       67      340   45                         23
messi        834      432     1012   36                         
cristiano    850      254     1115   37                          8
"""
# in my above created player dataframe i have the Nationality column with three empty cells
# Empty cells or null values can potentially give you wrong output after analyzing therefore they should be dealt with
# one way of dealing with empty cells or null values is through deleting or removing the rows containing the empty cells
# use the .dropna() to remove rows containing empty cells
# by default the .dropna() returns a new dataframe and does not alter the original one,
# if by chance you dont want to return a new dataframe but instead alter the original one, set "inplace =True"
playerlibrary.fillna("Brazil",inplace=True)
print(playerlibrary)
# also you can chose to replace the empty cells with the mean, median or mode of the column
# Median-------->The value at the centre when the values are arranged in Ascending order
# Mean---------->The average value "Add all values then divide by the number of values"
# Mode---------->The most occuring value in the data set column
