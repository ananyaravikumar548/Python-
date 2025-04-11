# Two DataFrames to concatenate side-by-side (horizontally)
df_a = pd.DataFrame({'A': [1, 2, 3]})
df_b = pd.DataFrame({'B': ['X', 'Y', 'Z']})

# Concatenate along columns (axis=1)
concat_df = pd.concat([df_a, df_b], axis=1)
print("\nConcatenated DataFrame (Horizontally):\n", concat_df)
