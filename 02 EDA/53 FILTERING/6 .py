import pandas as pd

df = pd.read_csv("sales4.csv")

result = df.iloc[:5,]
print(result)