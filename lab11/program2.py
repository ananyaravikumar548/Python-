# Sample DataFrames
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'ID': [3, 4],
    'City': ['Paris', 'London']
})

# Outer join on 'ID'
merged_df = pd.merge(df1, df2, on='ID', how='outer')
print("\nMerged (Outer Join):\n", merged_df)
