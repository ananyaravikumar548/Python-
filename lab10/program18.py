import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("5ds_salaries.csv")

# Display the column names to check numeric ones
print(df.columns)

# Optional: Select only numeric columns for pair plot (recommended)
numeric_df = df.select_dtypes(include=["float64", "int64"])

# Create the pair plot
sns.pairplot(numeric_df)
plt.suptitle("Pair Plot for Numeric Columns in 5ds_salaries.csv", y=1.02)
plt.show()
