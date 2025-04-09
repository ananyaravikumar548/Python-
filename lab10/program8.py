import pandas as pd

# Sample data simulating 'Mod_null_values.csv'
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Bob'],
    'Q1': [10.0, None, 30.0, None, None],
    'Q2': [20, 25, 22, 27, 25]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Step 1: Show missing values
print("\nMissing values in the DataFrame:")
print(df.isnull().sum())

# Step 2: Fill all missing values with column mean (numeric columns only)
df.fillna(df.mean(numeric_only=True), inplace=True)

# Step 3: Display DataFrame after filling nulls
print("\nDataFrame after filling all null values:")
print(df)

# Step 4: Check for duplicates
print("\nChecking for duplicate rows:")
print(df.duplicated())

# Step 5: Drop duplicate rows
df.drop_duplicates(inplace=True)

# Final DataFrame
print("\nFinal DataFrame after dropping duplicates:")
print(df)
