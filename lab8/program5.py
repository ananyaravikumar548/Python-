scaler = MinMaxScaler()
df[["Age", "Income", "Purchase_Amount"]] = scaler.fit_transform(
df[["Age", "Income", "Purchase_Amount"]]
)
print(df)
