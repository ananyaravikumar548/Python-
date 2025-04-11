import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("6Mcd.csv")

# Display first few rows to inspect
print("First 5 rows:\n", df.head())


# Plot using matplotlib
plt.figure(figsize=(10, 5))
plt.plot(df['DSA'], marker='o', linestyle='-')  # change 'Sales' to your target column
plt.title("Trend of Sales Over Time (Matplotlib)")
plt.xlabel("DSA")
plt.ylabel("Maths")
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot using seaborn
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x=df.index, y='Sales')  # change 'Sales' if needed
plt.title("Trend of Sales Over Time (Seaborn)")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.show()
