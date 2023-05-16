import pandas as pd

# reading the dataset from the path
data = pd.read_csv("D:/barcode/1. Weather Data.csv")
# print(data)

# 1. Find all the unique 'Wind Speed' values in the data
print(data['Wind Speed_km/h'].nunique())    # Gives the total count of the Wind Speed column
print(data['Wind Speed_km/h'].unique())     # Gives all the unique values of the column


# 2. Find the number of times when the 'Weather is exactly Clear'?
print(data.groupby('Weather').get_group('Clear'))

# 3. Find the number of times when the 'Wind Speed was exactly 4 km/h'.
print(data[data['Wind Speed_km/h'] == 4])

# 4. Find out all the Null Values in the data
print(data.isnull().sum())

# 5. Rename the column name 'Weather' of the dataframe to 'Weather Condition'.
print(data.rename(columns = {'Weather': 'Weather Condition'}, inplace = True))

# 6. What is the mean 'Visibility'?
print(data.Visibility_km.mean())

# 7. What is the Standard Deviation of 'Pressure' in this data?
print(data.Press_kPa.std())

# 8. What is the Variance of 'Relative Humidity' in this data?
print(data['Rel Hum_%'].var())

# 9. Find all instances when 'Snow' was recorded?
print(data[data['Weather'].str.contains('Snow')].head(50))

# Find all instances when 'Wind Speed is above 24' and 'Visibility  is 25'.
print(data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)])

