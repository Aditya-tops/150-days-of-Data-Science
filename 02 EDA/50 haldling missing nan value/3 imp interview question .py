import pandas as pd

df1 = pd.read_csv("fruits1.csv")
df2 = df1.dropna()

print(df1)      # data + NaN vals (100GB)
print()
print(df2)      # only data no missing vals (95 GB)

# if you dont want new object thats possible
# use old object with inplace parameter like
print("------------------------------------------")
df1.dropna(inplace=True)
print(df1)
