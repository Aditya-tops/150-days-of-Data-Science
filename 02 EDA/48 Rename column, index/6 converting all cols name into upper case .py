import pandas as pd

df = pd.read_csv("sales3.csv")
df.columns = df.columns.str.upper()
print(df.head())