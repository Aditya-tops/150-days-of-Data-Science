import pandas as pd

df = pd.read_csv("sales1.csv")
print(df.columns)                 

# Index(['Order ID', 'Customer Name', 'Product', 'Quantity'], dtype='object')

print("--------------------------------")

import pandas as pd

df = pd.read_csv("sales1.csv")

for col in df.columns:
    print(col)

'''
Order ID
Customer Name
Product
Quantity
'''