# retail_sales_eda.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ✅ Replace this with the full path to your CSV file
csv_file_path = "D:/FULL STACK/PROJECT.2/retail_sales_dataset.csv"

# Check current directory (optional debug)
print("Looking for file in:", os.getcwd())

# Load dataset
df = pd.read_csv(csv_file_path)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# ===============================
# 📊 Descriptive Statistics
# ===============================
desc_stats = df[['Age', 'Quantity', 'Price per Unit', 'Total Amount']].describe().T
desc_stats['mode'] = df[['Age', 'Quantity', 'Price per Unit', 'Total Amount']].mode().iloc[0]
print("\n📊 Descriptive Statistics:\n", desc_stats)

# ===============================
# 📈 Time Series Sales Trend
# ===============================
monthly_sales = df.set_index('Date').resample('M')['Total Amount'].sum()
plt.figure(figsize=(12, 6))
monthly_sales.plot(marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales Amount')
plt.grid(True)
plt.tight_layout()
plt.show()

# ===============================
# 🧓 Age Distribution
# ===============================
plt.figure(figsize=(10, 5))
sns.histplot(df['Age'], bins=20, kde=True)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# ===============================
# 🧍 Gender Distribution
# ===============================
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Gender')
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# ===============================
# 🛍️ Product Category Sales
# ===============================
plt.figure(figsize=(10, 5))
category_sales = df.groupby('Product Category')['Total Amount'].sum().sort_values(ascending=False)
sns.barplot(x=category_sales.index, y=category_sales.values)
plt.title("Total Sales by Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
