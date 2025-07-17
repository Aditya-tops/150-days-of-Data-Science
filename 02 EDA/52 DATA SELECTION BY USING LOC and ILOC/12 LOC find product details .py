# select rows with specific product with all cols betweens order id and product cost

import pandas as pd

data = pd.read_csv('sales2.csv')

product = data['Product name'] == 'LG Washing Machine'
result = data.loc[product]
print(result)