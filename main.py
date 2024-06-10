import pandas as pds
import matplotlib.pyplot as pylt

# Read the CSV file
df = pds.read_csv('data.csv')

# Perform basic data analysis
print("Data Shape:", df.shape)
print("Data Columns:", df.columns)
print("Data Head:", df.head())
print("Data Info:", df.info())
print("Data Describe:", df.describe())

# Calculate total sales per product
total_sales_prdct = df.groupby('Product')['Sales'].sum().reset_index()
print("Total Sales per Product:")
print(total_sales_prdct)

# Plot total sales per product
pylt.figure(figsize=(8, 6))
pylt.bar(total_sales_prdct['Product'], total_sales_prdct['Sales'])
pylt.xlabel('Product')
pylt.ylabel('Total Sales')
pylt.title('Total Sales per Product')
pylt.savefig('total_sales_prdct.png')
pylt.show()

# Plot sales trends over time
pylt.figure(figsize=(8, 6))
pylt.plot(df['Date'], df['Sales'])
pylt.xlabel('Date')
pylt.ylabel('Sales')
pylt.title('Sales Trends over Time')
pylt.savefig('sales_trends_over_time.png')
pylt.show()