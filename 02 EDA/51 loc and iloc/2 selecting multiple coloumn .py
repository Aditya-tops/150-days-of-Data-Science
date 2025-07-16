import pandas as pd

df = pd.read_csv("sales1.csv")

d = ["Order ID","Customer Name"]

print(df[d])

print()
print("---------OR--------------")
print()

print(df[["Product","Quantity"]])

