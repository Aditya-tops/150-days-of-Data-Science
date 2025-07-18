import pandas as pd

df = pd.read_csv("sales4.csv")

df1 = df.iloc[:5,]
print(df1)