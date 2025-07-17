import pandas as pd

df = pd.read_csv('sales2.csv')
df.set_index("Product name",inplace=True)

productname = ['iPhone 8','Google Phone']
df1 = df.loc[productname,'Order id':'Customer id']
print(df1)