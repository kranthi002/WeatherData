# Before moving to the project lets understand the basic required data methods we are using in this project
# The below data methods are important in pandas

import pandas as pd

# reading the dataset from the path
data = pd.read_csv("D:/barcode/1. Weather Data.csv")
print(data)

# Analyse the data before working with data. Below are the few steps
# .head() it shows the first N rows in the data (by default, N = 5)
print(data.head()) 

#.shape it shows the total no of rows and columms of the dataframe
print(data.shape)

# .index this attribute provides the index of the dataframe
print(data.index)

# .columns it shows the name of each column
print(data.columns)

# .dtypes it shows the datatypes of the columns
print(data.dtypes)

# .unique it shows all the unique values. It can be append on a single column only. not on the whole dataframe
print(data['Weather'].unique())

# .nunique it shows the total no of unique values in each column. It can be applied on a single column as well as on whole dataframe
print(data.nunique())

#.count it shows the total non-null values in each column. It  can be applied on a single column as well as the whole dataframe
print(data.count())

#.value_counts it shows all unique values with their count. It  can be applied on a single column only.
print(data.value_counts('Weather'))

# .info provides basic information about the dataframe.
print(data.info())