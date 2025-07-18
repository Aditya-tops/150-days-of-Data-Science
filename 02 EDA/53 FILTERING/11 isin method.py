import pandas as pd

df = pd.read_csv("sales4.csv")

a = ["Macbook Pro Laptop"]
b = df.Product_Name.isin(a)

result = df.loc[b]
print(result)               # [15144 rows x 5 columns]