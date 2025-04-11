import pandas as pd

# Sample sales data
data = {
    'Category': ['Electronics', 'Electronics', 'Furniture', 'Furniture', 'Grocery'],
    'Sales': [1200, 1500, 800, 900, 400]
}
df = pd.DataFrame(data)

# Group by Category and calculate median sales
median_sales = df.groupby('Category')['Sales'].median().reset_index()

print("Grouped by Category (Median Sales):\n", median_sales)
