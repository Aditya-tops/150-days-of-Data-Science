import pandas as pd

df = pd.read_csv('sales2.csv')
df.set_index("Product name", inplace=True)

a = 'Samsung Galaxy S9 Plus'
df1 = df.loc[a]
print(df1)

a = ['iPhone 11','iPhone 7s']
df1 = df.loc[a]
print(df1)