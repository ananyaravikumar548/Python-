df.fillna({"Age": df["Age"].mean()},inplace=True)
print(df)
