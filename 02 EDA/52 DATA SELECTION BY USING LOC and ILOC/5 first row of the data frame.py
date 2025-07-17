import pandas as pd

df = pd.read_csv("sales2.csv")
s = df.iloc[:,0]
print(s)
print(df.iloc[:,1])
print(df.iloc[:,-1])
print(df.iloc[0:5])
print(df.iloc[:,0:2])
print(df.iloc[:,0:3])
print(df.iloc[0:5,0:2])
print(df.iloc[0:3,0:5])