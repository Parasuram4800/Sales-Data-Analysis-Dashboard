import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

base_dir = Path(__file__).parent.parent

input_file = base_dir / "data" / "sales_data.csv"

df = pd.read_csv(input_file)

# ------------------
# Chart 1: Category
# ------------------
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()

plt.savefig(base_dir / "screenshots" / "sales_by_category.png")
plt.close()

# ------------------
# Chart 2: Region
# ------------------
region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()

plt.savefig(base_dir / "screenshots" / "sales_by_region.png")
plt.close()

# ------------------
# Chart 3: Monthly Trend
# ------------------
monthly_sales = df.groupby("Date")["Sales"].sum()

plt.figure(figsize=(10,5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(base_dir / "screenshots" / "monthly_sales_trend.png")
plt.close()

print("All charts generated successfully!")