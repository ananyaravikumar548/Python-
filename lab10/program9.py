import pandas as pd

# Load the CSV file
df = pd.read_csv('2salary.csv')

# Assuming the column name is 'Salary'
mean_value = df['Salary'].mean()
median_value = df['Salary'].median()
mode_value = df['Salary'].mode()[0]  # First mode if multiple
min_value = df['Salary'].min()
max_value = df['Salary'].max()
variance_value = df['Salary'].var()
std_dev_value = df['Salary'].std()

# Printing the results
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
print(f"Minimum: {min_value}")
print(f"Maximum: {max_value}")
print(f"Variance: {variance_value}")
print(f"Standard Deviation: {std_dev_value}")
