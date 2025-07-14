import pandas as pd

data = pd.read_csv("sales1.csv")

print(data.dtypes)

'''
Order ID           int64
Customer Name     object
Product           object
Quantity         float64
dtype: object
'''