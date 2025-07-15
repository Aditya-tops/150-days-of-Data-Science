import pandas as pd

df1 = pd.read_csv("sales3.csv")
print(df1)

df1.index = range(10,20)

print()
print(df1)

