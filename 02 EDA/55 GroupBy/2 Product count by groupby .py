import pandas as pd

df = pd.read_csv("sales5.csv")

cols = ['Date','Product_Name']
grouped = df.groupby(cols)['Date']
result = grouped.count()
print(result)