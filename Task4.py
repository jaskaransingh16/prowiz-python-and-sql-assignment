# ==========================================
# Import Libraries
# ==========================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# ==========================================
# Load Data
# ==========================================
customers = pd.read_csv("Global+Electronics+Retailer/Customers.csv", encoding="latin1")
products = pd.read_csv("Global+Electronics+Retailer/Products.csv", encoding="latin1")
sales = pd.read_csv("Global+Electronics+Retailer/Sales.csv", encoding="latin1")

# ==========================================
# Merge Datasets
# ==========================================
data = sales.merge(customers, on="CustomerKey")
data = data.merge(products, on="ProductKey")

# ==========================================
# Create Total Sales Column
# ==========================================
data["Sales"] = data["Quantity"] * data["Unit Price USD"]

# ==========================================
# 1. Gender-wise Sales
# ==========================================
gender_sales = data.groupby("Gender")["Sales"].sum().reset_index()

plt.figure(figsize=(6,4))
sns.barplot(data=gender_sales, x="Gender", y="Sales")
plt.title("Gender-wise Sales")
plt.xlabel("Gender")
plt.ylabel("Total Sales")
plt.show()


# ==========================================
# 2. Brand Popularity (Top 10)
# ==========================================
brand_sales = (
    data.groupby("Brand")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

plt.figure(figsize=(8,5))
sns.barplot(data=brand_sales, x="Sales", y="Brand")
plt.title("Top 10 Popular Brands")
plt.xlabel("Total Sales")
plt.ylabel("Brand")
plt.show()


# ==========================================
# 3. Popular Brands Among Female Customers
# ==========================================
female_data = data[data["Gender"] == "Female"]

female_brand_sales = (
    female_data.groupby("Brand")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

plt.figure(figsize=(8,5))
sns.barplot(data=female_brand_sales, x="Sales", y="Brand")
plt.title("Popular Brands Among Female Customers")
plt.xlabel("Total Sales")
plt.ylabel("Brand")
plt.show()


# ==========================================
# 4. Popular Brands Among Male Customers
# ==========================================
male_data = data[data["Gender"] == "Male"]

male_brand_sales = (
    male_data.groupby("Brand")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

plt.figure(figsize=(8,5))
sns.barplot(data=male_brand_sales, x="Sales", y="Brand")
plt.title("Popular Brands Among Male Customers")
plt.xlabel("Total Sales")
plt.ylabel("Brand")
plt.show()


# ==========================================
# 5. Country-wise Sales
# ==========================================
country_sales = (
    data.groupby("Country")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

plt.figure(figsize=(10,6))
sns.barplot(data=country_sales, x="Sales", y="Country")
plt.title("Country-wise Sales")
plt.xlabel("Total Sales")
plt.ylabel("Country")
plt.show()


# ==========================================
# 6. Brand Popularity by Gender
# ==========================================
brand_gender_sales = (
    data.pivot_table(
        values="Sales",
        index="Brand",
        columns="Gender",
        aggfunc="sum"
    )
    .fillna(0)
)

brand_gender_sales = brand_gender_sales.sort_values(
    by=["Male","Female"],
    ascending=False
).head(10)

brand_gender_sales.plot(kind="bar", figsize=(10,6))
plt.title("Brand Popularity by Gender")
plt.xlabel("Brand")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()


# ==========================================
# 7. Brand with Most Categories
# ==========================================
brand_categories = (
    products.groupby("Brand")["Category"]
    .nunique()
    .sort_values(ascending=False)
)

print("\nBrand covering most categories:")
print(brand_categories.head())