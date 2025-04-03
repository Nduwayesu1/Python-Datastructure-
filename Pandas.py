import pandas as pd
# create a list
dataSeries = [[90, 45, 3, 96, 5],[1,2,3,4,5]]
# create a Series
my_series=pd.DataFrame(dataSeries,index=['i',2])
# we use thsese indexes to access the data
# print the series
print(my_series['i'])
# python use also loc attribute to return the list of raws
print(my_series.loc[['i',2]])




# create a 2D list
data = [[90, 45, 3, 96, 5], [1, 2, 3, 4, 5]]

# create a DataFrame
my_dataframe = pd.DataFrame(data, index=['i', 2])

# we use these indexes to access the data
# print the row with index 'i'
print(my_dataframe.loc['i'])

# Python also uses the loc attribute to return specific rows
print(my_dataframe.loc[['i', 2]])