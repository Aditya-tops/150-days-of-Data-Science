import pandas as pd

df = pd.read_csv("sales4.csv")

rows = df.index[5:]
cols = ["Product_Name","Customer_Id"]

result = df.loc[rows,cols]
print(result)