import pandas as pd

# load dataset
df = pd.read_csv("Sales.csv")

print("Dataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# top selling products
top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)

print("\nTop Selling Products:")
print(top_products.head())