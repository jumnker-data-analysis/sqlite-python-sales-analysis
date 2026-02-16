import sqlite3
import pandas as pd

# change this to your real db file path
DB_PATH=r"C:\Users\user\Documents\Data_Analytics\data_practice.db"
conn= sqlite3.connect(DB_PATH)

# 1) List tables
tables=pd.read_sql("select name from sqlite_master where type='table';", conn)
print("Tables:")
print(tables)

# 2) Read your sales table
df=pd.read_sql("select * from sales;", conn)
print("\nSales data:")
print(df)

# 3) Simple analysis: revenue per product
df["revenue"]=df["quantity"]*df["price"]
summary=df.groupby("product", as_index=False)["revenue"].sum().sort_values("revenue", ascending=False)
print("\nRevenue by product:")
print(summary)
conn.close()