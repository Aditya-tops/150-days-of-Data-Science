# based on requiredment we can select cols from Datafrmae
# if select single column then it return series

import pandas as pd

df = pd.read_csv("sales1.csv")
print(df.Product.head())
print("-----------------------------")
print(df.Product[range(10,20)])