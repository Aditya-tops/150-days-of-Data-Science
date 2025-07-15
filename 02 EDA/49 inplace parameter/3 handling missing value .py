import pandas as pd
'''
    1. Data(file)
    2. Create a dataframe
    3. Apply basic operations(shape, columns, head(), tail())
    4. checking missing values
        1.DataFrame having no missing values
            -> No need to handle
        2.Dataframe having missing values
            -> We need to handle missing values
    5.
'''
df = pd.read_csv("fruits1.csv")
print(df.head())
print()

result = df.isna().sum()
print(result.head())

# columns wise missing values df.isna().sum()
print("------------------")
df = pd.read_csv("fruits1.csv")
print(df.head())
print()

df2 = df.isna()
result = df2.sum()
print(result.head())



