import pandas as pd

df = pd.read_csv('sales5.csv')
# print(df)

print(df.shape)
print(df.columns)
print(df.head())
print(df.tail())
print(df.info())
print("-----------------------------------------------------")
products = df.groupby("Product_Name")
p = products.size()
print(p)
print("-----------------------------------------------------")
emails = df.groupby(["Mail_Id"])
e = emails.size()
print(e)