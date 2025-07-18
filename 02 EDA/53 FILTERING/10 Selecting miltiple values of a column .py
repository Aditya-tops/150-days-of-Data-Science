import pandas as pd

df = pd.read_csv("sales4.csv")

a = df.Product_Name == "LG Washing Machine"
b = df.Customer_Id == 1
c = a | b
result = df.loc[c]
print(result)               # [26278 rows x 5 columns]