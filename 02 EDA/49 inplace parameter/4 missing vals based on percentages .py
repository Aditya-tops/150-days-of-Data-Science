# checking missing values bases based on parcentagte
import pandas as pd

df = pd.read_csv("fruits1.csv")

missvals = df.isna().sum()

per = ( missvals * 100) / len(df)

print(per.round(2))