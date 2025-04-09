import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("5ds_salaries.csv")

# Display skewness and kurtosis
print("Skewness of salary:", df["salary"].skew())
print("Kurtosis of salary:", df["salary"].kurt())

# Basic histogram
sns.histplot(df["salary"])
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Count")
plt.show()

# Histogram with KDE
sns.histplot(df["salary"], kde=True)
plt.title("Salary Distribution with KDE")
plt.xlabel("Salary")
plt.ylabel("Density")
plt.show()

# Distribution plot (Seaborn's old method)
sns.displot(df["salary"], kde=True)
plt.title("Salary Distribution using displot")
plt.xlabel("Salary")
plt.ylabel("Density")
plt.show()
