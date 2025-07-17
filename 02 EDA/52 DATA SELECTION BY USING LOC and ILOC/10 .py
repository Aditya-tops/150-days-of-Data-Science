# setting index product name and select ing a couple of product of product names with all cols bettween order id aND PRODUCT COST

import pandas as pd

df = pd.read_csv('sales2.csv')
df.set_index("Product name",inplace=True)

productname = ['iPhone 8','Google Phone']
df1 = df.loc[productname,'Order id':'Product cost']
print(df1)