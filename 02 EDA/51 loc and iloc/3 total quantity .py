import pandas as pd

df = pd.read_csv("sales1.csv")
total = df["Quantity"].sum()
print(total)                        # 883.0

# or 
print("---------------------")
print(df.Quantity.sum())