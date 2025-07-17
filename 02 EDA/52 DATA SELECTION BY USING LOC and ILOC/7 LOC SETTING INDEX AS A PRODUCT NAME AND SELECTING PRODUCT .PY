import pandas as pd

df = pd.read_csv('sales2.csv')
df.set_index("Product name", inplace=True)

a = 'iPhone 9'
df1 = df.loc[a]

print(df1.head(10))
