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