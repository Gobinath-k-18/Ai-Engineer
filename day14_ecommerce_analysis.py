import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ecommerce_sales.csv")

print(df)

print("\nFirst 5 rows:")
print(df.head())

print("\nData information:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())



df = df.drop_duplicates()

print("\nAfter removing duplicates:")
print(df)

print("\nDuplicate rows after cleaning:")
print(df.duplicated().sum())

df["Sales"] = df["Quantity"] * df["Price"]
print("\nData with Sales:")
print(df)

total_sales = df["Sales"].sum()

print("Total Sales:", total_sales)

average_sales = df["Sales"].mean()

print("Average Sales:", average_sales)

highest_sales = df["Sales"].max()

print("Highest Sales:", highest_sales)

lowest_sales = df["Sales"].min()

print("Lowest Sales:", lowest_sales)

product_sales = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Product:")
print(product_sales)

best_product = product_sales.index[0]
best_sales = product_sales.iloc[0]

print("Best-selling product:", best_product)
print("Sales:", best_sales)

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Category:")
print(category_sales)


quantity_by_product = (
    df.groupby("Product")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\nQuantity Sold by Product:")
print(quantity_by_product)


df["Date"] = pd.to_datetime(df["Date"])

monthly_sales = (
    df.groupby(df["Date"].dt.month)["Sales"]
    .sum()
)

monthly_sales.plot(kind="bar")

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")

plt.show()

product_sales = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
)
product_sales.plot(kind="bar")

plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Sales by Product")

plt.show()

plt.scatter(df["Quantity"], df["Sales"])

plt.xlabel("Quantity")
plt.ylabel("Sales")
plt.title("Quantity vs Sales")

plt.show()

correlation = df[["Quantity", "Price", "Sales"]].corr()

print("\nCorrelation:")
print(correlation)