import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("5ds_salaries.csv")

# It's important to check the unique values in 'company_size' to understand the categories.
print(df['company_size'].unique())

# Visualize the relationship between 'experience_level' (categorical) and 'company_size' (categorical) using a count plot

# Matplotlib approach for count plot
plt.figure(figsize=(12, 6))
df['company_size'].value_counts().plot(kind='bar')
plt.xlabel("Company Size")
plt.ylabel("Count of Occurrences")
plt.title("Distribution of Company Sizes")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Seaborn approach for count plot (more concise)
plt.figure(figsize=(12, 6))
sns.countplot(x='company_size', data=df, order=df['company_size'].value_counts().index) # Order by frequency
plt.xlabel("Company Size")
plt.ylabel("Count of Occurrences")
plt.title("Distribution of Company Sizes")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# To see how company size varies across experience levels, we can use a grouped bar chart:
plt.figure(figsize=(14, 7))
sns.countplot(x='experience_level', hue='company_size', data=df, order=df['experience_level'].value_counts().index)
plt.xlabel("Experience Level")
plt.ylabel("Count of Occurrences")
plt.title("Company Size Distribution Across Experience Levels")
plt.xticks(rotation=45, ha='right')
plt.legend(title='Company Size')
plt.tight_layout()
plt.show()
