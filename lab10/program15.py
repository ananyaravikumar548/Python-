import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("4laptops.csv")

# Matplotlib boxplot: Weight
plt.figure(figsize=(6, 4))
plt.boxplot(df['Weight_kg'], notch=True, patch_artist=True)
plt.title("Matplotlib Boxplot - Laptop Weight")
plt.xlabel("Weight (kg)")
plt.grid(True)
plt.show()

# Matplotlib boxplot: Screen Size
plt.figure(figsize=(6, 4))
plt.boxplot(df['Screen_size_inches'], notch=True, patch_artist=True)
plt.title("Matplotlib Boxplot - Screen Size")
plt.xlabel("Screen Size (inches)")
plt.grid(True)
plt.show()

# Seaborn boxplot: Weight
plt.figure(figsize=(6, 4))
sns.boxplot(x=df["Weight_kg"])
plt.title("Seaborn Boxplot - Laptop Weight")
plt.show()

# Seaborn boxplot: Screen Size
plt.figure(figsize=(6, 4))
sns.boxplot(x=df["Screen_size_inches"])
plt.title("Seaborn Boxplot - Screen Size")
plt.show()
