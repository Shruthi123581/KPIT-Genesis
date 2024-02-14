import pandas as pd

#Create a DataFrame
data = {'Name':['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25,30,35,40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

#Display the DataFrame
print("Original DataFrame: ")
print(df)

# Accessing specific columns
print("\nAccessing specific columns: ")
print(df['Name'])
print(df[['Name', 'Age']])

# Filterinf data based on a condition
print("\nFiltering data based on a condition: ")
filtered_df = df[df['Age']>30]
print(filtered_df)

# Adding a new column
df['Salary'] = [50000, 60000, 70000, 80000]
print("\nDataFrame after adding a new column: ")
print(df)

# Basic statistics
print("\nBasic statistics: ")
print(df.describe())
print(df.info())
