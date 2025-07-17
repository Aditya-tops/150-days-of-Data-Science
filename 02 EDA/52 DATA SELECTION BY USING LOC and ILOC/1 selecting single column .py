import pandas as pd

df = pd.read_csv("sales1.csv")

print(df.Product)
# or 
print(df["Product"])
# or
print(df.iloc[:,2])