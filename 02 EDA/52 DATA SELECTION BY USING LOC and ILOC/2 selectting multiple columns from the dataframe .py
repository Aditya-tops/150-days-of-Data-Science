import pandas as pd

df = pd.read_csv("sales1.csv")

cols = ["Customer Name","Product"]
print(df[cols])
# or
print(df[["Customer Name","Product"]])
# or
print(df.iloc[:,1:3])