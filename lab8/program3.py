Q1 = df['Income'].quantile(0.25)
Q3 = df['Income'].quantile(0.75)
IQR = Q3 - Q1
print(Q3, Q1, IQR)
outlier_iqr = df[((df['Income'] < (Q1 - 1.5 * IQR)) | (df['Income'] > (Q3 + 1.5␣
↪* IQR)))]
print(outlier_iqr)
