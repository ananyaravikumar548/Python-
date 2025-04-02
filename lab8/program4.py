Q1 = df["Income"].quantile(0.25,"lower") # 18.5
Q3 = df["Income"].quantile(0.75,"lower") # 31.5
IQR = Q3 - Q1 # 13.0
print(Q3, Q1, IQR)
# Identify outliers
lower_bound = Q1 - 1.5 * IQR # -1.0
upper_bound = Q3 + 1.5 * IQR # 51.0
outliers = df[(df["Income"] < lower_bound) | (df["Income"] > upper_bound)] #␣
↪Returns 60
print(outliers)
