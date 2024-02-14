import pandas as pd
import matplotlib.pyplot as plt

#Load a dataset from a CSV file
# Replace 'example_data.csv' with the actual file path or URL of your dataset
file_path = 'C:/Users/SHRUTHIB/Documents/Python/example_data.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame: ")
print(df.head())

# Get information about the DataFrame
print("\nDataFrame info: ")
print(df.info())

# Summary statistics
print("\nSummary statistics: ")
print(df.describe())

# Selecting specific coulmns
selected_coulmns = ['Name', 'Age', 'Salary']
selected_df = df[selected_coulmns]
print("\nDataFrame with selected columns: ")
print(selected_df.head())

# Grouping data by a coulmn and calculating statistics
grouped_data = df.groupby('City')['Salary'].mean()
print("\Average Salary by City: ")
print(grouped_data)

# Visualizing data (using matplotlib)
df.plot(x='Age', y='Salary', kind='scatter', title='Age vs. Salary')
# df.plot(x='Age', y='Salary', kind='bargraph', title='Age vs. Salary')
plt.show()