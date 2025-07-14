import pandas as pd

df = pd.read_csv("dummy.csv")
df2 = pd.read_csv("sales1.csv")
print(df.count())
print("-------------")
print(df2.count())

'''
--> count is use for missing value in coloumn

Order ID         590
Customer Name    600
Product          600
Quantity         600
dtype: int64
---------------------
Order ID         600
Customer Name    600
Product          600
Quantity         600
dtype: int64

'''