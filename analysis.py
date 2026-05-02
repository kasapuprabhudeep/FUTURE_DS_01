import pandas as pd

df = pd.read_csv("sales.csv", encoding='latin1')

print(df.head())
print(df.shape)
print(df.columns)

print(df.info())
print(df.isnull().sum())

df.columns = df.columns.str.strip()
df = df.drop_duplicates()

df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')

df = df.dropna()

df['Month'] = df['Order Date'].dt.to_period('M')

print("Cleaned Data:")
print(df.head())
print(df.info())
print(df.shape)


# Monthly Sales
monthly_sales = df.groupby('Month')['Sales'].sum().sort_index()
print("\nMonthly Sales:\n", monthly_sales)

# Top Products
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
print("\nTop Products:\n", top_products)

# Category Sales
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print("\nCategory Sales:\n", category_sales)

# Sub-Category Sales
sub_category_sales = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False)
print("\nSub-Category Sales:\n", sub_category_sales)

# Region Sales
region_sales = df.groupby('Region')['Sales'].sum()
print("\nRegion Sales:\n", region_sales)

# Profit Analysis
profit_by_category = df.groupby('Category')['Profit'].sum()
print("\nProfit by Category:\n", profit_by_category)


import matplotlib.pyplot as plt

# 1. Monthly Sales Trend (Line Chart)
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()


# 2. Top Products (Bar Chart)
top_products.plot(kind='bar')
plt.title("Top 10 Products by Sales")
plt.xlabel("Product Name")
plt.ylabel("Sales")
plt.xticks(rotation=75)
plt.show()


# 3. Category Sales (Bar Chart)
category_sales.plot(kind='bar')
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()


# 4. Region Sales (Bar Chart)
region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()


# 5. Profit by Category (Extra - Very Important 🔥)
profit_by_category.plot(kind='bar')
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.show()

# After analysis or cleaning
print(df.shape)

# Save cleaned data
df.to_csv("cleaned_sales.csv", index=False)