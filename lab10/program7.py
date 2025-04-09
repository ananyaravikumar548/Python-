import pandas as pd

# List of dictionaries with product information
products = [
    {'Name': 'Laptop', 'Category': 'Electronics', 'Price': 60000},
    {'Name': 'Chair', 'Category': 'Furniture', 'Price': 3000},
    {'Name': 'Pen', 'Category': 'Stationery', 'Price': 50}
]

# Creating a DataFrame
df = pd.DataFrame(products)

# Adding a new column for discounted price (10% discount)
df['Discounted Price'] = df['Price'] * 0.90

# Displaying the DataFrame
print("Product DataFrame with Discounted Price:")
print(df)
