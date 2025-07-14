import pandas as pd

df = pd.read_csv("dummy.csv")
print(df.describe().round())
print("-------------------")
print(df.describe().round(2))
