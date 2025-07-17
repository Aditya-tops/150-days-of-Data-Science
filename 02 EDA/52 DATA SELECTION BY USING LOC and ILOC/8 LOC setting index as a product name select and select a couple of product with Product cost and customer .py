import pandas as pd

df = pd.read_csv('sales2.csv')
df.set_index("Product name", inplace=True)

a = ["iPhone 9",'ThinkPad Laptop']
b = ["Product cost",'Customer name']

df1 = df.loc[a,b]
print(df1)