import pandas as pd

df = pd.read_csv("dummy.csv")
print(df.nunique())

'''
Order ID         563
Customer Name     23
Product           21
Quantity           5
dtype: int64
'''