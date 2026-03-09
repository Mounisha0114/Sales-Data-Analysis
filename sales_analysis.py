import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Superstore.csv", encoding="latin1")
# Show first rows
print(df.head())

# Convert date
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Sales by Region
region_sales = df.groupby("Region")["Sales"].sum()

region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()

# Monthly Sales Trend
df['Month'] = df['Order Date'].dt.month
monthly_sales = df.groupby("Month")["Sales"].sum()

plt.plot(monthly_sales)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Top Products
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

top_products.plot(kind="barh")
plt.title("Top 10 Products by Sales")
plt.show()

# Sales by Category
sns.barplot(x="Category", y="Sales", data=df)
plt.title("Sales by Category")
plt.show()
print("Total Sales:", df['Sales'].sum())

print("\nSales by Region:")
print(df.groupby("Region")["Sales"].sum())

print("\nTop 5 Products:")
print(df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head())

plt.figure()
sns.scatterplot(x="Sales", y="Profit", data=df)
plt.title("Profit vs Sales")
plt.show()

df['Month'] = df['Order Date'].dt.month
monthly_sales = df.groupby("Month")["Sales"].sum()
print(monthly_sales)

plt.figure()
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()